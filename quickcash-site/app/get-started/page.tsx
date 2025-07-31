'use client'

import Link from 'next/link'
import EmailCapture from '@/components/EmailCapture'

export default function GetStartedPage() {
  return (
    <main className="min-h-screen">
      {/* Header */}
      <header className="bg-money-green text-white py-4 px-4">
        <div className="max-w-6xl mx-auto flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold">
            Quick Cash Hub
          </Link>
          <nav className="space-x-6">
            <Link href="/" className="hover:underline">Home</Link>
            <Link href="/affiliate-products" className="hover:underline">Products</Link>
            <Link href="/services" className="hover:underline">Services</Link>
          </nav>
        </div>
      </header>

      {/* Hero */}
      <section className="bg-gradient-to-r from-purple-600 to-pink-600 text-white py-16 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-6">
            Your $100/Day Journey Starts NOW
          </h1>
          <p className="text-xl mb-8">
            Follow this exact blueprint to start making money within 24-48 hours
          </p>
        </div>
      </section>

      {/* Emergency Action Plan */}
      <section className="py-16 px-4 bg-red-50">
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-lg shadow-xl p-8 border-4 border-red-500">
            <h2 className="text-3xl font-bold mb-6 text-red-600">
              🚨 EMERGENCY MONEY PLAN (If You Need Cash FAST)
            </h2>
            <p className="mb-6">Do these TODAY for fastest results:</p>
            
            <div className="space-y-6">
              <div className="bg-yellow-50 p-6 rounded-lg">
                <h3 className="text-xl font-bold mb-3">1. Website Testing (Make $10-60 TODAY)</h3>
                <ol className="space-y-2 ml-6">
                  <li>• Sign up: UserTesting.com (takes 10 minutes)</li>
                  <li>• Complete sample test</li>
                  <li>• Start earning $10-60 per 20-minute test</li>
                  <li>• Can make $100+ on your first day!</li>
                </ol>
                <a href="https://www.usertesting.com" target="_blank" rel="noopener noreferrer" 
                   className="inline-block mt-3 text-blue-600 font-bold hover:underline">
                  → Start Testing Now
                </a>
              </div>

              <div className="bg-green-50 p-6 rounded-lg">
                <h3 className="text-xl font-bold mb-3">2. Quick Fiverr Gigs (Make $25-200 TODAY)</h3>
                <p className="mb-2">Services that sell immediately:</p>
                <ul className="space-y-1 ml-6">
                  <li>• Remove background from 10 images ($25)</li>
                  <li>• Write product descriptions ($50)</li>
                  <li>• Create simple logos in Canva ($25)</li>
                  <li>• Do 1 hour of data entry ($40)</li>
                </ul>
                <a href="https://www.fiverr.com" target="_blank" rel="noopener noreferrer" 
                   className="inline-block mt-3 text-blue-600 font-bold hover:underline">
                  → Create Your First Gig
                </a>
              </div>

              <div className="bg-blue-50 p-6 rounded-lg">
                <h3 className="text-xl font-bold mb-3">3. Facebook Marketplace Flip (Make $50-500 THIS WEEK)</h3>
                <ol className="space-y-2 ml-6">
                  <li>• Find free items on Craigslist/Facebook</li>
                  <li>• Clean them up</li>
                  <li>• Resell for profit</li>
                  <li>• Focus on: furniture, electronics, appliances</li>
                </ol>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 30-Day Plan */}
      <section className="py-16 px-4">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            Your 30-Day $100/Day Roadmap
          </h2>
          
          <div className="space-y-8">
            {/* Week 1 */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-2xl font-bold mb-4 text-money-green">Week 1: Quick Wins (Target: $200)</h3>
              <ul className="space-y-3">
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <div>
                    <strong>Day 1-2:</strong> Sign up for UserTesting, Fiverr, and Upwork. Create profiles.
                  </div>
                </li>
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <div>
                    <strong>Day 3-4:</strong> Complete 5 website tests ($50-300)
                  </div>
                </li>
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <div>
                    <strong>Day 5-7:</strong> Launch 3 quick Fiverr gigs, apply to 20 Upwork jobs
                  </div>
                </li>
              </ul>
            </div>

            {/* Week 2 */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-2xl font-bold mb-4 text-money-green">Week 2: Build Momentum (Target: $500)</h3>
              <ul className="space-y-3">
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <div>
                    <strong>Day 8-10:</strong> Land first freelance client, start affiliate marketing setup
                  </div>
                </li>
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <div>
                    <strong>Day 11-12:</strong> Create social media accounts for promotion
                  </div>
                </li>
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <div>
                    <strong>Day 13-14:</strong> Launch first affiliate campaigns, scale what's working
                  </div>
                </li>
              </ul>
            </div>

            {/* Week 3-4 */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-2xl font-bold mb-4 text-money-green">Week 3-4: Scale Up (Target: $1,500+)</h3>
              <ul className="space-y-3">
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <div>
                    <strong>Week 3:</strong> Increase rates, add more services, create digital product
                  </div>
                </li>
                <li className="flex items-start">
                  <span className="text-green-500 mr-2">✓</span>
                  <div>
                    <strong>Week 4:</strong> Automate processes, hire VA, scale winning strategies
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Resources Section */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            Free Resources to Get You Started
          </h2>
          
          <div className="grid md:grid-cols-2 gap-6">
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-xl font-bold mb-4">📧 Email Templates</h3>
              <p className="mb-4">Copy-paste templates for landing clients</p>
              <ul className="space-y-2 text-sm">
                <li>• Cold outreach templates</li>
                <li>• Follow-up sequences</li>
                <li>• Price negotiation scripts</li>
              </ul>
            </div>
            
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-xl font-bold mb-4">🎯 Traffic Sources</h3>
              <p className="mb-4">Where to promote for free</p>
              <ul className="space-y-2 text-sm">
                <li>• Reddit marketing guide</li>
                <li>• Facebook group strategy</li>
                <li>• TikTok viral formulas</li>
              </ul>
            </div>
            
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-xl font-bold mb-4">💰 Pricing Calculator</h3>
              <p className="mb-4">Know exactly what to charge</p>
              <ul className="space-y-2 text-sm">
                <li>• Service pricing guide</li>
                <li>• Profit margin calculator</li>
                <li>• Rate increase timeline</li>
              </ul>
            </div>
            
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h3 className="text-xl font-bold mb-4">🚀 Quick Start Checklist</h3>
              <p className="mb-4">Never miss a step</p>
              <ul className="space-y-2 text-sm">
                <li>• Platform setup guide</li>
                <li>• Daily action items</li>
                <li>• Progress tracker</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Final CTA */}
      <section className="py-16 px-4 bg-gradient-to-r from-money-green to-dark-green text-white">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl font-bold mb-6">
            Get Everything You Need to Start Making $100/Day
          </h2>
          <p className="text-xl mb-8">
            Enter your email to get instant access to all templates, guides, and resources
          </p>
          <EmailCapture />
          <p className="mt-6 text-sm">
            🔒 Your information is 100% secure. We hate spam as much as you do.
          </p>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8 px-4">
        <div className="max-w-6xl mx-auto text-center">
          <p className="mb-4">© 2024 Quick Cash Hub. All rights reserved.</p>
          <div className="space-x-4">
            <Link href="/privacy" className="hover:underline">Privacy</Link>
            <Link href="/terms" className="hover:underline">Terms</Link>
            <Link href="/contact" className="hover:underline">Contact</Link>
          </div>
        </div>
      </footer>
    </main>
  )
}