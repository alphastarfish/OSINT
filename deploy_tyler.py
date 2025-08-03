#!/usr/bin/env python3
"""
🚀 TYLER FRAMEWORK DEPLOYMENT SCRIPT
TYLER Force Multiplier Framework - Automated Setup & Deployment

Classification: DEPLOYMENT SYSTEM
Version: 1.0
Node: SIGMA COMMAND
"""

import os
import sys
import subprocess
import json
import sqlite3
import secrets
import time
from pathlib import Path
from datetime import datetime
import argparse
import logging

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
    """Display TYLER deployment banner"""
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

{Colors.GREEN}🔒 Classification: OPERATIONAL DEPLOYMENT{Colors.END}
{Colors.GREEN}🎯 Version: 1.0{Colors.END}
{Colors.GREEN}📡 Node: SIGMA COMMAND{Colors.END}

{Colors.CYAN}═══════════════════════════════════════════════════════{Colors.END}
"""
    print(banner)

def check_python_version():
    """Verify Python version compatibility"""
    required_version = (3, 8)
    current_version = sys.version_info[:2]
    
    if current_version < required_version:
        print(f"{Colors.RED}❌ Python {required_version[0]}.{required_version[1]}+ required. Current: {current_version[0]}.{current_version[1]}{Colors.END}")
        sys.exit(1)
    
    print(f"{Colors.GREEN}✅ Python version {current_version[0]}.{current_version[1]} compatible{Colors.END}")

def install_dependencies():
    """Install required Python packages"""
    print(f"{Colors.CYAN}📦 Installing TYLER framework dependencies...{Colors.END}")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--upgrade"
        ])
        print(f"{Colors.GREEN}✅ Dependencies installed successfully{Colors.END}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}❌ Failed to install dependencies: {e}{Colors.END}")
        sys.exit(1)

def create_directory_structure():
    """Create required directory structure"""
    print(f"{Colors.CYAN}📁 Creating directory structure...{Colors.END}")
    
    directories = [
        "data",
        "logs", 
        "config",
        "ssl_certs",
        "backups",
        "temp",
        "exports",
        "intelligence",
        "missions",
        "operators",
        "tools"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"  📁 {directory}/")
    
    print(f"{Colors.GREEN}✅ Directory structure created{Colors.END}")

def generate_ssl_certificates():
    """Generate self-signed SSL certificates for development"""
    print(f"{Colors.CYAN}🔐 Generating SSL certificates...{Colors.END}")
    
    cert_dir = Path("ssl_certs")
    cert_path = cert_dir / "tyler.crt"
    key_path = cert_dir / "tyler.key"
    
    if cert_path.exists() and key_path.exists():
        print(f"{Colors.YELLOW}⚠️  SSL certificates already exist, skipping generation{Colors.END}")
        return
    
    try:
        # Generate private key
        subprocess.check_call([
            "openssl", "genrsa", "-out", str(key_path), "2048"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Generate certificate
        subprocess.check_call([
            "openssl", "req", "-new", "-x509", "-key", str(key_path),
            "-out", str(cert_path), "-days", "365", "-subj",
            "/C=US/ST=Cyber/L=Digital/O=TYLER/OU=SIGMA/CN=tyler.local"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        print(f"{Colors.GREEN}✅ SSL certificates generated{Colors.END}")
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"{Colors.YELLOW}⚠️  OpenSSL not found, skipping SSL certificate generation{Colors.END}")
        print(f"{Colors.YELLOW}   For production deployment, manually generate certificates{Colors.END}")

def initialize_databases():
    """Initialize SQLite databases for TYLER components"""
    print(f"{Colors.CYAN}🗄️  Initializing databases...{Colors.END}")
    
    databases = {
        "data/vibe_core.db": """
            CREATE TABLE IF NOT EXISTS threat_intel (
                id TEXT PRIMARY KEY,
                timestamp TEXT,
                source TEXT,
                threat_type TEXT,
                threat_level TEXT,
                confidence REAL,
                attribution TEXT,
                description TEXT,
                raw_data TEXT
            );
            
            CREATE TABLE IF NOT EXISTS operator_nodes (
                node_id TEXT PRIMARY KEY,
                codename TEXT,
                node_type TEXT,
                status TEXT,
                location TEXT,
                capabilities TEXT,
                last_heartbeat TEXT,
                current_mission TEXT,
                threat_exposure TEXT
            );
            
            CREATE TABLE IF NOT EXISTS missions (
                mission_id TEXT PRIMARY KEY,
                codename TEXT,
                objective TEXT,
                priority INTEGER,
                assigned_nodes TEXT,
                start_time TEXT,
                estimated_completion TEXT,
                status TEXT,
                progress REAL,
                threat_indicators TEXT
            );
        """,
        
        "data/nodelink.db": """
            CREATE TABLE IF NOT EXISTS nodes (
                node_id TEXT PRIMARY KEY,
                codename TEXT,
                role TEXT,
                endpoint TEXT,
                public_key BLOB,
                last_seen TEXT,
                status TEXT,
                security_level TEXT,
                capabilities TEXT,
                trust_score REAL
            );
            
            CREATE TABLE IF NOT EXISTS messages (
                message_id TEXT PRIMARY KEY,
                sender_id TEXT,
                recipient_id TEXT,
                message_type TEXT,
                timestamp TEXT,
                processed BOOLEAN
            );
            
            CREATE TABLE IF NOT EXISTS credentials (
                node_id TEXT PRIMARY KEY,
                public_key BLOB,
                private_key BLOB,
                symmetric_key BLOB,
                signature_key BLOB,
                key_version INTEGER,
                expiry TEXT,
                security_clearance TEXT
            );
        """
    }
    
    for db_path, schema in databases.items():
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.executescript(schema)
        conn.commit()
        conn.close()
        print(f"  🗄️  {db_path}")
    
    print(f"{Colors.GREEN}✅ Databases initialized{Colors.END}")

def create_configuration_files():
    """Create configuration files for TYLER components"""
    print(f"{Colors.CYAN}⚙️  Creating configuration files...{Colors.END}")
    
    # Main TYLER configuration
    tyler_config = {
        "framework": {
            "name": "TYLER Force Multiplier Framework",
            "version": "1.0",
            "classification": "OPERATIONAL",
            "deployment_time": datetime.now().isoformat()
        },
        "security": {
            "encryption_standard": "AES-256-GCM",
            "key_rotation_interval": 3600,
            "max_session_age": 7200,
            "require_2fa": True
        },
        "components": {
            "vibe_dashboard": {
                "host": "127.0.0.1",
                "port": 8050,
                "debug": False,
                "auto_refresh": 5
            },
            "nodelink_hub": {
                "host": "0.0.0.0", 
                "port": 8443,
                "ssl_enabled": True,
                "max_connections": 1000
            },
            "ai_engine": {
                "model_type": "local",
                "decision_threshold": 0.85,
                "learning_rate": 0.001
            }
        },
        "logging": {
            "level": "INFO",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "file": "logs/tyler.log",
            "max_bytes": 10485760,
            "backup_count": 5
        }
    }
    
    # Save configuration
    with open("config/tyler.json", "w") as f:
        json.dump(tyler_config, f, indent=2)
    
    # VIBE dashboard configuration
    vibe_config = {
        "dashboard": {
            "title": "VIBE Core Dashboard",
            "theme": "cyborg",
            "auto_refresh": True,
            "refresh_interval": 5000
        },
        "data_sources": {
            "threat_intel": "data/vibe_core.db",
            "operator_nodes": "data/vibe_core.db",
            "missions": "data/vibe_core.db"
        },
        "ai_models": {
            "threat_classifier": "models/threat_classifier.pkl",
            "behavior_analyzer": "models/behavior_analyzer.pkl",
            "decision_engine": "models/decision_engine.pkl"
        }
    }
    
    with open("config/vibe.json", "w") as f:
        json.dump(vibe_config, f, indent=2)
    
    # NodeLink configuration
    nodelink_config = {
        "network": {
            "hub_id": "SIGMA-HUB-01",
            "max_nodes": 1000,
            "heartbeat_interval": 30,
            "timeout": 300
        },
        "security": {
            "encryption": "AES-256-GCM",
            "signature_algorithm": "HMAC-SHA256",
            "key_size": 32,
            "rotation_interval": 3600
        },
        "database": {
            "path": "data/nodelink.db",
            "backup_interval": 3600,
            "retention_days": 90
        }
    }
    
    with open("config/nodelink.json", "w") as f:
        json.dump(nodelink_config, f, indent=2)
    
    print(f"{Colors.GREEN}✅ Configuration files created{Colors.END}")

def generate_initial_credentials():
    """Generate initial system credentials and API keys"""
    print(f"{Colors.CYAN}🔑 Generating initial credentials...{Colors.END}")
    
    credentials = {
        "system": {
            "master_key": secrets.token_hex(32),
            "api_key": secrets.token_hex(16),
            "session_secret": secrets.token_hex(24),
            "created": datetime.now().isoformat()
        },
        "admin": {
            "username": "sigma_admin",
            "password_hash": "changeme_on_first_login",
            "security_level": "DELTA",
            "created": datetime.now().isoformat()
        }
    }
    
    # Save credentials securely
    with open("config/credentials.json", "w") as f:
        json.dump(credentials, f, indent=2)
    
    # Set secure file permissions
    os.chmod("config/credentials.json", 0o600)
    
    print(f"{Colors.GREEN}✅ Initial credentials generated{Colors.END}")
    print(f"{Colors.YELLOW}⚠️  Remember to change default passwords on first login{Colors.END}")

def setup_logging():
    """Configure logging for TYLER framework"""
    print(f"{Colors.CYAN}📝 Setting up logging...{Colors.END}")
    
    # Create log directory if it doesn't exist
    Path("logs").mkdir(exist_ok=True)
    
    # Configure main logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/tyler.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Create component-specific log files
    log_files = [
        "logs/vibe_core.log",
        "logs/nodelink.log", 
        "logs/security.log",
        "logs/operations.log"
    ]
    
    for log_file in log_files:
        Path(log_file).touch()
    
    print(f"{Colors.GREEN}✅ Logging configured{Colors.END}")

def create_startup_scripts():
    """Create startup scripts for different components"""
    print(f"{Colors.CYAN}🚀 Creating startup scripts...{Colors.END}")
    
    # VIBE Dashboard startup script
    vibe_script = """#!/bin/bash
# VIBE Core Dashboard Startup Script
echo "🧠 Starting VIBE Core Dashboard..."
cd "$(dirname "$0")"
python3 vibe_core_dashboard.py
"""
    
    with open("start_vibe.sh", "w") as f:
        f.write(vibe_script)
    os.chmod("start_vibe.sh", 0o755)
    
    # NodeLink Hub startup script
    nodelink_script = """#!/bin/bash
# NodeLink Hub Startup Script
echo "🔗 Starting NodeLink Hub..."
cd "$(dirname "$0")"
python3 nodelink_secure_comms.py
"""
    
    with open("start_nodelink.sh", "w") as f:
        f.write(nodelink_script)
    os.chmod("start_nodelink.sh", 0o755)
    
    # Complete TYLER system startup script
    tyler_script = """#!/bin/bash
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
"""
    
    with open("start_tyler.sh", "w") as f:
        f.write(tyler_script)
    os.chmod("start_tyler.sh", 0o755)
    
    print(f"{Colors.GREEN}✅ Startup scripts created{Colors.END}")

def run_system_checks():
    """Run post-deployment system checks"""
    print(f"{Colors.CYAN}🔍 Running system checks...{Colors.END}")
    
    checks = []
    
    # Check database files
    db_files = ["data/vibe_core.db", "data/nodelink.db"]
    for db_file in db_files:
        if Path(db_file).exists():
            checks.append(f"✅ Database: {db_file}")
        else:
            checks.append(f"❌ Database: {db_file}")
    
    # Check configuration files
    config_files = ["config/tyler.json", "config/vibe.json", "config/nodelink.json"]
    for config_file in config_files:
        if Path(config_file).exists():
            checks.append(f"✅ Config: {config_file}")
        else:
            checks.append(f"❌ Config: {config_file}")
    
    # Check startup scripts
    script_files = ["start_tyler.sh", "start_vibe.sh", "start_nodelink.sh"]
    for script_file in script_files:
        if Path(script_file).exists() and os.access(script_file, os.X_OK):
            checks.append(f"✅ Script: {script_file}")
        else:
            checks.append(f"❌ Script: {script_file}")
    
    # Display results
    for check in checks:
        print(f"  {check}")
    
    # Overall status
    failed_checks = [c for c in checks if c.startswith("❌")]
    if failed_checks:
        print(f"{Colors.YELLOW}⚠️  {len(failed_checks)} checks failed{Colors.END}")
    else:
        print(f"{Colors.GREEN}✅ All system checks passed{Colors.END}")

def show_deployment_summary():
    """Show deployment summary and next steps"""
    print(f"\n{Colors.CYAN}═══════════════════════════════════════════════════════{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}🎯 TYLER DEPLOYMENT COMPLETE{Colors.END}")
    print(f"{Colors.CYAN}═══════════════════════════════════════════════════════{Colors.END}")
    
    summary = f"""
{Colors.BOLD}📊 Deployment Summary:{Colors.END}
  🧠 Framework: TYLER Force Multiplier v1.0
  🔒 Classification: OPERATIONAL
  📅 Deployed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  🌍 Status: READY FOR OPERATIONS

{Colors.BOLD}🚀 Quick Start Commands:{Colors.END}
  {Colors.CYAN}./start_tyler.sh{Colors.END}        - Start complete TYLER framework
  {Colors.CYAN}./start_vibe.sh{Colors.END}         - Start VIBE dashboard only
  {Colors.CYAN}./start_nodelink.sh{Colors.END}     - Start NodeLink hub only

{Colors.BOLD}📡 Access Points:{Colors.END}
  🧠 VIBE Dashboard:  http://127.0.0.1:8050
  🔗 NodeLink Hub:    http://127.0.0.1:8443
  📊 API Endpoints:   http://127.0.0.1:8443/api/

{Colors.BOLD}📁 Key Directories:{Colors.END}
  📊 Data:       ./data/
  📝 Logs:       ./logs/
  ⚙️  Config:     ./config/
  🔐 SSL Certs:  ./ssl_certs/

{Colors.BOLD}🔒 Security Notes:{Colors.END}
  • Change default credentials in config/credentials.json
  • Generate proper SSL certificates for production
  • Configure firewall rules for NodeLink hub
  • Set up log rotation and monitoring

{Colors.BOLD}📖 Documentation:{Colors.END}
  📋 Framework:  tyler_framework_core.md
  🏛️  Charter:    tyler_charter.md
  🔗 NodeLink:   NodeLink protocol documentation
  🧠 VIBE:       Dashboard user guide

{Colors.YELLOW}⚠️  IMPORTANT SECURITY REMINDER:{Colors.END}
This deployment uses development settings. For production:
1. Generate proper SSL certificates
2. Change all default passwords
3. Configure proper firewall rules
4. Set up monitoring and alerting
5. Review and customize security settings

{Colors.BOLD}{Colors.GREEN}The digital realm awaits your command, Operator.{Colors.END}
{Colors.CYAN}"Precision multiplies power. Structure wins wars."{Colors.END}
"""
    
    print(summary)

def main():
    """Main deployment function"""
    parser = argparse.ArgumentParser(description="TYLER Framework Deployment Script")
    parser.add_argument("--skip-deps", action="store_true", help="Skip dependency installation")
    parser.add_argument("--dev-mode", action="store_true", help="Enable development mode")
    parser.add_argument("--quiet", action="store_true", help="Minimal output")
    
    args = parser.parse_args()
    
    if not args.quiet:
        print_banner()
    
    try:
        # Pre-deployment checks
        check_python_version()
        
        # Core deployment steps
        if not args.skip_deps:
            install_dependencies()
        
        create_directory_structure()
        generate_ssl_certificates()
        initialize_databases()
        create_configuration_files()
        generate_initial_credentials()
        setup_logging()
        create_startup_scripts()
        
        # Post-deployment validation
        run_system_checks()
        
        if not args.quiet:
            show_deployment_summary()
        
        print(f"{Colors.GREEN}✅ TYLER deployment completed successfully!{Colors.END}")
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️  Deployment interrupted by user{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}❌ Deployment failed: {e}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()