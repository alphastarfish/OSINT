#!/bin/bash
# NodeLink Hub Startup Script
echo "🔗 Starting NodeLink Hub..."
cd "$(dirname "$0")"
python3 nodelink_secure_comms.py
