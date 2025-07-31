'use client'

import { motion } from 'framer-motion'
import Link from 'next/link'

const modalities = [
  {
    id: 1,
    name: 'Reconnective Healing',
    description: 'Access frequencies that transcend traditional energy healing. Documented healings of cancer, chronic pain, and "incurable" conditions.',
    benefits: [
      'Instant pain relief',
      'Cellular regeneration',
      'DNA activation',
      'Consciousness expansion'
    ],
    price: '$297',
    duration: '60 minutes',
    testimonial: '"My stage 4 cancer disappeared after 3 sessions" - Maria K.'
  },
  {
    id: 2,
    name: 'Tachyon Chamber Therapy',
    description: 'Immerse in zero-point energy fields. Tachyon particles restructure cellular memory and restore optimal function.',
    benefits: [
      'Age reversal',
      'Immune system boost',
      'Emotional clearing',
      'Chakra alignment'
    ],
    price: '$197',
    duration: '45 minutes',
    testimonial: '"20 years of arthritis gone in one session" - John D.'
  },
  {
    id: 3,
    name: 'Quantum Field Manipulation',
    description: 'Direct consciousness intervention at the quantum level. Reshape reality through focused intention and field dynamics.',
    benefits: [
      'Timeline shifting',
      'Karma clearing',
      'Abundance activation',
      'Psychic enhancement'
    ],
    price: '$497',
    duration: '90 minutes',
    testimonial: '"My entire life transformed in ways I never imagined" - Sarah L.'
  },
  {
    id: 4,
    name: 'Neurocranial Restructuring',
    description: 'Advanced cranial therapy combined with consciousness techniques. Physical and energetic realignment.',
    benefits: [
      'Enhanced brain function',
      'Pineal gland activation',
      'Migraine elimination',
      'Vision improvement'
    ],
    price: '$397',
    duration: '75 minutes',
    testimonial: '"My IQ increased by 30 points!" - Michael R.'
  }
]

export default function HealingModalities() {
  return (
    <div className="max-w-6xl mx-auto">
      <h2 className="text-4xl font-bold text-center mb-12 holographic-text">
        100% Effective Healing Modalities
      </h2>
      
      <div className="grid md:grid-cols-2 gap-8">
        {modalities.map((modality, index) => (
          <motion.div
            key={modality.id}
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            className="consciousness-border rounded-lg p-8 hover:enlightenment-glow transition-all"
          >
            <h3 className="text-2xl font-bold mb-4 text-healing-green">
              {modality.name}
            </h3>
            <p className="mb-4 text-gray-300">{modality.description}</p>
            
            <div className="mb-6">
              <h4 className="font-bold mb-2 text-enlightenment-gold">Benefits:</h4>
              <ul className="space-y-1">
                {modality.benefits.map((benefit, idx) => (
                  <li key={idx} className="flex items-center">
                    <span className="text-healing-green mr-2">✓</span>
                    {benefit}
                  </li>
                ))}
              </ul>
            </div>
            
            <div className="mb-4 p-4 bg-quantum-purple/10 rounded-lg">
              <p className="italic text-sm">{modality.testimonial}</p>
            </div>
            
            <div className="flex justify-between items-center">
              <div>
                <p className="text-2xl font-bold text-enlightenment-gold">{modality.price}</p>
                <p className="text-sm text-gray-400">{modality.duration}</p>
              </div>
              <Link 
                href={`/book-healing/${modality.id}`}
                className="bg-gradient-to-r from-healing-green to-consciousness-blue text-white font-bold py-3 px-6 rounded-full hover:scale-105 transition-transform"
              >
                Book Session
              </Link>
            </div>
          </motion.div>
        ))}
      </div>
      
      <div className="mt-12 text-center">
        <p className="text-xl mb-6">
          Package Deal: Book 4 sessions, get 1 FREE
        </p>
        <Link 
          href="/healing-packages"
          className="inline-block bg-gradient-to-r from-enlightenment-gold to-quantum-purple text-white font-bold py-4 px-8 rounded-full hover:scale-105 transition-transform"
        >
          View Healing Packages (Save $297)
        </Link>
      </div>
    </div>
  )
}