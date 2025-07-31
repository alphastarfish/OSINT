'use client'

import { useState } from 'react'
import Link from 'next/link'
import { motion } from 'framer-motion'
import QuantumAnimation from '@/components/QuantumAnimation'
import HealingModalities from '@/components/HealingModalities'
import ConsciousnessPrograms from '@/components/ConsciousnessPrograms'

export default function Home() {
  const [selectedPath, setSelectedPath] = useState<string | null>(null)

  return (
    <main className="min-h-screen neural-network-bg">
      {/* Navigation */}
      <nav className="fixed top-0 w-full z-50 bg-cosmic-dark/80 backdrop-blur-md border-b border-quantum-purple/20">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex justify-between items-center">
            <h1 className="text-2xl font-bold holographic-text">Consciousness Tech Hub</h1>
            <div className="space-x-6">
              <Link href="#healing" className="hover:text-healing-green transition-colors">Healing</Link>
              <Link href="#programs" className="hover:text-consciousness-blue transition-colors">Programs</Link>
              <Link href="#technology" className="hover:text-quantum-purple transition-colors">Technology</Link>
              <Link href="#membership" className="text-enlightenment-gold font-bold">Join ($97/mo)</Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center px-4">
        <QuantumAnimation />
        
        <div className="relative z-10 max-w-6xl mx-auto text-center">
          <motion.h1 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-5xl md:text-7xl font-bold mb-6"
          >
            <span className="holographic-text">Transcend Reality</span>
          </motion.h1>
          
          <motion.p 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="text-xl md:text-2xl mb-8 text-gray-300"
          >
            Where Ancient Wisdom Meets Quantum Technology
          </motion.p>
          
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="grid md:grid-cols-3 gap-6 mb-12"
          >
            <div className="consciousness-border rounded-lg p-6 hover:enlightenment-glow transition-all">
              <h3 className="text-xl font-bold mb-3 text-healing-green">100% Healing Modalities</h3>
              <p>Reconnective healing, tachyon technology, quantum field manipulation</p>
              <p className="text-enlightenment-gold mt-2 font-bold">$197 per session</p>
            </div>
            
            <div className="consciousness-border rounded-lg p-6 hover:enlightenment-glow transition-all">
              <h3 className="text-xl font-bold mb-3 text-consciousness-blue">Consciousness Training</h3>
              <p>Remote viewing, autonomic control, holographic perception mastery</p>
              <p className="text-enlightenment-gold mt-2 font-bold">$497 course</p>
            </div>
            
            <div className="consciousness-border rounded-lg p-6 hover:enlightenment-glow transition-all">
              <h3 className="text-xl font-bold mb-3 text-quantum-purple">Paradigm Solutions</h3>
              <p>Revolutionary tech, 3D printed homes, neuronal computing enhancement</p>
              <p className="text-enlightenment-gold mt-2 font-bold">$997 consultation</p>
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.6 }}
            className="space-x-4"
          >
            <Link href="#start" className="inline-block bg-gradient-to-r from-quantum-purple to-consciousness-blue text-white font-bold py-4 px-8 rounded-full hover:scale-105 transition-transform">
              Start Your Journey ($97)
            </Link>
            <Link href="#free" className="inline-block border-2 border-enlightenment-gold text-enlightenment-gold font-bold py-4 px-8 rounded-full hover:bg-enlightenment-gold hover:text-cosmic-dark transition-all">
              Free Resources
            </Link>
          </motion.div>
        </div>
      </section>

      {/* Revenue Model Section */}
      <section className="py-20 px-4 bg-cosmic-dark/50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-12 holographic-text">
            Revenue Streams ($100-1000/day)
          </h2>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="bg-gradient-to-br from-healing-green/20 to-transparent rounded-lg p-6 border border-healing-green/30">
              <h3 className="text-xl font-bold mb-3 text-healing-green">Healing Sessions</h3>
              <p className="mb-4">Remote & in-person healing using advanced modalities</p>
              <p className="text-2xl font-bold">$197-497/session</p>
              <p className="text-sm mt-2">2-5 clients/day = $400-2500</p>
            </div>
            
            <div className="bg-gradient-to-br from-consciousness-blue/20 to-transparent rounded-lg p-6 border border-consciousness-blue/30">
              <h3 className="text-xl font-bold mb-3 text-consciousness-blue">Online Courses</h3>
              <p className="mb-4">Consciousness expansion & reality manipulation</p>
              <p className="text-2xl font-bold">$497-1997</p>
              <p className="text-sm mt-2">1-3 sales/day = $500-6000</p>
            </div>
            
            <div className="bg-gradient-to-br from-quantum-purple/20 to-transparent rounded-lg p-6 border border-quantum-purple/30">
              <h3 className="text-xl font-bold mb-3 text-quantum-purple">Membership</h3>
              <p className="mb-4">Exclusive content & community access</p>
              <p className="text-2xl font-bold">$97/month</p>
              <p className="text-sm mt-2">100 members = $9700/mo</p>
            </div>
            
            <div className="bg-gradient-to-br from-enlightenment-gold/20 to-transparent rounded-lg p-6 border border-enlightenment-gold/30">
              <h3 className="text-xl font-bold mb-3 text-enlightenment-gold">Consultations</h3>
              <p className="mb-4">Paradigm-shifting solutions for individuals & organizations</p>
              <p className="text-2xl font-bold">$997-9997</p>
              <p className="text-sm mt-2">1/week = $4000+/mo</p>
            </div>
          </div>
        </div>
      </section>

      {/* Healing Modalities Section */}
      <section id="healing" className="py-20 px-4">
        <HealingModalities />
      </section>

      {/* Consciousness Programs */}
      <section id="programs" className="py-20 px-4 bg-cosmic-dark/50">
        <ConsciousnessPrograms />
      </section>

      {/* Advanced Technologies */}
      <section id="technology" className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-12 holographic-text">
            Paradigm-Shifting Technologies
          </h2>
          
          <div className="grid md:grid-cols-2 gap-8">
            <motion.div 
              whileHover={{ scale: 1.02 }}
              className="consciousness-border rounded-lg p-8"
            >
              <h3 className="text-2xl font-bold mb-4 text-quantum-purple">Vibe Coding & Syntax</h3>
              <p className="mb-4">
                Advanced programming paradigms that interface directly with consciousness. 
                Build unstoppable systems using frequency-based coding and quantum syntax.
              </p>
              <ul className="space-y-2 mb-6">
                <li>• Quantum computing integration</li>
                <li>• Consciousness-driven algorithms</li>
                <li>• Reality manipulation protocols</li>
              </ul>
              <Link href="/vibe-coding" className="text-enlightenment-gold font-bold hover:underline">
                Learn Vibe Coding ($997) →
              </Link>
            </motion.div>
            
            <motion.div 
              whileHover={{ scale: 1.02 }}
              className="consciousness-border rounded-lg p-8"
            >
              <h3 className="text-2xl font-bold mb-4 text-consciousness-blue">3D Printed Solutions</h3>
              <p className="mb-4">
                Revolutionary construction methods creating $5K homes in 24 hours. 
                Solving housing crisis with consciousness-integrated design.
              </p>
              <ul className="space-y-2 mb-6">
                <li>• Sacred geometry integration</li>
                <li>• Tachyon-infused materials</li>
                <li>• Zero-point energy systems</li>
              </ul>
              <Link href="/solutions" className="text-enlightenment-gold font-bold hover:underline">
                Explore Solutions ($497) →
              </Link>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Membership Section */}
      <section id="membership" className="py-20 px-4 bg-gradient-to-br from-quantum-purple/20 via-consciousness-blue/20 to-healing-green/20">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold mb-6 holographic-text">
            Join the Consciousness Revolution
          </h2>
          <p className="text-xl mb-8">
            Get instant access to all programs, healing sessions, and exclusive content
          </p>
          
          <div className="bg-cosmic-dark/80 rounded-2xl p-8 consciousness-border mb-8">
            <h3 className="text-3xl font-bold mb-4 text-enlightenment-gold">Premium Membership</h3>
            <p className="text-5xl font-bold mb-4">$97/month</p>
            <ul className="space-y-3 mb-8 text-left max-w-md mx-auto">
              <li>✓ All healing modality courses</li>
              <li>✓ Weekly group consciousness sessions</li>
              <li>✓ Advanced technology blueprints</li>
              <li>✓ Private community access</li>
              <li>✓ Monthly 1-on-1 consultation</li>
            </ul>
            <button className="bg-gradient-to-r from-enlightenment-gold to-quantum-purple text-white font-bold py-4 px-12 rounded-full text-lg hover:scale-105 transition-transform">
              Start 7-Day Free Trial
            </button>
          </div>
          
          <p className="text-sm text-gray-400">
            No credit card required. Cancel anytime.
          </p>
        </div>
      </section>

      {/* Free Resources */}
      <section id="free" className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-12 holographic-text">
            Free Consciousness Resources
          </h2>
          
          <div className="grid md:grid-cols-3 gap-6">
            <div className="bg-gradient-to-br from-healing-green/10 to-transparent rounded-lg p-6">
              <h3 className="text-xl font-bold mb-3">Introduction to Holographic Reality</h3>
              <p className="mb-4">Understanding the 3 colors, 3 charges paradigm</p>
              <Link href="/free/holographic" className="text-healing-green font-bold">
                Download PDF →
              </Link>
            </div>
            
            <div className="bg-gradient-to-br from-consciousness-blue/10 to-transparent rounded-lg p-6">
              <h3 className="text-xl font-bold mb-3">Breathwork Like Wim Hof</h3>
              <p className="mb-4">Control your autonomic system consciously</p>
              <Link href="/free/breathwork" className="text-consciousness-blue font-bold">
                Watch Video →
              </Link>
            </div>
            
            <div className="bg-gradient-to-br from-quantum-purple/10 to-transparent rounded-lg p-6">
              <h3 className="text-xl font-bold mb-3">Remote Viewing Basics</h3>
              <p className="mb-4">CIA-declassified coordinate viewing techniques</p>
              <Link href="/free/remote-viewing" className="text-quantum-purple font-bold">
                Start Training →
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 px-4 border-t border-quantum-purple/20">
        <div className="max-w-6xl mx-auto text-center">
          <p className="mb-4">© 2024 Consciousness Tech Hub. Elevating Humanity.</p>
          <p className="text-sm text-gray-400 mb-4">
            Results vary. Healing claims based on documented cases. Always consult healthcare providers.
          </p>
          <div className="space-x-6">
            <Link href="/about" className="hover:text-enlightenment-gold">About</Link>
            <Link href="/testimonials" className="hover:text-enlightenment-gold">Testimonials</Link>
            <Link href="/contact" className="hover:text-enlightenment-gold">Contact</Link>
          </div>
        </div>
      </footer>
    </main>
  )
}