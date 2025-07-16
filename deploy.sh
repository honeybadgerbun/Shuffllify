#!/bin/bash

# Shuffllify Deployment Script
echo "🎵 Welcome to Shuffllify Deployment! 🎵"
echo "======================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from template..."
    if [ -f env_example.txt ]; then
        cp env_example.txt .env
        echo "✅ Created .env file from template."
        echo "📝 Please edit .env file with your Spotify API credentials:"
        echo "   - SPOTIFY_CLIENT_ID"
        echo "   - SPOTIFY_CLIENT_SECRET"
        echo "   - REDIRECT_URI (optional, defaults to http://localhost:5000/callback)"
        echo ""
        echo "🔗 Get your credentials from: https://developer.spotify.com/dashboard"
        echo "   Don't forget to add http://localhost:5000/callback to your app's Redirect URIs!"
        exit 1
    else
        echo "❌ env_example.txt not found. Please create a .env file manually."
        exit 1
    fi
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check if environment variables are set
if grep -q "your_spotify_client_id_here" .env; then
    echo "❌ Please update your .env file with actual Spotify API credentials."
    echo "🔗 Get your credentials from: https://developer.spotify.com/dashboard"
    exit 1
fi

echo "✅ Setup complete!"
echo ""
echo "🚀 Starting Shuffllify..."
echo "📱 Open your browser and go to: http://localhost:5000"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

# Run the application
python app.py 