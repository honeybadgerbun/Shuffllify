import os
import random
import secrets
import time
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Spotify API credentials
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI', 'http://localhost:5000/callback')

# Spotify OAuth scope
SCOPE = "playlist-read-private playlist-modify-public playlist-modify-private user-library-read"

def create_spotify_oauth():
    """Create Spotify OAuth object"""
    return SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    )

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/health')
def health_check():
    """Health check endpoint for Railway"""
    return jsonify({'status': 'healthy', 'message': 'Shuffllify is running'}), 200

@app.route('/login')
def login():
    """Initiate Spotify login"""
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    """Handle Spotify OAuth callback"""
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session["token_info"] = token_info
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    """User dashboard with playlists"""
    try:
        token_info = get_token()
    except:
        return redirect(url_for('login'))
    
    sp = spotipy.Spotify(auth=token_info['access_token'])
    user_playlists = sp.current_user_playlists()
    
    return render_template('dashboard.html', playlists=user_playlists['items'])

@app.route('/shuffle_playlist', methods=['POST'])
def shuffle_playlist():
    """Shuffle a playlist and create a new one"""
    try:
        token_info = get_token()
    except:
        return jsonify({'error': 'Authentication required'}), 401
    
    playlist_id = request.form.get('playlist_id')
    make_temporary = request.form.get('make_temporary', 'false').lower() == 'true'
    
    if not playlist_id:
        return jsonify({'error': 'Playlist ID required'}), 400
    
    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    try:
        # Get playlist details
        playlist = sp.playlist(playlist_id)
        playlist_name = playlist['name']
        tracks = playlist['tracks']['items']
        
        # Extract track URIs
        track_uris = [track['track']['uri'] for track in tracks if track['track']]
        
        if not track_uris:
            return jsonify({'error': 'No tracks found in playlist'}), 400
        
        # Shuffle tracks with true randomness
        shuffled_tracks = track_uris.copy()
        random.shuffle(shuffled_tracks)
        
        # Get current user
        user = sp.current_user()
        
        # Create new playlist with appropriate name and description
        if make_temporary:
            new_playlist_name = f"🎲 Shuffled: {playlist_name} (Temporary)"
            description = f"Temporary shuffled version of '{playlist_name}' created by Shuffllify - will be cleaned up automatically"
        else:
            new_playlist_name = f"Shuffled: {playlist_name}"
            description = f"Shuffled version of '{playlist_name}' created by Shuffllify"
        
        new_playlist = sp.user_playlist_create(
            user=user['id'],
            name=new_playlist_name,
            public=False,
            description=description
        )
        
        # Add shuffled tracks to new playlist (in chunks of 100 due to API limits)
        chunk_size = 100
        for i in range(0, len(shuffled_tracks), chunk_size):
            chunk = shuffled_tracks[i:i + chunk_size]
            sp.playlist_add_items(new_playlist['id'], chunk)
        
        # Store temporary playlist info in session for cleanup
        if make_temporary:
            temp_playlists = session.get('temp_playlists', [])
            temp_playlists.append({
                'id': new_playlist['id'],
                'name': new_playlist_name,
                'created_at': time.time()
            })
            session['temp_playlists'] = temp_playlists
        
        return jsonify({
            'success': True,
            'new_playlist_id': new_playlist['id'],
            'new_playlist_name': new_playlist_name,
            'new_playlist_url': new_playlist['external_urls']['spotify'],
            'tracks_shuffled': len(shuffled_tracks),
            'is_temporary': make_temporary
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_token():
    """Get valid token from session"""
    token_info = session.get("token_info", None)
    if not token_info:
        raise Exception("Token not found")
    
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    
    if is_expired:
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        session["token_info"] = token_info
    
    return token_info

@app.route('/cleanup_temp_playlists', methods=['POST'])
def cleanup_temp_playlists():
    """Clean up temporary playlists older than 24 hours"""
    try:
        token_info = get_token()
    except:
        return jsonify({'error': 'Authentication required'}), 401
    
    sp = spotipy.Spotify(auth=token_info['access_token'])
    user = sp.current_user()
    cleaned_count = 0
    
    try:
        # Get all user playlists
        user_playlists = sp.current_user_playlists()
        
        # Find all shuffled playlists (those starting with Shuffled: or 🎲 Shuffled:)
        for playlist in user_playlists['items']:
            if playlist['name'].startswith('Shuffled:') or playlist['name'].startswith('🎲 Shuffled:'):
                try:
                    # Unfollow/delete the shuffled playlist
                    sp.user_playlist_unfollow(user=user['id'], playlist_id=playlist['id'])
                    cleaned_count += 1
                except Exception as e:
                    print(f"Error deleting playlist {playlist['id']}: {e}")
                    continue
        
        # Also clean up session-stored temporary playlists
        temp_playlists = session.get('temp_playlists', [])
        current_time = time.time()
        # Keep only playlists created in the last 24 hours
        temp_playlists = [p for p in temp_playlists if current_time - p['created_at'] < 86400]
        session['temp_playlists'] = temp_playlists
        
        return jsonify({
            'success': True,
            'cleaned_count': cleaned_count,
            'remaining_temp_playlists': len(temp_playlists)
        })
        
    except Exception as e:
        return jsonify({'error': f'Error during cleanup: {str(e)}'}), 500

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Get port from environment variable (Railway sets PORT)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 