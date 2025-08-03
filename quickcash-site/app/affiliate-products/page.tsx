'use client'

import Link from 'next/link'
import AffiliateProducts from '@/components/AffiliateProducts'
import EmailCapture from '@/components/EmailCapture'

export default function AffiliateProductsPage() {
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
            <Link href="/services" className="hover:underline">Services</Link>
            <Link href="/digital-products" className="hover:underline">Digital Products</Link>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-16 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-6">
            Top Affiliate Products That Actually Pay
          </h1>
          <p className="text-xl mb-8">
            These are the exact products I promote to make $3,000+ per month
          </p>
          <div className="bg-yellow-400 text-gray-900 inline-block px-6 py-3 rounded-lg font-bold">
            Some Products Pay Up To $2,500 Per Sale! 🤯
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-12 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-8">
            How Affiliate Marketing Works
          </h2>
          <div className="grid md:grid-cols-4 gap-6 text-center">
            <div>
              <div className="text-4xl mb-3">1️⃣</div>
              <h3 className="font-bold mb-2">Choose Product</h3>
              <p className="text-sm text-gray-600">Pick products you believe in</p>
            </div>
            <div>
              <div className="text-4xl mb-3">2️⃣</div>
              <h3 className="font-bold mb-2">Get Your Link</h3>
              <p className="text-sm text-gray-600">Sign up for free affiliate program</p>
            </div>
            <div>
              <div className="text-4xl mb-3">3️⃣</div>
              <h3 className="font-bold mb-2">Share & Promote</h3>
              <p className="text-sm text-gray-600">Share on social media, blog, etc.</p>
            </div>
            <div>
              <div className="text-4xl mb-3">4️⃣</div>
              <h3 className="font-bold mb-2">Earn Commissions</h3>
              <p className="text-sm text-gray-600">Get paid for every sale!</p>
            </div>
          </div>
        </div>
      </section>

      {/* Products Grid */}
      <section className="py-16 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-4">
            🔥 Highest-Paying Affiliate Programs
          </h2>
          <p className="text-center text-gray-600 mb-12">
            Updated daily with the best converting offers
          </p>
          <AffiliateProducts />
        </div>
      </section>

      {/* Success Tips */}
      <section className="py-16 px-4 bg-money-green text-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-8">
            💡 Pro Tips for Maximum Earnings
          </h2>
          <div className="grid md:grid-cols-2 gap-6">
            <div className="bg-white/10 rounded-lg p-6">
              <h3 className="text-xl font-bold mb-3">✅ Do This:</h3>
              <ul className="space-y-2">
                <li>• Focus on 2-3 products initially</li>
                <li>• Create honest reviews and tutorials</li>
                <li>• Build an email list of interested buyers</li>
                <li>• Use multiple traffic sources</li>
                <li>• Track your results and optimize</li>
              </ul>
            </div>
            <div className="bg-white/10 rounded-lg p-6">
              <h3 className="text-xl font-bold mb-3">❌ Avoid This:</h3>
              <ul className="space-y-2">
                <li>• Spamming links everywhere</li>
                <li>• Promoting products you haven't tried</li>
                <li>• Ignoring FTC disclosure rules</li>
                <li>• Giving up too quickly</li>
                <li>• Focusing only on high-ticket items</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Email Capture */}
      <section className="py-16 px-4 bg-gray-100">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl font-bold mb-6">
            Want My Secret List of $500+ Commission Products?
          </h2>
          <p className="text-xl mb-8">
            Get access to exclusive high-ticket affiliate programs not listed here
          </p>
          <EmailCapture />
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8 px-4">
        <div className="max-w-6xl mx-auto text-center">
          <p className="mb-4">© 2024 Quick Cash Hub. All rights reserved.</p>
          <p className="text-sm text-gray-400 mb-4">
            Affiliate Disclosure: We earn commissions from qualifying purchases at no extra cost to you.
          </p>
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