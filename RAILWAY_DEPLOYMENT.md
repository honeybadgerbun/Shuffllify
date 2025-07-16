# Railway Deployment Guide - Free Public Hosting 🚀

This guide will help you deploy Shuffllify to Railway for free, making it accessible to anyone on the internet.

## Why Railway?

✅ **Completely Free** - 500 hours/month (enough for personal projects)  
✅ **Public Access** - Anyone can use your app  
✅ **Easy Setup** - Just connect GitHub and deploy  
✅ **Automatic HTTPS** - Secure connections included  
✅ **Custom Domains** - Add your own domain later  
✅ **No Credit Card Required** - Truly free  

## Prerequisites

1. **GitHub account** with your Shuffllify repository
2. **Spotify Developer account** with your app credentials
3. **Railway account** (free signup)

## Step 1: Prepare Your Repository

### 1.1 Push to GitHub
Make sure your Shuffllify code is pushed to a GitHub repository:

```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### 1.2 Verify Files
Ensure these files are in your repository:
- `app.py`
- `requirements.txt`
- `railway.json`
- `templates/` folder
- `.env` (for local testing only)

## Step 2: Deploy to Railway

### 2.1 Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Sign up with GitHub (recommended) or email

### 2.2 Deploy from GitHub
1. Click "Deploy from GitHub repo"
2. Select your Shuffllify repository
3. Click "Deploy Now"

### 2.3 Wait for Build
- Railway will automatically detect it's a Python app
- It will install dependencies from `requirements.txt`
- Build process takes 2-5 minutes

## Step 3: Configure Environment Variables

### 3.1 Access Your Project
1. Click on your deployed project in Railway dashboard
2. Go to the "Variables" tab

### 3.2 Add Spotify Credentials
Add these environment variables:

```
SPOTIFY_CLIENT_ID=your_spotify_client_id_here
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here
REDIRECT_URI=https://your-app-name.railway.app/callback
```

**Important**: Replace `your-app-name` with your actual Railway app name.

### 3.3 Get Your App URL
1. Go to the "Settings" tab
2. Copy your "Domain" URL (looks like `https://your-app-name.railway.app`)

## Step 4: Update Spotify App Settings

### 4.1 Go to Spotify Developer Dashboard
1. Visit [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Click on your Shuffllify app
3. Click "Edit Settings"

### 4.2 Update Redirect URI
In the "Redirect URIs" section:
1. **Remove** the old localhost URI
2. **Add** your Railway URL + `/callback`:
   ```
   https://your-app-name.railway.app/callback
   ```
3. Click "Save"

## Step 5: Test Your Deployment

### 5.1 Access Your App
1. Go to your Railway app URL
2. You should see the Shuffllify landing page

### 5.2 Test Spotify Connection
1. Click "Connect with Spotify"
2. Complete the OAuth flow
3. Test creating a shuffled playlist

### 5.3 Check Logs
If something doesn't work:
1. Go to Railway dashboard
2. Click on your project
3. Go to "Deployments" tab
4. Click on the latest deployment
5. Check the logs for errors

## Step 6: Make It Public

### 6.1 Share Your App
Your app is now publicly accessible! Share the URL:
```
https://your-app-name.railway.app
```

### 6.2 Optional: Custom Domain
If you have a domain:
1. Go to Railway dashboard → Settings
2. Click "Add Domain"
3. Follow the DNS setup instructions

## Troubleshooting

### Common Issues

**Issue: "Application Error"**
- Check Railway logs for specific errors
- Verify environment variables are set correctly
- Ensure all files are pushed to GitHub

**Issue: "Invalid redirect URI"**
- Make sure Spotify app redirect URI matches exactly
- Check that Railway URL is correct
- Verify no extra spaces in the URI

**Issue: "No client_id"**
- Verify environment variables in Railway dashboard
- Check variable names are exactly correct
- Redeploy after adding variables

**Issue: App won't start**
- Check `railway.json` configuration
- Verify `requirements.txt` has all dependencies
- Check logs for Python errors

### Useful Railway Commands

```bash
# Install Railway CLI (optional)
npm install -g @railway/cli

# Login to Railway
railway login

# Link to your project
railway link

# View logs
railway logs

# Deploy manually
railway up
```

## Monitoring and Maintenance

### 1. Check Usage
- Railway dashboard shows usage statistics
- Monitor hours used (500 free hours/month)
- Check deployment status

### 2. View Logs
- Go to Railway dashboard → Deployments
- Click on any deployment to view logs
- Monitor for errors or issues

### 3. Update Your App
- Push changes to GitHub
- Railway automatically redeploys
- No manual intervention needed

## Free Tier Limitations

### What's Included (500 hours/month):
- ✅ Public web app hosting
- ✅ Automatic HTTPS
- ✅ Custom domains
- ✅ GitHub integration
- ✅ Environment variables
- ✅ Logs and monitoring

### What's Not Included:
- ❌ 24/7 uptime (sleeps after inactivity)
- ❌ Unlimited bandwidth
- ❌ Advanced features (databases, etc.)

### Tips for Free Tier:
- **500 hours = ~20 days** of continuous running
- App sleeps after 15 minutes of inactivity
- Wakes up automatically when accessed
- Perfect for personal projects and demos

## Next Steps

### After Successful Deployment:
1. **Test thoroughly** with different users
2. **Monitor usage** in Railway dashboard
3. **Share your app** with friends and family
4. **Consider upgrades** if you need more resources

### Future Enhancements:
- Add a custom domain
- Set up monitoring alerts
- Consider paid plan for 24/7 uptime
- Add database for user analytics

## Support

If you encounter issues:

1. **Check Railway logs** first
2. **Verify environment variables**
3. **Check Spotify app settings**
4. **Railway documentation**: [docs.railway.app](https://docs.railway.app)
5. **Railway Discord**: [discord.gg/railway](https://discord.gg/railway)

---

**🎉 Congratulations! Your Shuffllify app is now live and accessible to anyone on the internet!**

**Your app URL**: `https://your-app-name.railway.app`

**Share it with the world! 🌍** 