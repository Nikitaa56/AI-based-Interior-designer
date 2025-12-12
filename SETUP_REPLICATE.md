# 🚀 Quick Setup Guide - Replicate API

Your AI Interior Designer now uses **Replicate API** for fast, high-quality image generation!

## ✨ Benefits
- ⚡ **10-20 seconds** per image (vs 5-10 minutes on CPU)
- 🎨 **High quality** professional results
- 💰 **Free tier** available (50 free predictions/month)
- 🚫 **No GPU needed** - runs in the cloud

---

## 📝 Setup Steps (5 minutes)

### 1. Get Your FREE Replicate API Token

1. Go to: **https://replicate.com/account/api-tokens**
2. Sign up (free account)
3. Copy your API token (starts with `r8_...`)

### 2. Configure the API Token

**Option A: Use the setup script (easiest)**
```bash
cd backend
./setup_api.sh
```

**Option B: Manual setup**
```bash
cd backend
echo "REPLICATE_API_TOKEN=your_token_here" > .env
```

Replace `your_token_here` with your actual token from step 1.

### 3. Restart the Backend

```bash
# Stop the old backend
pkill -f "python.*server.py"

# Start the new backend
cd backend
source venv/bin/activate
python3 server.py
```

### 4. Test It!

1. Open http://localhost:3000
2. Upload a room image
3. Enter a prompt like: "modern luxury bedroom with minimalist design"
4. Click "Generate Design"
5. Wait 10-20 seconds ⚡

---

## 💰 Pricing

- **Free Tier**: 50 predictions/month
- **Pay-as-you-go**: ~$0.01-0.03 per image
- More info: https://replicate.com/pricing

---

## 🔧 Troubleshooting

### "REPLICATE_API_TOKEN not configured" error
- Make sure you created the `.env` file in the `backend/` folder
- Check that your token is correct (starts with `r8_`)
- Restart the backend server

### Still slow?
- Check your internet connection
- Replicate API runs in the cloud, so it needs good internet

### Image quality issues?
- Try more descriptive prompts
- Add style keywords: "photorealistic", "professional", "8k", "detailed"

---

## 🎉 You're All Set!

Enjoy fast, high-quality AI interior design generation! 🏠✨

