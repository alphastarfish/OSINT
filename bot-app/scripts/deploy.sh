#!/bin/bash

# Multi-Platform Bot Deployment Script
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_NAME="multi-platform-bot"
COMPOSE_FILE="docker-compose.yml"

# Functions
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

# Check if Docker is installed
check_docker() {
    if ! command -v docker &> /dev/null; then
        error "Docker is not installed. Please install Docker first."
    fi
    
    if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
        error "Docker Compose is not installed. Please install Docker Compose first."
    fi
    
    success "Docker and Docker Compose are available"
}

# Check if .env file exists
check_env() {
    if [ ! -f ".env" ]; then
        warning ".env file not found. Creating template..."
        cat > .env << 'EOF'
# Bot Configuration
# Discord
DISCORD_TOKEN=your_discord_bot_token_here
ENABLE_DISCORD=true

# Telegram
TELEGRAM_TOKEN=your_telegram_bot_token_here
ENABLE_TELEGRAM=true

# Slack
SLACK_TOKEN=your_slack_bot_token_here
SLACK_SIGNING_SECRET=your_slack_signing_secret_here
ENABLE_SLACK=true

# General Settings
COMMAND_PREFIX=!
BOT_NAME=MultiBot
BOT_DESCRIPTION=A versatile multi-platform bot

# Admin Settings (comma-separated user IDs)
ADMIN_USERS=your_user_id_here

# Database (optional)
DATABASE_URL=sqlite:///data/bot.db
POSTGRES_PASSWORD=secure_password_here

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=text
EOF
        warning "Please edit .env file with your bot tokens before continuing!"
        exit 1
    else
        success ".env file found"
    fi
}

# Build the application
build() {
    log "Building bot application..."
    docker-compose build
    success "Build completed"
}

# Deploy the application
deploy() {
    log "Deploying bot application..."
    
    # Create necessary directories
    mkdir -p logs data
    
    # Deploy with redis (default)
    docker-compose up -d bot redis
    
    success "Bot deployed successfully!"
    log "Use 'docker-compose logs -f bot' to view logs"
}

# Deploy with PostgreSQL
deploy_with_postgres() {
    log "Deploying bot with PostgreSQL..."
    
    # Create necessary directories
    mkdir -p logs data
    
    # Deploy with postgres profile
    docker-compose --profile with-postgres up -d
    
    success "Bot deployed with PostgreSQL!"
    log "Use 'docker-compose logs -f bot' to view logs"
}

# Deploy with web interface
deploy_with_web() {
    log "Deploying bot with web interface..."
    
    # Create necessary directories
    mkdir -p logs data
    
    # Deploy with web profile
    docker-compose --profile with-web up -d
    
    success "Bot deployed with web interface!"
    log "Web interface available at http://localhost:8000"
    log "Use 'docker-compose logs -f bot' to view logs"
}

# Stop the application
stop() {
    log "Stopping bot application..."
    docker-compose down
    success "Bot stopped"
}

# View logs
logs() {
    docker-compose logs -f bot
}

# Update the application
update() {
    log "Updating bot application..."
    docker-compose down
    docker-compose pull
    docker-compose build --no-cache
    docker-compose up -d
    success "Bot updated successfully!"
}

# Clean up
cleanup() {
    log "Cleaning up..."
    docker-compose down -v
    docker system prune -f
    success "Cleanup completed"
}

# Backup data
backup() {
    log "Creating backup..."
    timestamp=$(date +%Y%m%d_%H%M%S)
    backup_dir="backups/${timestamp}"
    mkdir -p "${backup_dir}"
    
    # Backup volumes
    docker run --rm -v bot-app_bot_data:/data -v "$(pwd)/${backup_dir}:/backup" alpine tar czf /backup/bot_data.tar.gz -C /data .
    docker run --rm -v bot-app_redis_data:/data -v "$(pwd)/${backup_dir}:/backup" alpine tar czf /backup/redis_data.tar.gz -C /data .
    
    # Backup .env and logs
    cp .env "${backup_dir}/"
    cp -r logs "${backup_dir}/" 2>/dev/null || true
    
    success "Backup created in ${backup_dir}"
}

# Show usage
usage() {
    cat << EOF
Multi-Platform Bot Deployment Script

Usage: $0 [COMMAND]

Commands:
    build           Build the bot application
    deploy          Deploy the bot with Redis
    deploy-postgres Deploy the bot with PostgreSQL
    deploy-web      Deploy the bot with web interface
    stop            Stop the bot application
    logs            View bot logs
    update          Update and restart the bot
    backup          Create a backup of bot data
    cleanup         Stop and remove all containers and volumes
    help            Show this help message

Examples:
    $0 deploy                # Simple deployment
    $0 deploy-postgres       # Deploy with PostgreSQL
    $0 deploy-web           # Deploy with web interface
    $0 logs                 # View logs
    $0 stop                 # Stop the bot

EOF
}

# Main script
main() {
    case "${1:-help}" in
        "build")
            check_docker
            check_env
            build
            ;;
        "deploy")
            check_docker
            check_env
            build
            deploy
            ;;
        "deploy-postgres")
            check_docker
            check_env
            build
            deploy_with_postgres
            ;;
        "deploy-web")
            check_docker
            check_env
            build
            deploy_with_web
            ;;
        "stop")
            check_docker
            stop
            ;;
        "logs")
            check_docker
            logs
            ;;
        "update")
            check_docker
            check_env
            update
            ;;
        "backup")
            check_docker
            backup
            ;;
        "cleanup")
            check_docker
            cleanup
            ;;
        "help"|*)
            usage
            ;;
    esac
}

# Run main function
main "$@"