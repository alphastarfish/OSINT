'use client'

import Link from 'next/link'
import { useState } from 'react'

const services = [
  {
    id: 1,
    title: 'Social Media Management',
    price: '$500-2000/month per client',
    time: '2-4 hours/day',
    difficulty: 'Easy',
    description: 'Manage social media accounts for small businesses. Post content, engage with followers, grow their presence.',
    skills: ['Basic social media knowledge', 'Content creation', 'Communication'],
    platforms: ['Upwork', 'Fiverr', 'Direct outreach'],
  },
  {
    id: 2,
    title: 'Virtual Assistant',
    price: '$15-50/hour',
    time: 'Flexible',
    difficulty: 'Easy',
    description: 'Help businesses with admin tasks, email management, scheduling, research, and data entry.',
    skills: ['Organization', 'Basic computer skills', 'Communication'],
    platforms: ['Belay', 'Time Etc', 'Fancy Hands'],
  },
  {
    id: 3,
    title: 'Content Writing',
    price: '$50-500/article',
    time: '2-4 hours/article',
    difficulty: 'Medium',
    description: 'Write blog posts, articles, and web content for businesses. High demand for quality writers.',
    skills: ['Writing skills', 'Research', 'SEO basics'],
    platforms: ['Contently', 'Scripted', 'WriterAccess'],
  },
  {
    id: 4,
    title: 'Online Tutoring',
    price: '$20-80/hour',
    time: 'Flexible',
    difficulty: 'Easy-Medium',
    description: 'Teach subjects you know online. English, math, science, or specialized skills.',
    skills: ['Subject expertise', 'Teaching ability', 'Patience'],
    platforms: ['VIPKid', 'Chegg Tutors', 'Tutor.com'],
  },
  {
    id: 5,
    title: 'Graphic Design',
    price: '$25-150/design',
    time: '1-4 hours/project',
    difficulty: 'Medium',
    description: 'Create logos, social media graphics, presentations, and marketing materials.',
    skills: ['Design software', 'Creativity', 'Client communication'],
    platforms: ['99designs', 'DesignCrowd', 'Fiverr'],
  },
  {
    id: 6,
    title: 'Website Testing',
    price: '$10-60/test',
    time: '20-60 minutes',
    difficulty: 'Very Easy',
    description: 'Test websites and apps for usability. Give feedback on user experience.',
    skills: ['Basic computer skills', 'Attention to detail', 'Clear communication'],
    platforms: ['UserTesting', 'TryMyUI', 'Userlytics'],
  }
]

export default function ServicesPage() {
  const [selectedService, setSelectedService] = useState<number | null>(null)

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
            <Link href="/affiliate-products" className="hover:underline">Affiliate Products</Link>
            <Link href="/digital-products" className="hover:underline">Digital Products</Link>
          </nav>
        </div>
      </header>

      {/* Hero */}
      <section className="bg-gradient-to-r from-orange-500 to-red-500 text-white py-16 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-6">
            Start Freelancing Today, Get Paid This Week
          </h1>
          <p className="text-xl mb-8">
            Use your existing skills to make money immediately. No degree required!
          </p>
          <div className="bg-white text-orange-500 inline-block px-6 py-3 rounded-lg font-bold">
            Average Freelancer Makes $28/hour 💰
          </div>
        </div>
      </section>

      {/* Quick Start Guide */}
      <section className="py-12 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-8">
            🚀 Quick Start Guide
          </h2>
          <div className="bg-white rounded-lg shadow-lg p-8">
            <ol className="space-y-4">
              <li className="flex items-start">
                <span className="bg-money-green text-white rounded-full w-8 h-8 flex items-center justify-center font-bold mr-3 flex-shrink-0">1</span>
                <div>
                  <strong>Choose Your Service:</strong> Pick something you can do today (even basic skills work!)
                </div>
              </li>
              <li className="flex items-start">
                <span className="bg-money-green text-white rounded-full w-8 h-8 flex items-center justify-center font-bold mr-3 flex-shrink-0">2</span>
                <div>
                  <strong>Create Your Profile:</strong> Sign up on 2-3 platforms (takes 30 minutes)
                </div>
              </li>
              <li className="flex items-start">
                <span className="bg-money-green text-white rounded-full w-8 h-8 flex items-center justify-center font-bold mr-3 flex-shrink-0">3</span>
                <div>
                  <strong>Apply to 10 Jobs:</strong> Use templates to apply quickly (1 hour)
                </div>
              </li>
              <li className="flex items-start">
                <span className="bg-money-green text-white rounded-full w-8 h-8 flex items-center justify-center font-bold mr-3 flex-shrink-0">4</span>
                <div>
                  <strong>Land Your First Client:</strong> Usually happens within 24-48 hours!
                </div>
              </li>
            </ol>
          </div>
        </div>
      </section>

      {/* Services Grid */}
      <section className="py-16 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            Top Money-Making Services You Can Start Today
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {services.map((service) => (
              <div key={service.id} className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow">
                <h3 className="text-xl font-bold mb-2">{service.title}</h3>
                <div className="mb-4">
                  <span className="text-2xl font-bold text-money-green">{service.price}</span>
                  <div className="text-sm text-gray-600 mt-1">
                    <span className="inline-block mr-3">⏱️ {service.time}</span>
                    <span className="inline-block">📊 {service.difficulty}</span>
                  </div>
                </div>
                <p className="text-gray-600 mb-4">{service.description}</p>
                <button
                  onClick={() => setSelectedService(selectedService === service.id ? null : service.id)}
                  className="text-money-green font-bold hover:underline"
                >
                  {selectedService === service.id ? 'Hide Details' : 'Show Details'} →
                </button>
                
                {selectedService === service.id && (
                  <div className="mt-4 pt-4 border-t">
                    <div className="mb-3">
                      <strong>Skills Needed:</strong>
                      <ul className="mt-1">
                        {service.skills.map((skill, idx) => (
                          <li key={idx} className="text-sm text-gray-600">• {skill}</li>
                        ))}
                      </ul>
                    </div>
                    <div>
                      <strong>Best Platforms:</strong>
                      <ul className="mt-1">
                        {service.platforms.map((platform, idx) => (
                          <li key={idx} className="text-sm text-gray-600">• {platform}</li>
                        ))}
                      </ul>
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Success Story */}
      <section className="py-16 px-4 bg-yellow-50">
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-3xl font-bold mb-6">
              "I Made $2,400 in My First Month!" 
            </h2>
            <p className="text-lg mb-4">
              "I started as a virtual assistant with zero experience. Within 30 days, I had 3 regular clients paying me $800/month each. Now I work from home and have complete freedom!"
            </p>
            <p className="text-gray-600">- Sarah M., Virtual Assistant</p>
            <Link href="#" className="money-button inline-block mt-6">
              Start Your Success Story
            </Link>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 px-4 bg-gradient-to-r from-money-green to-dark-green text-white">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl font-bold mb-6">
            Ready to Make Your First $100 Today?
          </h2>
          <p className="text-xl mb-8">
            Get my freelancing templates + client-getting scripts FREE
          </p>
          <Link href="/get-started" className="bg-white text-money-green font-bold py-4 px-8 rounded-lg hover:bg-gray-100 inline-block text-lg">
            Give Me The Templates! 📄
          </Link>
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