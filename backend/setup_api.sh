#!/bin/bash

echo "🚀 AI Interior Designer - Replicate API Setup"
echo "=============================================="
echo ""
echo "To use this app, you need a FREE Replicate API token."
echo ""
echo "📝 Steps to get your API token:"
echo "   1. Go to: https://replicate.com/account/api-tokens"
echo "   2. Sign up (it's free!)"
echo "   3. Copy your API token"
echo ""
echo -n "Enter your Replicate API token: "
read API_TOKEN

if [ -z "$API_TOKEN" ]; then
    echo "❌ No token provided. Exiting."
    exit 1
fi

# Create .env file
echo "REPLICATE_API_TOKEN=$API_TOKEN" > .env

echo ""
echo "✅ API token saved to .env file!"
echo ""
echo "🎉 Setup complete! Now run:"
echo "   python3 server.py"
echo ""

