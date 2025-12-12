# 🚀 Deployment Guide - AI Interior Designer

This guide will help you deploy your AI Interior Designer app and make it live on the internet.

## 📋 Overview

Your app has two parts:
1. **Frontend** (React) - User interface
2. **Backend** (Flask/Python) - AI processing with Replicate API

## Step 1: Push to GitHub ✅

Run the push script:
```bash
chmod +x push_to_github.sh
./push_to_github.sh
```

Follow the prompts to authenticate and push your code.

## Step 2: Deploy Backend (Python/Flask)

### Option A: Deploy to Render.com (Recommended - Free Tier Available)

1. **Go to [Render.com](https://render.com)** and sign up/login

2. **Create a new Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `Nikitaa56/AI-based-Interior-designer`
   - Configure:
     - **Name**: `ai-interior-designer-backend`
     - **Root Directory**: `backend`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn server:app`

3. **Add Environment Variables**
   - Go to "Environment" tab
   - Add: `REPLICATE_API_TOKEN` = `your_replicate_token_here`

4. **Deploy** - Click "Create Web Service"

5. **Copy your backend URL** (e.g., `https://ai-interior-designer-backend.onrender.com`)

### Option B: Deploy to Railway.app

1. Go to [Railway.app](https://railway.app)
2. Click "Start a New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add environment variable: `REPLICATE_API_TOKEN`
5. Railway will auto-detect Python and deploy

## Step 3: Deploy Frontend (React)

### Deploy to Vercel (Recommended)

1. **Run the deployment script**:
```bash
chmod +x deploy_to_vercel.sh
./deploy_to_vercel.sh
```

2. **Or manually**:
```bash
cd frontend
npm install -g vercel
vercel login
vercel --prod
```

3. **Update API URL**:
   - After backend is deployed, update `frontend/src/App.js`
   - Change the API URL from `http://localhost:5001` to your Render backend URL
   - Redeploy: `vercel --prod`

### Alternative: Deploy to Netlify

1. Go to [Netlify.com](https://netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect GitHub and select your repository
4. Configure:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/build`
5. Deploy!

## Step 4: Configure Environment Variables

### Backend Environment Variables (Render/Railway)
```
REPLICATE_API_TOKEN=your_token_here
PORT=5000
```

### Frontend Environment Variables (Vercel/Netlify)
Create `frontend/.env.production`:
```
REACT_APP_API_URL=https://your-backend-url.onrender.com
```

## Step 5: Update Frontend to Use Production Backend

Edit `frontend/src/App.js` and update the API endpoint:

```javascript
// Change from:
const API_URL = 'http://localhost:5001';

// To:
const API_URL = process.env.REACT_APP_API_URL || 'https://your-backend-url.onrender.com';
```

## 🎉 Your App is Live!

After deployment:
- **Frontend**: `https://your-app.vercel.app`
- **Backend**: `https://your-backend.onrender.com`

## 📝 Important Notes

1. **Free Tier Limitations**:
   - Render free tier: Backend may sleep after inactivity (takes ~30s to wake up)
   - Vercel: Generous free tier for frontend

2. **API Costs**:
   - Replicate API charges per generation
   - Monitor your usage at [replicate.com/account](https://replicate.com/account)

3. **Custom Domain** (Optional):
   - Both Vercel and Render support custom domains
   - Configure in their respective dashboards

## 🐛 Troubleshooting

- **CORS errors**: Make sure backend has Flask-CORS configured
- **API not responding**: Check backend logs on Render/Railway
- **Build fails**: Check Node/Python versions match your local setup

## 📞 Need Help?

- Render Docs: https://render.com/docs
- Vercel Docs: https://vercel.com/docs
- Railway Docs: https://docs.railway.app

