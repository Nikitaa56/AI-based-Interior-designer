#!/bin/bash

# Kill any existing processes
pkill -f "react-scripts" 2>/dev/null
pkill -f "python.*server.py" 2>/dev/null
sleep 2

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "🚀 Starting AI Interior Designer..."
echo ""

# Start backend
echo "📦 Starting Backend Server..."
cd "$SCRIPT_DIR/backend"
source venv/bin/activate
nohup python3 server.py > ../backend.log 2>&1 &
BACKEND_PID=$!
echo "✅ Backend started (PID: $BACKEND_PID)"
echo ""

# Wait for backend to initialize
sleep 5

# Start frontend
echo "🎨 Starting Frontend Server..."
cd "$SCRIPT_DIR/frontend"
nohup npm start > ../frontend.log 2>&1 &
FRONTEND_PID=$!
echo "✅ Frontend started (PID: $FRONTEND_PID)"
echo ""

# Wait for frontend to compile
echo "⏳ Waiting for frontend to compile..."
sleep 15

echo ""
echo "✨ Application is ready!"
echo ""
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend:  http://127.0.0.1:5000"
echo ""
echo "📝 Logs:"
echo "   Backend:  $SCRIPT_DIR/backend.log"
echo "   Frontend: $SCRIPT_DIR/frontend.log"
echo ""
echo "🛑 To stop the servers, run:"
echo "   kill $BACKEND_PID $FRONTEND_PID"
echo ""

# Open browser
sleep 2
open http://localhost:3000 2>/dev/null || echo "Please open http://localhost:3000 in your browser"

