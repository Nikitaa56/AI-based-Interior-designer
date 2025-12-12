# 🔑 Get Your FREE Replicate API Token (2 Minutes)

## Why You Need This:

**Current:** Filters applied to your image (same room, different colors)  
**With API Token:** AI generates completely NEW room designs! 🎨

---

## 📝 Step-by-Step Instructions:

### **Step 1: Sign Up (1 minute)**

1. Click this link: **https://replicate.com/signin?next=/account/api-tokens**
2. Click "Sign up with GitHub" or "Sign up with Google"
3. That's it - you're signed up!

### **Step 2: Copy Your Token (30 seconds)**

1. You'll see a page with your API token
2. It looks like: `r8_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
3. Click the "Copy" button

### **Step 3: Add Token to App (30 seconds)**

**Option A - Paste it here:**

I'll create a simple command for you. Just replace `YOUR_TOKEN_HERE` with your actual token:

```bash
echo "REPLICATE_API_TOKEN=YOUR_TOKEN_HERE" > backend/.env
```

**Option B - Use the script:**

```bash
cd backend
./add_token.sh
```

Then paste your token when asked.

### **Step 4: Restart Backend (10 seconds)**

```bash
pkill -f "python.*server.py"
cd backend
source venv/bin/activate
nohup python3 server.py > ../backend_server.log 2>&1 &
```

---

## 🎉 What You'll Get:

### **Before (Current - Filters Only):**
- ❌ Same room, just different colors
- ❌ Same furniture
- ❌ Same layout
- ❌ Just brightness/contrast changes

### **After (With API Token - Real AI):**
- ✅ **Completely redesigned rooms**
- ✅ **New furniture generated**
- ✅ **Different layouts**
- ✅ **Professional AI interior design**
- ✅ **10-20 second generation**

---

## 💰 Pricing:

- **FREE:** 50 images per month
- **After that:** ~$0.02 per image (2 cents)
- **No credit card required** for free tier

---

## 🚀 Quick Copy-Paste:

Once you have your token, run this (replace `r8_YOUR_TOKEN` with your real token):

```bash
cd "/Users/nikitachoudhary/Desktop/AI-Interior-Designer copy/backend"
echo "REPLICATE_API_TOKEN=r8_YOUR_TOKEN" > .env
pkill -f "python.*server.py"
source venv/bin/activate
nohup python3 server.py > ../backend_server.log 2>&1 &
echo "✅ Backend restarted with API token!"
```

---

## ❓ Need Help?

Just tell me:
1. "I got my token" - and paste it (I'll add it for you)
2. "I'm stuck at step X" - and I'll help

---

## 🎯 Bottom Line:

**2 minutes of setup = Real AI room redesigns instead of just filters!**

Ready? Go to: **https://replicate.com/signin?next=/account/api-tokens**

