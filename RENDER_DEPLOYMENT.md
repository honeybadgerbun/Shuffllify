# Render Deployment Guide - Free Public Hosting 🚀

This guide will help you deploy Shuffllify to Render for free, making it accessible to anyone on the internet and compatible with Spotify's OAuth requirements.

## Why Render?

✅ **Completely Free** - 750 hours/month (generous free tier)  
✅ **Spotify-Compatible** - `.onrender.com` domains are allowed by Spotify  
✅ **Easy Setup** - Connect GitHub and deploy automatically  
✅ **Automatic HTTPS** - Secure connections included  
✅ **Custom Domains** - Add your own domain later  
✅ **No Credit Card Required** - Truly free  

## Prerequisites

1. **GitHub account** with your Shuffllify repository
2. **Spotify Developer account** with your app credentials
3. **Render account** (free signup)

## Step 1: Prepare Your Repository

### 1.1 Push to GitHub
Make sure your Shuffllify code is pushed to a GitHub repository:

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 1.2 Verify Files
Ensure these files are in your repository:
- `app.py`
- `requirements.txt`
- `render.yaml` (optional but recommended)
- `templates/` folder

## Step 2: Deploy to Render

### 2.1 Create Render Account
1. Go to [render.com](https://render.com)
2. Click "Get Started for Free"
3. Sign up with GitHub (recommended) or email

### 2.2 Create New Web Service
1. Click "New +" button
2. Select "Web Service"
3. Click "Connect" next to your GitHub repository
4. Select your Shuffllify repository

### 2.3 Configure the Service
Fill in the configuration:

**Basic Settings:**
- **Name**: `shuffllify` (or any name you prefer)
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main` (or your default branch)

**Build & Deploy:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python app.py`

**Advanced Settings:**
- **Health Check Path**: `/health`
- **Auto-Deploy**: ✅ Enabled (recommended)

### 2.4 Create the Service
Click "Create Web Service"

## Step 3: Configure Environment Variables

### 3.1 Access Environment Variables
1. Click on your deployed service in Render dashboard
2. Go to the "Environment" tab
3. Click "Add Environment Variable"

### 3.2 Add Spotify Credentials
Add these environment variables:

```
SPOTIFY_CLIENT_ID=your_spotify_client_id_here
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here
REDIRECT_URI=https://your-app-name.onrender.com/callback
```

**Important**: Replace `your-app-name` with your actual Render app name.

### 3.3 Get Your App URL
1. Go to the "Settings" tab
2. Copy your "URL" (looks like `https://your-app-name.onrender.com`)

## Step 4: Update Spotify App Settings

### 4.1 Go to Spotify Developer Dashboard
1. Visit [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Click on your Shuffllify app
3. Click "Edit Settings"

### 4.2 Update Redirect URI
In the "Redirect URIs" section:
1. **Remove** any old URIs (like Railway or localhost)
2. **Add** your Render URL + `/callback`:
   ```
   https://your-app-name.onrender.com/callback
   ```
3. Click "Save"

## Step 5: Test Your Deployment

### 5.1 Access Your App
1. Go to your Render app URL
2. You should see the Shuffllify landing page

### 5.2 Test Spotify Connection
1. Click "Connect with Spotify"
2. Complete the OAuth flow
3. Test creating a shuffled playlist

### 5.3 Check Logs
If something doesn't work:
1. Go to Render dashboard
2. Click on your service
3. Go to "Logs" tab
4. Check for any errors

## Step 6: Make It Public

### 6.1 Share Your App
Your app is now publicly accessible! Share the URL:
```
https://your-app-name.onrender.com
```

### 6.2 Optional: Custom Domain
If you have a domain:
1. Go to Render dashboard → Settings
2. Click "Custom Domain"
3. Follow the DNS setup instructions

## Troubleshooting

### Common Issues

**Issue: "Application Error"**
- Check Render logs for specific errors
- Verify environment variables are set correctly
- Ensure all files are pushed to GitHub

**Issue: "Invalid redirect URI"**
- Make sure Spotify app redirect URI matches exactly
- Check that Render URL is correct
- Verify no extra spaces in the URI

**Issue: "No client_id"**
- Verify environment variables in Render dashboard
- Check variable names are exactly correct
- Redeploy after adding variables

**Issue: App won't start**
- Check `render.yaml` configuration
- Verify `requirements.txt` has all dependencies
- Check logs for Python errors

**Issue: Build fails**
- Check that all dependencies are in `requirements.txt`
- Verify Python version compatibility
- Check build logs for specific errors

### Useful Render Commands

```bash
# View logs (in Render dashboard)
# Go to your service → Logs tab

# Manual deploy
# Go to your service → Manual Deploy

# Check service status
# Go to your service → Overview tab
```

## Monitoring and Maintenance

### 1. Check Usage
- Render dashboard shows usage statistics
- Monitor hours used (750 free hours/month)
- Check service status

### 2. View Logs
- Go to Render dashboard → Your service → Logs
- Monitor for errors or issues
- Check build and runtime logs

### 3. Update Your App
- Push changes to GitHub
- Render automatically redeploys (if auto-deploy is enabled)
- Or manually deploy from dashboard

## Free Tier Limitations

### What's Included (750 hours/month):
- ✅ Public web app hosting
- ✅ Automatic HTTPS
- ✅ Custom domains
- ✅ GitHub integration
- ✅ Environment variables
- ✅ Logs and monitoring
- ✅ Auto-deploy from GitHub

### What's Not Included:
- ❌ 24/7 uptime (sleeps after inactivity)
- ❌ Unlimited bandwidth
- ❌ Advanced features (databases, etc.)

### Tips for Free Tier:
- **750 hours = ~31 days** of continuous running
- App sleeps after 15 minutes of inactivity
- Wakes up automatically when accessed
- Perfect for personal projects and demos

## Comparison: Render vs Railway

| Feature | Render | Railway |
|---------|--------|---------|
| Free Hours | 750/month | 500/month |
| Spotify Compatible | ✅ Yes | ❌ No (custom domains only) |
| Setup Difficulty | Easy | Easy |
| Auto-deploy | ✅ Yes | ✅ Yes |
| Custom Domains | ✅ Yes | ✅ Yes |

## Next Steps

### After Successful Deployment:
1. **Test thoroughly** with different users
2. **Monitor usage** in Render dashboard
3. **Share your app** with friends and family
4. **Consider upgrades** if you need more resources

### Future Enhancements:
- Add a custom domain
- Set up monitoring alerts
- Consider paid plan for 24/7 uptime
- Add database for user analytics

## Support

If you encounter issues:

1. **Check Render logs** first
2. **Verify environment variables**
3. **Check Spotify app settings**
4. **Render documentation**: [render.com/docs](https://render.com/docs)
5. **Render community**: [community.render.com](https://community.render.com)

---

**🎉 Congratulations! Your Shuffllify app is now live and accessible to anyone on the internet!**

**Your app URL**: `https://your-app-name.onrender.com`

**Share it with the world! 🌍**

**Note**: This deployment is fully compatible with Spotify's OAuth requirements! 