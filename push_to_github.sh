#!/bin/bash

echo "🚀 GitHub Push Script for AI Interior Designer"
echo "=============================================="
echo ""
echo "This script will help you push your code to GitHub."
echo ""
echo "⚠️  IMPORTANT: You need to authenticate with GitHub first!"
echo ""
echo "Choose your authentication method:"
echo ""
echo "1. Using Personal Access Token (Recommended)"
echo "   - Go to: https://github.com/settings/tokens"
echo "   - Click 'Generate new token (classic)'"
echo "   - Give it a name like 'AI Interior Designer'"
echo "   - Select scope: 'repo' (full control of private repositories)"
echo "   - Click 'Generate token'"
echo "   - Copy the token (you won't see it again!)"
echo ""
echo "2. Using SSH (if you have SSH keys set up)"
echo ""
read -p "Enter 1 for Token or 2 for SSH: " auth_method

if [ "$auth_method" == "1" ]; then
    echo ""
    read -p "Enter your GitHub Personal Access Token: " token
    echo ""
    echo "📤 Pushing to GitHub using token..."
    git push https://${token}@github.com/Nikitaa56/AI-based-Interior-designer.git main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Successfully pushed to GitHub!"
        echo "🌐 View your repository at: https://github.com/Nikitaa56/AI-based-Interior-designer"
    else
        echo ""
        echo "❌ Push failed. Please check your token and try again."
        exit 1
    fi
    
elif [ "$auth_method" == "2" ]; then
    echo ""
    echo "📤 Switching to SSH and pushing..."
    git remote set-url origin git@github.com:Nikitaa56/AI-based-Interior-designer.git
    git push -u origin main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Successfully pushed to GitHub!"
        echo "🌐 View your repository at: https://github.com/Nikitaa56/AI-based-Interior-designer"
    else
        echo ""
        echo "❌ Push failed. Make sure your SSH keys are set up correctly."
        echo "   Run: ssh -T git@github.com to test your SSH connection"
        exit 1
    fi
else
    echo "Invalid option. Please run the script again and choose 1 or 2."
    exit 1
fi

echo ""
echo "🎉 Next Steps:"
echo "1. Visit your repository: https://github.com/Nikitaa56/AI-based-Interior-designer"
echo "2. Run the deployment script: ./deploy_to_vercel.sh"
echo ""

