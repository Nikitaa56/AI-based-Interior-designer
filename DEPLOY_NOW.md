# 🚀 Quick Deploy - AI Interior Designer

## Step 1: Push to GitHub (5 minutes)

```bash
./push_to_github.sh
```

You'll need a GitHub Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name: "AI Interior Designer"
4. Select: ✅ repo (full control)
5. Generate and copy the token
6. Paste it when the script asks

## Step 2: Deploy Backend to Render (10 minutes)

### A. Create Render Account
1. Go to https://render.com
2. Sign up with GitHub

### B. Create Web Service
1. Click "New +" → "Web Service"
2. Connect repository: `Nikitaa56/AI-based-Interior-designer`
3. Settings:
   - **Name**: `ai-interior-backend`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:app`
   - **Instance Type**: Free

### C. Add Environment Variable
1. Go to "Environment" tab
2. Add variable:
   - **Key**: `REPLICATE_API_TOKEN`
   - **Value**: Your Replicate API token (from backend/.env)

3. Click "Create Web Service"

### D. Copy Backend URL
After deployment, copy your URL (e.g., `https://ai-interior-backend.onrender.com`)

## Step 3: Update Frontend API URL (2 minutes)

Edit `frontend/src/App.js`:

Find this line (around line 10):
```javascript
const API_URL = 'http://localhost:5001';
```

Replace with:
```javascript
const API_URL = 'https://ai-interior-backend.onrender.com';
```
(Use YOUR actual Render URL)

Save the file.

## Step 4: Commit and Push Changes (1 minute)

```bash
git add frontend/src/App.js
git commit -m "Update API URL for production"
git push origin main
```

## Step 5: Deploy Frontend to Vercel (5 minutes)

```bash
./deploy_to_vercel.sh
```

Or manually:
```bash
cd frontend
npm install -g vercel
vercel login
vercel --prod
```

## 🎉 Done! Your App is Live!

- **Frontend**: Check Vercel dashboard for URL
- **Backend**: Your Render URL

## 🧪 Test Your Live App

1. Open your Vercel URL
2. Upload a room image
3. Enter a style prompt
4. Click "Redesign Room"
5. Wait ~30 seconds for AI generation

## ⚠️ Important Notes

1. **First Request**: Render free tier sleeps after inactivity. First request may take 30-60 seconds.

2. **API Costs**: Each generation uses Replicate API credits. Monitor at https://replicate.com/account

3. **Logs**: 
   - Backend logs: Render dashboard → Logs
   - Frontend logs: Vercel dashboard → Deployments → View logs

## 🐛 Troubleshooting

**Backend not responding?**
- Check Render logs for errors
- Verify REPLICATE_API_TOKEN is set correctly

**CORS errors?**
- Make sure Flask-CORS is installed (it's in requirements.txt)
- Check backend logs

**Frontend can't connect to backend?**
- Verify API_URL in App.js matches your Render URL
- Make sure backend is deployed and running

## 📞 Need Help?

Check the full guide: `DEPLOYMENT_GUIDE.md`

