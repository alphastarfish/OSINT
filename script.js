// TechProfits Pro - Advanced JavaScript functionality

// Configuration
const CONFIG = {
    emailAPI: 'https://api.convertkit.com/v3/', // Replace with actual API
    analyticsID: 'GA_TRACKING_ID', // Replace with actual Google Analytics ID
    affiliateCommission: 0.30, // 30% commission rate
    conversionGoals: {
        email_signup: 50, // $50 value per email signup
        affiliate_click: 25, // $25 value per affiliate click
        course_purchase: 297 // Course price
    }
};

// Revenue tracking
class RevenueTracker {
    constructor() {
        this.dailyGoal = 100;
        this.currentRevenue = this.loadRevenue();
        this.updateDisplay();
        this.startAutoSave();
    }

    loadRevenue() {
        return parseFloat(localStorage.getItem('dailyRevenue')) || 0;
    }

    saveRevenue() {
        localStorage.setItem('dailyRevenue', this.currentRevenue.toString());
        localStorage.setItem('lastUpdate', new Date().toDateString());
    }

    addRevenue(amount, source) {
        this.currentRevenue += amount;
        this.saveRevenue();
        this.updateDisplay();
        this.trackConversion(amount, source);
        
        // Show success animation
        this.showSuccessNotification(amount, source);
        
        // Check if daily goal reached
        if (this.currentRevenue >= this.dailyGoal) {
            this.celebrateDailyGoal();
        }
    }

    updateDisplay() {
        const progressElement = document.getElementById('revenue-progress');
        const amountElement = document.getElementById('current-revenue');
        
        if (progressElement && amountElement) {
            const percentage = Math.min((this.currentRevenue / this.dailyGoal) * 100, 100);
            progressElement.style.width = `${percentage}%`;
            amountElement.textContent = `$${this.currentRevenue.toFixed(2)}`;
        }
    }

    trackConversion(amount, source) {
        if (typeof gtag !== 'undefined') {
            gtag('event', 'purchase', {
                'transaction_id': Date.now().toString(),
                'value': amount,
                'currency': 'USD',
                'event_category': 'monetization',
                'event_label': source
            });
        }
    }

    showSuccessNotification(amount, source) {
        const notification = document.createElement('div');
        notification.className = 'fixed top-4 right-4 bg-green-500 text-white p-4 rounded-lg shadow-lg z-50 success-bounce';
        notification.innerHTML = `
            <div class="flex items-center">
                <i class="fas fa-check-circle mr-2"></i>
                <div>
                    <div class="font-bold">+$${amount.toFixed(2)} earned!</div>
                    <div class="text-sm opacity-90">${source}</div>
                </div>
            </div>
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 5000);
    }

    celebrateDailyGoal() {
        // Confetti effect or celebration
        const celebration = document.createElement('div');
        celebration.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
        celebration.innerHTML = `
            <div class="bg-white rounded-xl p-8 text-center max-w-md mx-4">
                <div class="text-6xl mb-4">🎉</div>
                <h3 class="text-2xl font-bold mb-2">Daily Goal Reached!</h3>
                <p class="text-gray-600 mb-4">Congratulations! You've earned $${this.currentRevenue.toFixed(2)} today.</p>
                <button onclick="this.parentElement.parentElement.remove()" class="bg-blue-600 text-white px-6 py-2 rounded-lg">
                    Awesome!
                </button>
            </div>
        `;
        
        document.body.appendChild(celebration);
    }

    startAutoSave() {
        setInterval(() => {
            this.saveRevenue();
        }, 30000); // Save every 30 seconds
    }

    resetDaily() {
        const today = new Date().toDateString();
        const lastUpdate = localStorage.getItem('lastUpdate');
        
        if (lastUpdate && lastUpdate !== today) {
            this.currentRevenue = 0;
            this.saveRevenue();
            this.updateDisplay();
        }
    }
}

// Email capture and list building
class EmailCapture {
    constructor() {
        this.setupForms();
        this.setupExitIntent();
        this.setupScrollTrigger();
    }

    setupForms() {
        document.querySelectorAll('form').forEach(form => {
            form.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.handleSubmission(form);
            });
        });
    }

    async handleSubmission(form) {
        const formData = new FormData(form);
        const email = formData.get('email') || form.querySelector('[type="email"]')?.value;
        const name = formData.get('name') || form.querySelector('[type="text"]')?.value;

        if (!email) return;

        // Show loading state
        const submitBtn = form.querySelector('[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Subscribing...';
        submitBtn.disabled = true;

        try {
            // Simulate API call (replace with actual email service)
            await this.simulateAPICall(email, name);
            
            // Track successful signup
            revenueTracker.addRevenue(CONFIG.conversionGoals.email_signup, 'Email Signup');
            
            // Show success message
            this.showSuccessMessage(form);
            
            // Reset form
            form.reset();
            
        } catch (error) {
            console.error('Email signup failed:', error);
            this.showErrorMessage(form);
        } finally {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    }

    async simulateAPICall(email, name) {
        // Simulate API delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // Store in localStorage for demo purposes
        const subscribers = JSON.parse(localStorage.getItem('subscribers') || '[]');
        subscribers.push({ email, name, date: new Date().toISOString() });
        localStorage.setItem('subscribers', JSON.stringify(subscribers));
        
        return { success: true };
    }

    showSuccessMessage(form) {
        const message = document.createElement('div');
        message.className = 'bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mt-4';
        message.innerHTML = `
            <div class="flex items-center">
                <i class="fas fa-check-circle mr-2"></i>
                <span>Success! Check your email for the free success kit.</span>
            </div>
        `;
        form.appendChild(message);
        
        setTimeout(() => message.remove(), 5000);
    }

    showErrorMessage(form) {
        const message = document.createElement('div');
        message.className = 'bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mt-4';
        message.innerHTML = `
            <div class="flex items-center">
                <i class="fas fa-exclamation-circle mr-2"></i>
                <span>Something went wrong. Please try again.</span>
            </div>
        `;
        form.appendChild(message);
        
        setTimeout(() => message.remove(), 5000);
    }

    setupExitIntent() {
        let exitIntentShown = false;
        
        document.addEventListener('mouseleave', (e) => {
            if (e.clientY <= 0 && !exitIntentShown) {
                exitIntentShown = true;
                this.showExitIntentPopup();
            }
        });
    }

    showExitIntentPopup() {
        const popup = document.createElement('div');
        popup.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
        popup.innerHTML = `
            <div class="bg-white rounded-xl p-8 max-w-md mx-4 text-center">
                <div class="text-4xl mb-4">⚡</div>
                <h3 class="text-2xl font-bold mb-2">Wait! Don't Miss Out!</h3>
                <p class="text-gray-600 mb-4">Get our exclusive $100/day blueprint before you leave!</p>
                <form class="mb-4">
                    <input type="email" placeholder="Enter your email" class="w-full px-4 py-2 border rounded-lg mb-2" required>
                    <button type="submit" class="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700">
                        Get Free Blueprint
                    </button>
                </form>
                <button onclick="this.parentElement.parentElement.remove()" class="text-gray-500 text-sm">
                    No thanks, I'll figure it out myself
                </button>
            </div>
        `;
        
        document.body.appendChild(popup);
        
        // Setup form submission for popup
        const popupForm = popup.querySelector('form');
        popupForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            await this.handleSubmission(popupForm);
            popup.remove();
        });
    }

    setupScrollTrigger() {
        let scrollTriggerShown = false;
        
        window.addEventListener('scroll', () => {
            const scrolled = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
            
            if (scrolled > 50 && !scrollTriggerShown) {
                scrollTriggerShown = true;
                this.showScrollTriggerBanner();
            }
        });
    }

    showScrollTriggerBanner() {
        const banner = document.createElement('div');
        banner.className = 'fixed bottom-0 left-0 right-0 bg-yellow-400 text-black p-4 z-40 transform translate-y-full transition-transform duration-500';
        banner.innerHTML = `
            <div class="max-w-4xl mx-auto flex items-center justify-between">
                <div class="flex items-center">
                    <i class="fas fa-gift mr-2"></i>
                    <span class="font-semibold">Limited Time: Free $100/Day Success Kit!</span>
                </div>
                <div class="flex items-center space-x-4">
                    <input type="email" placeholder="Email" class="px-3 py-1 rounded border">
                    <button class="bg-black text-yellow-400 px-4 py-1 rounded font-semibold">Get It Free</button>
                    <button onclick="this.parentElement.parentElement.parentElement.remove()" class="text-black">×</button>
                </div>
            </div>
        `;
        
        document.body.appendChild(banner);
        
        // Animate in
        setTimeout(() => {
            banner.style.transform = 'translateY(0)';
        }, 100);
        
        // Auto-hide after 10 seconds
        setTimeout(() => {
            banner.style.transform = 'translateY(100%)';
            setTimeout(() => banner.remove(), 500);
        }, 10000);
    }
}

// Affiliate link tracking
class AffiliateTracker {
    constructor() {
        this.setupAffiliateLinks();
        this.trackPageViews();
    }

    setupAffiliateLinks() {
        document.querySelectorAll('a[href*="?ref="], a[href*="&ref="]').forEach(link => {
            link.addEventListener('click', (e) => {
                this.trackAffiliateClick(link);
            });
        });
    }

    trackAffiliateClick(link) {
        const url = new URL(link.href);
        const product = link.dataset.product || this.extractProductFromURL(url);
        
        // Track revenue (estimated based on conversion rates)
        const estimatedRevenue = CONFIG.conversionGoals.affiliate_click;
        revenueTracker.addRevenue(estimatedRevenue, `Affiliate Click: ${product}`);
        
        // Track in analytics
        if (typeof gtag !== 'undefined') {
            gtag('event', 'click', {
                'event_category': 'affiliate',
                'event_label': product,
                'value': estimatedRevenue
            });
        }
        
        // Store click data
        this.storeClickData(product, url.hostname);
    }

    extractProductFromURL(url) {
        const hostname = url.hostname.toLowerCase();
        if (hostname.includes('teachable')) return 'Teachable';
        if (hostname.includes('convertkit')) return 'ConvertKit';
        if (hostname.includes('shopify')) return 'Shopify';
        if (hostname.includes('later')) return 'Later';
        if (hostname.includes('semrush')) return 'SEMrush';
        if (hostname.includes('canva')) return 'Canva';
        return 'Unknown Product';
    }

    storeClickData(product, domain) {
        const clicks = JSON.parse(localStorage.getItem('affiliateClicks') || '[]');
        clicks.push({
            product,
            domain,
            timestamp: new Date().toISOString(),
            revenue: CONFIG.conversionGoals.affiliate_click
        });
        localStorage.setItem('affiliateClicks', JSON.stringify(clicks));
    }

    trackPageViews() {
        // Track page views for revenue estimation
        const pageViews = parseInt(localStorage.getItem('pageViews') || '0') + 1;
        localStorage.setItem('pageViews', pageViews.toString());
        
        // Estimate revenue based on page views (rough calculation)
        if (pageViews % 100 === 0) { // Every 100 page views
            revenueTracker.addRevenue(10, 'Ad Revenue (estimated)');
        }
    }
}

// Performance monitoring
class PerformanceMonitor {
    constructor() {
        this.trackLoadTime();
        this.trackUserEngagement();
        this.optimizeImages();
    }

    trackLoadTime() {
        window.addEventListener('load', () => {
            const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
            
            if (typeof gtag !== 'undefined') {
                gtag('event', 'timing_complete', {
                    'name': 'load',
                    'value': loadTime
                });
            }
            
            console.log(`Page loaded in ${loadTime}ms`);
        });
    }

    trackUserEngagement() {
        let startTime = Date.now();
        let isActive = true;
        
        // Track time on page
        window.addEventListener('beforeunload', () => {
            const timeOnPage = Date.now() - startTime;
            
            if (typeof gtag !== 'undefined') {
                gtag('event', 'engagement_time', {
                    'value': timeOnPage
                });
            }
        });
        
        // Track scroll depth
        let maxScroll = 0;
        window.addEventListener('scroll', () => {
            const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
            maxScroll = Math.max(maxScroll, scrollPercent);
            
            // Track scroll milestones
            if (scrollPercent > 25 && !this.scrollMilestones?.quarter) {
                this.trackScrollMilestone('25%');
                this.scrollMilestones = { ...this.scrollMilestones, quarter: true };
            }
            if (scrollPercent > 50 && !this.scrollMilestones?.half) {
                this.trackScrollMilestone('50%');
                this.scrollMilestones = { ...this.scrollMilestones, half: true };
            }
            if (scrollPercent > 75 && !this.scrollMilestones?.three_quarters) {
                this.trackScrollMilestone('75%');
                this.scrollMilestones = { ...this.scrollMilestones, three_quarters: true };
            }
        });
    }

    trackScrollMilestone(milestone) {
        if (typeof gtag !== 'undefined') {
            gtag('event', 'scroll', {
                'event_category': 'engagement',
                'event_label': milestone
            });
        }
    }

    optimizeImages() {
        // Lazy load images
        const images = document.querySelectorAll('img[data-src]');
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('img-fade-in');
                    observer.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }

    scrollMilestones = {};
}

// Revenue dashboard
function createRevenueDashboard() {
    const dashboard = document.createElement('div');
    dashboard.id = 'revenue-dashboard';
    dashboard.className = 'fixed top-20 left-4 bg-white rounded-lg shadow-lg p-4 z-40 max-w-xs';
    dashboard.innerHTML = `
        <div class="text-center">
            <h4 class="font-bold mb-2">Today's Progress</h4>
            <div class="text-2xl font-bold text-green-600" id="current-revenue">$0.00</div>
            <div class="text-sm text-gray-600 mb-2">Goal: $100.00</div>
            <div class="w-full bg-gray-200 rounded-full h-2">
                <div id="revenue-progress" class="bg-green-600 h-2 rounded-full transition-all duration-500" style="width: 0%"></div>
            </div>
            <button onclick="this.parentElement.parentElement.style.display='none'" class="text-xs text-gray-500 mt-2">Hide</button>
        </div>
    `;
    
    document.body.appendChild(dashboard);
    
    // Auto-hide after 10 seconds, show toggle button
    setTimeout(() => {
        dashboard.style.display = 'none';
        
        const toggleButton = document.createElement('button');
        toggleButton.className = 'fixed top-20 left-4 bg-green-600 text-white p-2 rounded-full shadow-lg z-40';
        toggleButton.innerHTML = '<i class="fas fa-chart-line"></i>';
        toggleButton.onclick = () => {
            dashboard.style.display = dashboard.style.display === 'none' ? 'block' : 'none';
        };
        
        document.body.appendChild(toggleButton);
    }, 10000);
}

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Initialize all tracking systems
    window.revenueTracker = new RevenueTracker();
    window.emailCapture = new EmailCapture();
    window.affiliateTracker = new AffiliateTracker();
    window.performanceMonitor = new PerformanceMonitor();
    
    // Create revenue dashboard
    createRevenueDashboard();
    
    // Check for daily reset
    revenueTracker.resetDaily();
    
    // Add scroll progress bar
    const progressBar = document.createElement('div');
    progressBar.className = 'progress-bar';
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', () => {
        const scrolled = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
        progressBar.style.width = `${scrolled}%`;
    });
    
    console.log('TechProfits Pro loaded successfully! 💰');
});

// Export for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        RevenueTracker,
        EmailCapture,
        AffiliateTracker,
        PerformanceMonitor
    };
}