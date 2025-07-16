# Shuffllify User Guide 🎵

Welcome to Shuffllify! This guide will help you understand how to use this application to create truly random shuffled versions of your Spotify playlists.

## What is Shuffllify?

Shuffllify is a web application that creates truly random shuffled versions of your Spotify playlists. Unlike Spotify's built-in shuffle, which can sometimes feel predictable, Shuffllify uses cryptographically secure random number generation to ensure your playlists are shuffled in a truly random order.

## Key Features

- **True Randomness**: Uses Python's secure random number generator
- **Temporary Playlists**: Option to create playlists that auto-cleanup after 24 hours
- **Beautiful UI**: Modern, responsive design that works on all devices
- **Easy Cleanup**: One-click cleanup of all shuffled playlists
- **Secure**: OAuth 2.0 authentication with Spotify

## Getting Started

### Prerequisites

Before you can use Shuffllify, you'll need:

1. **A Spotify account** (free or premium)
2. **Python 3.7 or higher** installed on your computer
3. **Spotify Developer credentials** (we'll help you get these)

### Step 1: Get Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Click "Create App"
3. Fill in the app details:
   - **App name**: Shuffllify (or any name you prefer)
   - **App description**: A playlist shuffler application
   - **Website**: `http://localhost:5000`
   - **Redirect URI**: `http://127.0.0.1:5000/callback`
4. Click "Save"
5. Copy your **Client ID** and **Client Secret** (you'll need these later)

### Step 2: Set Up the Application

1. **Clone or download** the Shuffllify repository
2. **Open a terminal/command prompt** in the Shuffllify folder
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Create environment file**:
   - Copy `env_example.txt` to `.env`
   - Edit `.env` and add your Spotify credentials:
   ```
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here
   REDIRECT_URI=http://127.0.0.1:5000/callback
   ```

### Step 3: Run the Application

**Option A: Using the deployment script (recommended)**
- **Windows**: Double-click `deploy.bat`
- **Mac/Linux**: Run `./deploy.sh`

**Option B: Manual start**
```bash
python app.py
```

### Step 4: Access the Application

1. Open your web browser
2. Go to: `http://127.0.0.1:5000`
3. You should see the Shuffllify landing page

## How to Use Shuffllify

### First Time Setup

1. **Click "Connect with Spotify"** on the landing page
2. **Authorize the application** on Spotify's website
3. **You'll be redirected back** to your dashboard

### Creating Shuffled Playlists

1. **Browse your playlists** on the dashboard
2. **Choose a playlist** you want to shuffle
3. **Click "Shuffle Playlist"**
4. **Wait for processing** (you'll see a loading animation)
5. **Your shuffled playlist is ready!** Click "Open Shuffled Playlist" to view it in Spotify

### Temporary vs Permanent Playlists

**Temporary Playlists (Default)**
- ✅ **Enabled by default** - the toggle switch starts in the "on" position
- 🎲 **Special naming** - prefixed with "🎲 Shuffled:" and marked as "(Temporary)"
- 🗑️ **Auto-cleanup** - automatically removed after 24 hours
- 💡 **Perfect for** - one-time listening sessions, testing, or when you don't want playlist clutter

**Permanent Playlists**
- 🔄 **Toggle off** - turn off the "Create Temporary Playlists" switch
- 📝 **Standard naming** - prefixed with "Shuffled:"
- 💾 **Persistent** - remain in your Spotify account until manually deleted
- 💡 **Perfect for** - playlists you want to keep long-term

### Managing Your Playlists

#### Cleanup Feature
- **One-click cleanup**: Click "Clean up all shuffled playlists" to remove all shuffled playlists at once
- **Works on both types**: Removes both temporary and permanent shuffled playlists
- **Safe operation**: Only removes playlists created by Shuffllify

#### Manual Management
- **In Spotify**: You can manually delete any playlist from your Spotify account
- **Filtering**: Look for playlists starting with "Shuffled:" or "🎲 Shuffled:" to find Shuffllify-created playlists

## Understanding the Interface

### Dashboard Layout

```
┌─────────────────────────────────────┐
│ Shuffllify Dashboard                │
├─────────────────────────────────────┤
│ [Create Temporary Playlists] [ON]   │
│ Temporary playlists auto-cleanup    │
│ [Clean up all shuffled playlists]   │
├─────────────────────────────────────┤
│ ┌─────────┐ ┌─────────┐ ┌─────────┐ │
│ │Playlist1│ │Playlist2│ │Playlist3│ │
│ │[Shuffle]│ │[Shuffle]│ │[Shuffle]│ │
│ │[Open in │ │[Open in │ │[Open in │ │
│ │ Spotify]│ │ Spotify]│ │ Spotify]│ │
│ └─────────┘ └─────────┘ └─────────┘ │
└─────────────────────────────────────┘
```

### Button Functions

- **Shuffle Playlist**: Creates a new shuffled version of the selected playlist
- **Open in Spotify**: Opens the original playlist in Spotify
- **Clean up all shuffled playlists**: Removes all Shuffllify-created playlists

### Status Indicators

- **Loading animation**: Shows when a shuffle operation is in progress
- **Success modal**: Confirms when a playlist has been created successfully
- **Error modal**: Shows if something goes wrong

## Troubleshooting

### Common Issues

**"Cannot connect" error**
- Make sure the Flask server is running
- Check that you're accessing `http://127.0.0.1:5000` (not `localhost`)
- Verify no other application is using port 5000

**"Invalid redirect URI" error**
- Ensure your Spotify app's redirect URI is set to `http://127.0.0.1:5000/callback`
- Check that your `.env` file has the correct `REDIRECT_URI`

**"No client_id" error**
- Verify your `.env` file exists and contains your Spotify credentials
- Make sure the credentials are copied correctly from Spotify Developer Dashboard

**Shuffle button doesn't work**
- Try refreshing the page
- Check that you're logged into Spotify
- Ensure you have playlists in your Spotify account

**Cleanup button doesn't work**
- Make sure you have shuffled playlists to clean up
- Check the browser console for any error messages
- Try refreshing the page and trying again

### Getting Help

If you encounter issues not covered here:

1. **Check the browser console** (F12 → Console tab) for error messages
2. **Verify your setup** matches the requirements above
3. **Check the terminal** where you're running the Flask app for error messages
4. **Ensure your Spotify credentials** are correct and up-to-date

## Privacy and Security

### What Shuffllify Can Access
- **Your playlists**: To read and create shuffled versions
- **Your profile**: Basic account information for authentication
- **Playlist modification**: To create new playlists in your account

### What Shuffllify Cannot Access
- **Your password**: Never stored or transmitted
- **Your listening history**: Only accesses playlists you explicitly choose
- **Your personal data**: Only uses what's necessary for the service

### Data Storage
- **No database**: Shuffllify doesn't store your data permanently
- **Session storage**: Temporary data is stored only during your session
- **Spotify storage**: Playlists are stored in your Spotify account, not Shuffllify

## Advanced Usage

### Custom Shuffle Patterns
Currently, Shuffllify uses true random shuffling. Future versions may include:
- Custom shuffle algorithms
- Weighted randomization
- Genre-based shuffling

### Batch Operations
- Create multiple shuffled playlists in one session
- Use the cleanup feature to manage all at once
- Combine with Spotify's playlist features

### Integration with Spotify Features
- Use shuffled playlists with Spotify Connect
- Share shuffled playlists with friends
- Add shuffled playlists to your library

## Tips and Best Practices

### For Best Results
1. **Use temporary playlists** for one-time listening sessions
2. **Clean up regularly** to keep your playlist library organized
3. **Test with small playlists** first to understand the feature
4. **Keep your Spotify credentials** secure and up-to-date

### Performance Tips
- **Large playlists** may take longer to process
- **Multiple operations** can be performed in sequence
- **Browser refresh** if the interface becomes unresponsive

### Organization Tips
- **Use descriptive names** for your original playlists
- **Regular cleanup** prevents playlist clutter
- **Combine with Spotify folders** for better organization

## Future Features

Shuffllify is actively developed and may include:
- Collaborative playlist support
- Advanced shuffle algorithms
- Playlist analytics
- Mobile app version
- Social features

## Support and Feedback

If you have questions, suggestions, or encounter issues:
1. Check this guide first
2. Review the troubleshooting section
3. Check the project's issue tracker
4. Provide detailed information about your setup and the issue

---

**Enjoy your truly random music experience with Shuffllify! 🎵** 