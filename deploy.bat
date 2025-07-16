@echo off
REM Shuffllify Deployment Script for Windows
echo 🎵 Welcome to Shuffllify Deployment! 🎵
echo ======================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH. Please install Python 3.7 or higher.
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist .env (
    echo ⚠️  .env file not found. Creating from template...
    if exist env_example.txt (
        copy env_example.txt .env >nul
        echo ✅ Created .env file from template.
        echo 📝 Please edit .env file with your Spotify API credentials:
        echo    - SPOTIFY_CLIENT_ID
        echo    - SPOTIFY_CLIENT_SECRET
        echo    - REDIRECT_URI (optional, defaults to http://localhost:5000/callback)
        echo.
        echo 🔗 Get your credentials from: https://developer.spotify.com/dashboard
        echo    Don't forget to add http://localhost:5000/callback to your app's Redirect URIs!
        pause
        exit /b 1
    ) else (
        echo ❌ env_example.txt not found. Please create a .env file manually.
        pause
        exit /b 1
    )
)

REM Check if virtual environment exists
if not exist venv (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Check if environment variables are set
findstr "your_spotify_client_id_here" .env >nul
if not errorlevel 1 (
    echo ❌ Please update your .env file with actual Spotify API credentials.
    echo 🔗 Get your credentials from: https://developer.spotify.com/dashboard
    pause
    exit /b 1
)

echo ✅ Setup complete!
echo.
echo 🚀 Starting Shuffllify...
echo 📱 Open your browser and go to: http://localhost:5000
echo 🛑 Press Ctrl+C to stop the server
echo.

REM Run the application
python app.py 