#!/bin/bash

echo "🔑 Add Your Replicate API Token"
echo "================================"
echo ""
echo "I just opened the Replicate signup page in your browser."
echo ""
echo "Steps:"
echo "  1. Sign up at Replicate (it's FREE!)"
echo "  2. Copy your API token (starts with 'r8_...')"
echo "  3. Paste it below"
echo ""
echo -n "Enter your Replicate API token: "
read API_TOKEN

if [ -z "$API_TOKEN" ]; then
    echo ""
    echo "❌ No token provided."
    echo ""
    echo "To add it manually, run:"
    echo "  echo 'REPLICATE_API_TOKEN=your_token_here' > backend/.env"
    exit 1
fi

# Save to .env file
echo "REPLICATE_API_TOKEN=$API_TOKEN" > .env

echo ""
echo "✅ Token saved successfully!"
echo ""
echo "Now restart the backend:"
echo "  pkill -f 'python.*server.py'"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  python3 server.py"
echo ""

