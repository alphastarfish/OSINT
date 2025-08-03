#!/usr/bin/env python3
"""
🧠 TYLER FRAMEWORK DEMO
TYLER Force Multiplier Framework - Simplified Demo

Classification: DEMONSTRATION SYSTEM
Version: 1.0
Node: SIGMA COMMAND
"""

import json
import time
import sqlite3
import threading
import random
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import os

# ANSI color codes for terminal output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_banner():
    """Display TYLER banner"""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
    ████████╗██╗   ██╗██╗     ███████╗██████╗ 
    ╚══██╔══╝╚██╗ ██╔╝██║     ██╔════╝██╔══██╗
       ██║    ╚████╔╝ ██║     █████╗  ██████╔╝
       ██║     ╚██╔╝  ██║     ██╔══╝  ██╔══██╗
       ██║      ██║   ███████╗███████╗██║  ██║
       ╚═╝      ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
{Colors.END}
{Colors.BOLD}🧠 TYLER FORCE MULTIPLIER FRAMEWORK 🧠{Colors.END}
{Colors.YELLOW}    "Precision multiplies power. Structure wins wars."{Colors.END}

{Colors.GREEN}🔒 Classification: DEMONSTRATION SYSTEM{Colors.END}
{Colors.GREEN}🎯 Version: 1.0{Colors.END}
{Colors.GREEN}📡 Node: SIGMA COMMAND{Colors.END}

{Colors.CYAN}═══════════════════════════════════════════════════════{Colors.END}
"""
    print(banner)

class TYLERDemo:
    """Simplified TYLER framework demonstration"""
    
    def __init__(self):
        self.threat_levels = ["LOW", "MEDIUM", "HIGH", "CRITICAL", "IMMINENT"]
        self.threat_types = ["malware", "phishing", "apt", "ransomware", "ddos", "insider"]
        self.sources = ["SIGMA-GHOST-01", "SPECTER-ALPHA", "VIBE-GRID", "NODELINK-HUB"]
        self.operators = ["PHANTOM_RECON", "CYBER_SENTINEL", "DIGITAL_GUARDIAN", "THREAT_HUNTER"]
        
        self.active_threats = []
        self.operator_status = {}
        self.ooda_metrics = {"observe": 0.1, "orient": 0.2, "decide": 0.3, "act": 0.4, "total": 1.0}
        self.system_status = "OPERATIONAL"
        
        self.initialize_demo_data()
    
    def initialize_demo_data(self):
        """Initialize demo data"""
        # Create some sample threats
        for i in range(5):
            threat = {
                "id": f"THREAT-{i+1:03d}",
                "timestamp": datetime.now().isoformat(),
                "source": random.choice(self.sources),
                "threat_type": random.choice(self.threat_types),
                "threat_level": random.choice(self.threat_levels),
                "confidence": round(random.uniform(0.6, 0.95), 2),
                "description": f"Suspicious {random.choice(self.threat_types)} activity detected",
                "status": "ACTIVE" if i < 3 else "RESOLVED"
            }
            self.active_threats.append(threat)
        
        # Initialize operator status
        for operator in self.operators:
            self.operator_status[operator] = {
                "status": random.choice(["ACTIVE", "MONITORING", "STANDBY"]),
                "location": f"SECTOR-{random.randint(1, 9)}",
                "last_heartbeat": datetime.now().isoformat(),
                "mission": f"INTEL-COLLECTION-{random.randint(1, 10)}"
            }
    
    def generate_threat_update(self):
        """Generate a new threat for demonstration"""
        threat = {
            "id": f"THREAT-{len(self.active_threats)+1:03d}",
            "timestamp": datetime.now().isoformat(),
            "source": random.choice(self.sources),
            "threat_type": random.choice(self.threat_types),
            "threat_level": random.choice(self.threat_levels),
            "confidence": round(random.uniform(0.6, 0.95), 2),
            "description": f"New {random.choice(self.threat_types)} threat detected",
            "status": "ACTIVE"
        }
        self.active_threats.append(threat)
        
        # Update OODA metrics
        self.ooda_metrics = {
            "observe": round(random.uniform(0.05, 0.2), 3),
            "orient": round(random.uniform(0.1, 0.3), 3),
            "decide": round(random.uniform(0.2, 0.4), 3),
            "act": round(random.uniform(0.3, 0.6), 3),
            "total": 0
        }
        self.ooda_metrics["total"] = round(sum(self.ooda_metrics.values()) - self.ooda_metrics["total"], 3)
        
        return threat
    
    def get_dashboard_data(self):
        """Get current dashboard data"""
        active_threats = [t for t in self.active_threats if t["status"] == "ACTIVE"]
        critical_threats = [t for t in active_threats if t["threat_level"] in ["HIGH", "CRITICAL", "IMMINENT"]]
        
        return {
            "system_status": self.system_status,
            "total_threats": len(self.active_threats),
            "active_threats": len(active_threats),
            "critical_threats": len(critical_threats),
            "active_operators": len([o for o in self.operator_status.values() if o["status"] == "ACTIVE"]),
            "ooda_metrics": self.ooda_metrics,
            "recent_threats": self.active_threats[-5:],
            "operator_status": self.operator_status,
            "timestamp": datetime.now().isoformat()
        }

class TYLERHTTPHandler(BaseHTTPRequestHandler):
    """HTTP handler for TYLER demo web interface"""
    
    def __init__(self, tyler_demo, *args, **kwargs):
        self.tyler_demo = tyler_demo
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.serve_dashboard()
        elif self.path == '/api/status':
            self.serve_api_status()
        elif self.path == '/api/threats':
            self.serve_api_threats()
        elif self.path == '/generate_threat':
            self.generate_new_threat()
        else:
            self.send_error(404)
    
    def serve_dashboard(self):
        """Serve main dashboard"""
        dashboard_html = self.get_dashboard_html()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(dashboard_html.encode())
    
    def serve_api_status(self):
        """Serve API status"""
        data = self.tyler_demo.get_dashboard_data()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())
    
    def serve_api_threats(self):
        """Serve threats API"""
        threats = self.tyler_demo.active_threats
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(threats, indent=2).encode())
    
    def generate_new_threat(self):
        """Generate new threat for demo"""
        new_threat = self.tyler_demo.generate_threat_update()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(new_threat, indent=2).encode())
    
    def get_dashboard_html(self):
        """Generate dashboard HTML"""
        data = self.tyler_demo.get_dashboard_data()
        
        return f"""
<!DOCTYPE html>
<html>
<head>
    <title>🧠 TYLER Force Multiplier Framework</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
            background: #0a0a0a;
            color: #00ff00;
            font-family: 'Courier New', monospace;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            text-align: center;
            border: 2px solid #00ff00;
            padding: 20px;
            margin-bottom: 20px;
            background: linear-gradient(45deg, #001100, #003300);
        }}
        .title {{
            font-size: 24px;
            font-weight: bold;
            color: #00ffff;
            text-shadow: 0 0 10px #00ffff;
        }}
        .subtitle {{
            color: #ffff00;
            margin-top: 10px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}
        .panel {{
            border: 1px solid #00ff00;
            padding: 15px;
            background: #001100;
            border-radius: 5px;
        }}
        .panel h3 {{
            color: #00ffff;
            margin-top: 0;
            border-bottom: 1px solid #00ffff;
            padding-bottom: 5px;
        }}
        .metric {{
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
        }}
        .metric-value {{
            color: #ffff00;
            font-weight: bold;
        }}
        .threat-item {{
            border-left: 3px solid #ff0000;
            padding: 10px;
            margin: 10px 0;
            background: #220000;
        }}
        .threat-high {{
            border-left-color: #ff0000;
        }}
        .threat-medium {{
            border-left-color: #ffaa00;
        }}
        .threat-low {{
            border-left-color: #00ff00;
        }}
        .operator {{
            display: flex;
            justify-content: space-between;
            padding: 5px 0;
            border-bottom: 1px dotted #333;
        }}
        .status-operational {{
            color: #00ff00;
        }}
        .status-warning {{
            color: #ffaa00;
        }}
        .status-critical {{
            color: #ff0000;
        }}
        .button {{
            background: #003300;
            border: 1px solid #00ff00;
            color: #00ff00;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 3px;
            text-decoration: none;
            display: inline-block;
            margin: 5px;
        }}
        .button:hover {{
            background: #005500;
        }}
        .timestamp {{
            color: #888;
            font-size: 12px;
        }}
    </style>
    <script>
        function refreshData() {{
            fetch('/api/status')
                .then(response => response.json())
                .then(data => {{
                    document.getElementById('timestamp').innerHTML = 'Last Update: ' + data.timestamp;
                    // Update metrics
                    document.getElementById('system-status').innerHTML = data.system_status;
                    document.getElementById('active-threats').innerHTML = data.active_threats;
                    document.getElementById('critical-threats').innerHTML = data.critical_threats;
                    document.getElementById('active-operators').innerHTML = data.active_operators;
                    document.getElementById('ooda-total').innerHTML = data.ooda_metrics.total + 's';
                }});
        }}
        
        function generateThreat() {{
            fetch('/generate_threat')
                .then(response => response.json())
                .then(data => {{
                    console.log('New threat generated:', data);
                    setTimeout(refreshData, 1000);
                }});
        }}
        
        // Auto-refresh every 5 seconds
        setInterval(refreshData, 5000);
    </script>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="title">🧠 TYLER FORCE MULTIPLIER FRAMEWORK</div>
            <div class="subtitle">"Precision multiplies power. Structure wins wars."</div>
            <div class="timestamp" id="timestamp">Last Update: {data['timestamp']}</div>
        </div>
        
        <div class="grid">
            <div class="panel">
                <h3>🎯 System Status</h3>
                <div class="metric">
                    <span>System Status:</span>
                    <span class="metric-value status-operational" id="system-status">{data['system_status']}</span>
                </div>
                <div class="metric">
                    <span>Active Threats:</span>
                    <span class="metric-value" id="active-threats">{data['active_threats']}</span>
                </div>
                <div class="metric">
                    <span>Critical Threats:</span>
                    <span class="metric-value" id="critical-threats">{data['critical_threats']}</span>
                </div>
                <div class="metric">
                    <span>Active Operators:</span>
                    <span class="metric-value" id="active-operators">{data['active_operators']}</span>
                </div>
            </div>
            
            <div class="panel">
                <h3>⚛️ OODA Loop Metrics</h3>
                <div class="metric">
                    <span>Observe:</span>
                    <span class="metric-value">{data['ooda_metrics']['observe']}s</span>
                </div>
                <div class="metric">
                    <span>Orient:</span>
                    <span class="metric-value">{data['ooda_metrics']['orient']}s</span>
                </div>
                <div class="metric">
                    <span>Decide:</span>
                    <span class="metric-value">{data['ooda_metrics']['decide']}s</span>
                </div>
                <div class="metric">
                    <span>Act:</span>
                    <span class="metric-value">{data['ooda_metrics']['act']}s</span>
                </div>
                <div class="metric">
                    <span><strong>Total OODA:</strong></span>
                    <span class="metric-value" id="ooda-total"><strong>{data['ooda_metrics']['total']}s</strong></span>
                </div>
            </div>
        </div>
        
        <div class="grid">
            <div class="panel">
                <h3>🚨 Recent Threats</h3>
                {self.format_threats(data['recent_threats'])}
                <button class="button" onclick="generateThreat()">🎯 Generate New Threat</button>
            </div>
            
            <div class="panel">
                <h3>👥 Operator Status</h3>
                {self.format_operators(data['operator_status'])}
            </div>
        </div>
        
        <div class="panel">
            <h3>📊 API Endpoints</h3>
            <a href="/api/status" class="button">📊 System Status</a>
            <a href="/api/threats" class="button">🚨 Threat Data</a>
            <a href="/generate_threat" class="button">🎯 Generate Threat</a>
        </div>
    </div>
</body>
</html>
        """
    
    def format_threats(self, threats):
        """Format threats for HTML display"""
        html = ""
        for threat in threats:
            level_class = f"threat-{threat['threat_level'].lower()}"
            html += f"""
            <div class="threat-item {level_class}">
                <strong>{threat['id']}</strong> - {threat['threat_type'].upper()}<br>
                <span>Level: {threat['threat_level']} | Confidence: {threat['confidence']}</span><br>
                <span class="timestamp">{threat['timestamp']}</span>
            </div>
            """
        return html
    
    def format_operators(self, operators):
        """Format operators for HTML display"""
        html = ""
        for name, status in operators.items():
            html += f"""
            <div class="operator">
                <span>{name}</span>
                <span class="metric-value">{status['status']}</span>
            </div>
            """
        return html
    
    def log_message(self, format, *args):
        """Suppress log messages"""
        pass

def create_handler(tyler_demo):
    """Create HTTP handler with TYLER demo instance"""
    def handler(*args, **kwargs):
        TYLERHTTPHandler(tyler_demo, *args, **kwargs)
    return handler

def main():
    """Main function to run TYLER demo"""
    print_banner()
    
    print(f"{Colors.CYAN}🚀 Initializing TYLER demonstration...{Colors.END}")
    
    # Initialize TYLER demo
    tyler_demo = TYLERDemo()
    
    # Create HTTP server
    port = 8050
    handler = create_handler(tyler_demo)
    
    try:
        server = HTTPServer(('localhost', port), handler)
        
        print(f"{Colors.GREEN}✅ TYLER Demo Server initialized{Colors.END}")
        print(f"{Colors.CYAN}📡 Dashboard available at: http://localhost:{port}{Colors.END}")
        print(f"{Colors.CYAN}📊 API endpoints: http://localhost:{port}/api/status{Colors.END}")
        print(f"{Colors.YELLOW}🎯 Click 'Generate New Threat' to see OODA loop in action{Colors.END}")
        print(f"{Colors.CYAN}═══════════════════════════════════════════════════════{Colors.END}")
        print(f"{Colors.BOLD}Press Ctrl+C to stop the server{Colors.END}")
        
        # Start background threat generation
        def background_threat_gen():
            while True:
                time.sleep(30 + random.randint(10, 50))  # Random interval
                tyler_demo.generate_threat_update()
                print(f"{Colors.YELLOW}🚨 New threat detected - Dashboard updated{Colors.END}")
        
        threat_thread = threading.Thread(target=background_threat_gen, daemon=True)
        threat_thread.start()
        
        # Start server
        server.serve_forever()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}🛑 TYLER Demo shutting down...{Colors.END}")
        server.shutdown()
        print(f"{Colors.GREEN}✅ Shutdown complete. Stay vigilant, Operator.{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.END}")

if __name__ == "__main__":
    main()