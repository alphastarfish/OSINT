'use client'

import { useState } from 'react'
import Link from 'next/link'
import EmailCapture from '@/components/EmailCapture'
import AffiliateProducts from '@/components/AffiliateProducts'
import AdBanner from '@/components/AdBanner'

export default function Home() {
  const [email, setEmail] = useState('')

  return (
    <main className="min-h-screen">
      {/* Hero Section - Immediate Value Proposition */}
      <section className="bg-gradient-to-r from-money-green to-dark-green text-white py-20 px-4">
        <div className="max-w-6xl mx-auto text-center">
          <h1 className="text-5xl font-bold mb-6">
            Start Making $100+ Per Day Online
          </h1>
          <p className="text-2xl mb-8">
            Proven Methods That Work in 2024 - No Experience Required
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="#quick-wins" className="money-button pulse-animation">
              Show Me The Money! 💰
            </Link>
            <Link href="#free-guide" className="bg-white text-money-green font-bold py-3 px-6 rounded-lg hover:bg-gray-100">
              Get Free $100/Day Guide
            </Link>
          </div>
        </div>
      </section>

      {/* Ad Space - Top */}
      <AdBanner position="top" />

      {/* Quick Win Methods */}
      <section id="quick-wins" className="py-16 px-4 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-12">
            Fastest Ways to Make Money Today
          </h2>
          
          <div className="grid md:grid-cols-3 gap-8">
            {/* Method 1: Affiliate Marketing */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <div className="text-3xl mb-4">🛍️</div>
              <h3 className="text-2xl font-bold mb-3">Affiliate Marketing</h3>
              <p className="text-gray-600 mb-4">
                Earn 5-50% commissions promoting products. Start earning within 24 hours!
              </p>
              <ul className="mb-6 space-y-2">
                <li>✅ No inventory needed</li>
                <li>✅ $10-$500 per sale</li>
                <li>✅ Work from anywhere</li>
              </ul>
              <Link href="/affiliate-products" className="money-button block text-center">
                View Top Products
              </Link>
            </div>

            {/* Method 2: Freelance Services */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <div className="text-3xl mb-4">💼</div>
              <h3 className="text-2xl font-bold mb-3">Quick Freelance Gigs</h3>
              <p className="text-gray-600 mb-4">
                Offer services and get paid immediately. $25-$200 per gig!
              </p>
              <ul className="mb-6 space-y-2">
                <li>✅ Get paid same day</li>
                <li>✅ Use existing skills</li>
                <li>✅ Flexible schedule</li>
              </ul>
              <Link href="/services" className="money-button block text-center">
                Start Freelancing
              </Link>
            </div>

            {/* Method 3: Digital Products */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <div className="text-3xl mb-4">📱</div>
              <h3 className="text-2xl font-bold mb-3">Sell Digital Products</h3>
              <p className="text-gray-600 mb-4">
                Create once, sell forever. 100% profit margins!
              </p>
              <ul className="mb-6 space-y-2">
                <li>✅ Passive income</li>
                <li>✅ No shipping costs</li>
                <li>✅ Instant delivery</li>
              </ul>
              <Link href="/digital-products" className="money-button block text-center">
                Create & Sell Now
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* High-Converting Affiliate Products Section */}
      <section className="py-16 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-12">
            🔥 Hottest Money-Making Products (Earn Up to $75 Per Sale!)
          </h2>
          <AffiliateProducts />
        </div>
      </section>

      {/* Ad Space - Middle */}
      <AdBanner position="middle" />

      {/* Free Guide Lead Magnet */}
      <section id="free-guide" className="py-16 px-4 bg-money-green text-white">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold mb-6">
            FREE: The $100/Day Blueprint
          </h2>
          <p className="text-xl mb-8">
            Get my proven step-by-step guide that shows exactly how I make $100+ daily online
          </p>
          <EmailCapture />
          <p className="mt-4 text-sm">
            Join 10,000+ people already making money online
          </p>
        </div>
      </section>

      {/* Urgency Section */}
      <section className="py-16 px-4 bg-red-50">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl font-bold mb-6 text-red-600">
            ⚠️ Time-Sensitive Opportunity
          </h2>
          <p className="text-xl mb-8">
            These methods work NOW but may not last forever. The online landscape changes fast.
          </p>
          <div className="bg-white rounded-lg shadow-lg p-8 max-w-2xl mx-auto">
            <h3 className="text-2xl font-bold mb-4">Start Today and You Could:</h3>
            <ul className="text-left space-y-3 mb-6">
              <li>💰 Make your first $100 within 7 days</li>
              <li>📈 Scale to $500+/day within 30 days</li>
              <li>🏖️ Achieve location independence</li>
              <li>🚀 Build multiple income streams</li>
            </ul>
            <Link href="/get-started" className="money-button pulse-animation inline-block">
              I Want To Start Now!
            </Link>
          </div>
        </div>
      </section>

      {/* Ad Space - Bottom */}
      <AdBanner position="bottom" />

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8 px-4">
        <div className="max-w-6xl mx-auto text-center">
          <p className="mb-4">© 2024 Quick Cash Hub. All rights reserved.</p>
          <p className="text-sm text-gray-400">
            Earnings Disclaimer: Results vary. Success depends on effort and market conditions.
          </p>
          <div className="mt-4 space-x-4">
            <Link href="/privacy" className="hover:underline">Privacy Policy</Link>
            <Link href="/terms" className="hover:underline">Terms of Service</Link>
            <Link href="/contact" className="hover:underline">Contact</Link>
          </div>
        </div>
      </footer>
    </main>
  )
}