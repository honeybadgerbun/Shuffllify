# Shuffllify 🎵

A web application that creates truly random shuffled versions of your Spotify playlists using Python's cryptographically secure random number generator.

## Features

- **True Randomness**: Uses Python's `random.shuffle()` with cryptographically secure random number generation
- **Beautiful UI**: Modern, responsive design with Tailwind CSS
- **Spotify Integration**: Seamless OAuth authentication with Spotify
- **Instant Results**: Create shuffled playlists immediately
- **User-Friendly**: Simple, intuitive interface

## How It Works

1. **Connect**: Link your Spotify account securely via OAuth
2. **Select**: Choose any playlist from your library
3. **Shuffle**: We create a truly random order using Python's secure random generator
4. **Enjoy**: Your new shuffled playlist is ready in Spotify!

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- A Spotify account
- Spotify Developer credentials

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Shuffllify
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Spotify API Credentials

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new application
3. Add `http://localhost:5000/callback` to the Redirect URIs
4. Copy your Client ID and Client Secret

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
# Copy the example file
cp env_example.txt .env
```

Edit `.env` with your Spotify credentials:

```env
SPOTIFY_CLIENT_ID=your_spotify_client_id_here
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here
REDIRECT_URI=http://localhost:5000/callback
```

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. Visit the application in your browser
2. Click "Connect with Spotify"
3. Authorize the application to access your Spotify account
4. Browse your playlists
5. Click "Shuffle Playlist" on any playlist
6. Your shuffled playlist will be created and you can open it in Spotify

## Technical Details

### Randomness Implementation

The application uses Python's built-in `random.shuffle()` function, which:
- Uses the Mersenne Twister PRNG by default
- Can be seeded with `random.seed()` for reproducible results
- Provides cryptographically secure randomness when the system's entropy pool is used

### API Endpoints

- `GET /` - Landing page
- `GET /login` - Initiate Spotify OAuth
- `GET /callback` - Handle OAuth callback
- `GET /dashboard` - User dashboard with playlists
- `POST /shuffle_playlist` - Create shuffled playlist
- `GET /logout` - Logout user

### Security Features

- OAuth 2.0 authentication with Spotify
- Secure session management
- Environment variable configuration
- No sensitive data stored in code

## Deployment

### Local Development

```bash
python app.py
```

### Free Public Deployment (Recommended)

#### Railway - Best Free Option for Public Access 🚀
- **Completely Free**: 500 hours/month (no credit card required)
- **Public Access**: Anyone can use your app worldwide
- **Easy Setup**: Just connect GitHub and deploy
- **Automatic HTTPS**: Secure connections included
- **Custom Domains**: Add your own domain later

**📖 Complete deployment guide: [RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md)**

**Quick deploy:**
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub account
3. Select your Shuffllify repository
4. Add environment variables in Railway dashboard
5. Deploy automatically
6. Share your public URL with the world!

#### 2. Render
- **Free tier**: 750 hours/month
- **Easy setup**: GitHub integration
- **Python support**: Full Flask compatibility
- **Custom domains**: Free SSL included

**Quick deploy:**
1. Go to [render.com](https://render.com)
2. Connect GitHub and select your repo
3. Choose "Web Service"
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`
6. Add environment variables

#### 3. PythonAnywhere
- **Free tier**: 512MB storage, limited CPU
- **Python-focused**: Perfect for Python apps
- **Easy setup**: Web-based interface
- **Custom domains**: Supported

**Quick deploy:**
1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload your code or clone from GitHub
3. Set up a web app with Flask
4. Configure environment variables
5. Deploy

#### 4. Fly.io
- **Free tier**: 3 shared-cpu VMs, 3GB persistent volume
- **Global deployment**: Multiple regions
- **Docker support**: Container-based deployment
- **Custom domains**: Free SSL

**Quick deploy:**
1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Run: `fly launch`
3. Follow the setup wizard
4. Deploy with: `fly deploy`

#### 5. Replit
- **Free tier**: Unlimited public projects
- **Web-based IDE**: Code and deploy in browser
- **Instant deployment**: No setup required
- **Collaboration**: Built-in features

**Quick deploy:**
1. Go to [replit.com](https://replit.com)
2. Create new Python project
3. Upload your code or import from GitHub
4. Add environment variables in Secrets
5. Run and deploy

### Paid Options (If you need more resources)

#### Heroku
- **Basic Dyno**: $7/month
- **Standard Dyno**: $25/month
- **Most popular**: Excellent documentation and support

#### DigitalOcean App Platform
- **Starting at**: $5/month
- **More control**: Full server access
- **Scalable**: Easy to upgrade

### Local Deployment (Free)

#### Run on Your Own Computer
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Access at http://127.0.0.1:5000
```

#### Share with ngrok (Free)
```bash
# Install ngrok
# Run your Flask app
python app.py

# In another terminal
ngrok http 5000

# Share the ngrok URL with others
```

### Deployment Considerations

**For all free platforms:**
- Update your Spotify app's redirect URI to match your deployment URL
- Set environment variables in the platform's dashboard
- Consider the free tier limitations (CPU, memory, bandwidth)
- Monitor usage to avoid hitting limits

**Recommended for beginners:**
1. **Railway** - Easiest setup, generous free tier
2. **Render** - Good documentation, reliable
3. **Replit** - No setup required, instant deployment

**Recommended for learning:**
1. **PythonAnywhere** - Python-focused, educational
2. **Local + ngrok** - Learn the deployment process
3. **Fly.io** - Learn containerization

#### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:

```bash
docker build -t shuffllify .
docker run -p 5000:5000 --env-file .env shuffllify
```

#### Manual Production Deployment

For production deployment, consider:

1. **Environment Variables**: Set production Spotify credentials
2. **Redirect URI**: Update to your production domain
3. **Web Server**: Use Gunicorn or uWSGI with a reverse proxy
4. **HTTPS**: Ensure SSL/TLS encryption
5. **Environment**: Use a production Python environment

Example with Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## File Structure

```
Shuffllify/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── env_example.txt       # Environment variables template
├── README.md             # This file
├── templates/
│   ├── index.html        # Landing page
│   └── dashboard.html    # User dashboard
└── .gitignore           # Git ignore file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is not affiliated with Spotify. It uses the Spotify Web API for educational and personal use purposes.

## Support

If you encounter any issues:

1. Check that your Spotify API credentials are correct
2. Ensure your redirect URI matches your Spotify app settings
3. Verify that your playlists are accessible (not private)
4. Check the browser console for any JavaScript errors

## Future Enhancements

- [ ] Support for collaborative playlists
- [ ] Custom shuffle algorithms
- [ ] Playlist analytics
- [ ] Mobile app version
- [ ] Batch playlist processing 