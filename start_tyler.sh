#!/bin/bash
# Complete TYLER Framework Startup Script
echo "🧠 Starting TYLER Force Multiplier Framework..."
cd "$(dirname "$0")"

echo "🔗 Starting NodeLink Hub..."
python3 nodelink_secure_comms.py &
NODELINK_PID=$!

sleep 5

echo "🧠 Starting VIBE Core Dashboard..."
python3 vibe_core_dashboard.py &
VIBE_PID=$!

echo "✅ TYLER Framework started successfully"
echo "📡 VIBE Dashboard: http://127.0.0.1:8050"
echo "🔗 NodeLink Hub: http://127.0.0.1:8443"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for interrupt
trap 'echo "Stopping TYLER services..."; kill $NODELINK_PID $VIBE_PID; exit 0' INT
wait
