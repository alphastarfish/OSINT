#!/bin/bash
# VIBE Core Dashboard Startup Script
echo "🧠 Starting VIBE Core Dashboard..."
cd "$(dirname "$0")"
python3 vibe_core_dashboard.py
