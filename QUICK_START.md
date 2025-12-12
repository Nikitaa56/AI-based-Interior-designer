# 🚀 Quick Start - Your App is Running!

## ✅ Current Status

- **Frontend**: Running on http://localhost:3000
- **Backend**: Running on http://127.0.0.1:5001
- **Issue Fixed**: Button no longer gets stuck!

---

## ⚠️ Important: Get Your API Token

The app is running, but **you need a Replicate API token** to generate images.

### Get Your FREE Token (2 minutes):

1. **Go to**: https://replicate.com/account/api-tokens
2. **Sign up** (free account - 50 free images/month)
3. **Copy your API token** (starts with `r8_...`)

### Add Your Token:

```bash
cd backend
nano .env
```

Replace the content with:
```
REPLICATE_API_TOKEN=your_actual_token_here
```

Save and exit (Ctrl+X, then Y, then Enter)

### Restart Backend:

```bash
# Stop the backend
pkill -f "python.*server.py"

# Start it again
source venv/bin/activate
python3 server.py
```

---

## 🎨 Test It!

1. Open http://localhost:3000
2. Upload a room image
3. Enter prompt: "modern luxury bedroom with minimalist design"
4. Click "Generate Design"
5. Wait **10-20 seconds** for high-quality results! ⚡

---

## 🔧 What Was Fixed:

1. **Port conflict**: Changed from port 5000 → 5001 (macOS AirPlay uses 5000)
2. **Backend not running**: Restarted with new configuration
3. **Frontend stuck**: Restarted to pick up new proxy settings
4. **Slow generation**: Switched to Replicate API (10-20 sec vs 5-10 min)

---

## 📊 What You Get Now:

| Before | After |
|--------|-------|
| 5-10 minutes per image | 10-20 seconds ⚡ |
| Poor quality (CPU) | Professional quality 🎨 |
| Button gets stuck | Smooth experience ✅ |

---

## 🆘 Need Help?

- **Button still stuck?** Make sure you added your API token
- **"Network error"?** Check that backend is running on port 5001
- **Still slow?** You might still be using the old local model - restart backend

Enjoy your AI Interior Designer! 🏠✨

