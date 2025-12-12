#!/bin/bash

echo "🚀 Vercel Deployment Script for AI Interior Designer"
echo "===================================================="
echo ""
echo "This script will help you deploy your app to Vercel."
echo ""

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "📦 Vercel CLI not found. Installing..."
    npm install -g vercel
    
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install Vercel CLI."
        echo "Please install it manually: npm install -g vercel"
        exit 1
    fi
fi

echo "✅ Vercel CLI is ready!"
echo ""
echo "📋 Deployment Steps:"
echo ""
echo "IMPORTANT: This app has two parts:"
echo "  1. Frontend (React) - Will be deployed to Vercel"
echo "  2. Backend (Flask/Python) - Needs separate deployment"
echo ""
echo "For the backend, you'll need to use:"
echo "  - Render.com (recommended for Python)"
echo "  - Railway.app"
echo "  - Heroku"
echo ""
read -p "Press Enter to deploy the FRONTEND to Vercel..."

cd frontend

echo ""
echo "🔐 You'll need to login to Vercel..."
vercel login

echo ""
echo "🚀 Deploying frontend..."
vercel --prod

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Frontend deployed successfully!"
    echo ""
    echo "⚠️  NEXT STEPS:"
    echo "1. Deploy the backend using: ./deploy_backend_to_render.sh"
    echo "2. Update the frontend API URL to point to your backend"
    echo "3. Add your REPLICATE_API_TOKEN to the backend environment variables"
else
    echo ""
    echo "❌ Deployment failed. Please check the errors above."
    exit 1
fi

