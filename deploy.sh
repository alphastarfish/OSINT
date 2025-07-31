#!/bin/bash

# TechProfits Pro Deployment Script
# This script helps deploy the website to various hosting platforms

echo "🚀 TechProfits Pro Deployment Helper"
echo "====================================="

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found. Make sure you're in the project directory."
    exit 1
fi

echo "✅ Project files found"

# Function to deploy to Netlify
deploy_netlify() {
    echo "📡 Deploying to Netlify..."
    
    # Check if Netlify CLI is installed
    if ! command -v netlify &> /dev/null; then
        echo "Installing Netlify CLI..."
        npm install -g netlify-cli
    fi
    
    # Login to Netlify (if not already logged in)
    netlify login
    
    # Deploy
    netlify deploy --prod --dir .
    
    echo "✅ Deployed to Netlify!"
}

# Function to deploy to Vercel
deploy_vercel() {
    echo "📡 Deploying to Vercel..."
    
    # Check if Vercel CLI is installed
    if ! command -v vercel &> /dev/null; then
        echo "Installing Vercel CLI..."
        npm install -g vercel
    fi
    
    # Deploy
    vercel --prod
    
    echo "✅ Deployed to Vercel!"
}

# Function to deploy to GitHub Pages
deploy_github_pages() {
    echo "📡 Setting up for GitHub Pages..."
    
    # Check if we're in a git repository
    if [ ! -d ".git" ]; then
        echo "Initializing git repository..."
        git init
        git add .
        git commit -m "Initial commit - TechProfits Pro website"
    fi
    
    echo "📝 Next steps for GitHub Pages:"
    echo "1. Create a new repository on GitHub"
    echo "2. Push this code to the repository:"
    echo "   git remote add origin https://github.com/yourusername/your-repo.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo "3. Go to repository Settings > Pages"
    echo "4. Select 'Deploy from a branch' and choose 'main'"
    echo "5. Your site will be available at: https://yourusername.github.io/your-repo"
}

# Function to create hosting-ready package
create_package() {
    echo "📦 Creating hosting-ready package..."
    
    # Create deployment directory
    mkdir -p deploy
    
    # Copy all necessary files
    cp index.html deploy/
    cp styles.css deploy/
    cp script.js deploy/
    cp package.json deploy/
    cp README.md deploy/
    
    # Create .htaccess for Apache servers
    cat > deploy/.htaccess << EOL
# Enable GZIP compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>

# Set cache headers
<IfModule mod_expires.c>
    ExpiresActive on
    ExpiresByType text/css "access plus 1 year"
    ExpiresByType application/javascript "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
</IfModule>

# Force HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
EOL
    
    # Create robots.txt
    cat > deploy/robots.txt << EOL
User-agent: *
Allow: /

Sitemap: https://yourdomain.com/sitemap.xml
EOL
    
    # Create basic sitemap.xml
    cat > deploy/sitemap.xml << EOL
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://yourdomain.com/</loc>
        <lastmod>$(date +%Y-%m-%d)</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>
EOL
    
    echo "✅ Package created in 'deploy' directory"
    echo "📁 Upload the contents of the 'deploy' directory to your web hosting"
}

# Function to test locally
test_local() {
    echo "🧪 Starting local test server..."
    
    # Check if Python 3 is available
    if command -v python3 &> /dev/null; then
        echo "🌐 Server running at: http://localhost:8000"
        echo "Press Ctrl+C to stop"
        python3 -m http.server 8000
    elif command -v python &> /dev/null; then
        echo "🌐 Server running at: http://localhost:8000"
        echo "Press Ctrl+C to stop"
        python -m SimpleHTTPServer 8000
    else
        echo "❌ Python not found. Please install Python to run local server."
        echo "💡 Alternative: Install Node.js and run 'npx serve .'"
    fi
}

# Function to validate setup
validate_setup() {
    echo "🔍 Validating website setup..."
    
    local errors=0
    
    # Check required files
    if [ ! -f "index.html" ]; then
        echo "❌ Missing: index.html"
        errors=$((errors + 1))
    fi
    
    if [ ! -f "styles.css" ]; then
        echo "❌ Missing: styles.css"
        errors=$((errors + 1))
    fi
    
    if [ ! -f "script.js" ]; then
        echo "❌ Missing: script.js"
        errors=$((errors + 1))
    fi
    
    # Check for placeholder content that needs customization
    if grep -q "GA_TRACKING_ID" index.html; then
        echo "⚠️  Warning: Replace GA_TRACKING_ID with your Google Analytics ID"
        errors=$((errors + 1))
    fi
    
    if grep -q "yourref" index.html; then
        echo "⚠️  Warning: Replace 'yourref' with your actual affiliate codes"
        errors=$((errors + 1))
    fi
    
    if [ $errors -eq 0 ]; then
        echo "✅ Website setup validation passed!"
    else
        echo "⚠️  Found $errors issues that need attention"
    fi
    
    return $errors
}

# Function to optimize for production
optimize_production() {
    echo "⚡ Optimizing for production..."
    
    # Create optimized directory
    mkdir -p optimized
    
    # Copy files
    cp index.html optimized/
    cp styles.css optimized/
    cp script.js optimized/
    
    # Minify CSS (basic minification)
    if command -v sed &> /dev/null; then
        sed 's/[[:space:]]*\/\*[^*]*\*\///g' styles.css | sed 's/^[[:space:]]*//g' | sed 's/[[:space:]]*$//g' > optimized/styles.min.css
        echo "✅ CSS minified"
    fi
    
    # Add performance optimizations to HTML
    sed -i.bak 's/<link href="styles.css"/<link href="styles.min.css"/g' optimized/index.html 2>/dev/null || \
    sed -i '' 's/<link href="styles.css"/<link href="styles.min.css"/g' optimized/index.html 2>/dev/null
    
    echo "✅ Production optimization complete in 'optimized' directory"
}

# Main menu
echo ""
echo "Choose deployment option:"
echo "1) 🧪 Test locally"
echo "2) 🔍 Validate setup"
echo "3) 📦 Create hosting package"
echo "4) ⚡ Optimize for production"
echo "5) 📡 Deploy to Netlify"
echo "6) 📡 Deploy to Vercel"
echo "7) 📡 Setup for GitHub Pages"
echo "8) ❌ Exit"
echo ""

read -p "Enter your choice (1-8): " choice

case $choice in
    1)
        test_local
        ;;
    2)
        validate_setup
        ;;
    3)
        create_package
        ;;
    4)
        optimize_production
        ;;
    5)
        deploy_netlify
        ;;
    6)
        deploy_vercel
        ;;
    7)
        deploy_github_pages
        ;;
    8)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "🎉 Task completed!"
echo "💡 Tip: Don't forget to customize your affiliate links and Google Analytics ID for maximum revenue!"
echo "📚 Check README.md for detailed setup and optimization instructions."