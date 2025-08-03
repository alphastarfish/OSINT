'use client'

import { motion } from 'framer-motion'
import Link from 'next/link'

const programs = [
  {
    id: 1,
    name: 'Remote Viewing Mastery',
    level: 'Beginner to Advanced',
    description: 'Learn CIA-declassified coordinate remote viewing. Access any information across space and time.',
    modules: [
      'Stage 1-6 CRV Protocol',
      'Associative Remote Viewing',
      'Future Timeline Access',
      'Target Acquisition Mastery'
    ],
    price: '$497',
    bonuses: ['Private Discord Community', 'Weekly Practice Sessions', 'Target Database Access'],
    students: 1247,
    rating: 4.9
  },
  {
    id: 2,
    name: 'Autonomic System Control',
    level: 'Intermediate',
    description: 'Master your body like Wim Hof. Control temperature, eliminate disease, superhuman endurance.',
    modules: [
      'Conscious Breathing Techniques',
      'Cold/Heat Resistance',
      'Immune System Programming',
      'Pain Elimination Protocols'
    ],
    price: '$697',
    bonuses: ['Live Monthly Q&A', 'Biometric Tracking App', 'Personal Progress Coach'],
    students: 892,
    rating: 4.8
  },
  {
    id: 3,
    name: 'Holographic Reality Coding',
    level: 'Advanced',
    description: 'Understand the 3 colors, 3 charges paradigm. Manipulate reality at the fundamental level.',
    modules: [
      'Photonic Consciousness Theory',
      'Language Deprogramming',
      'Reality Matrix Navigation',
      'Manifestation Algorithms'
    ],
    price: '$997',
    bonuses: ['Source Code Access', 'Reality Hacking Tools', '1-on-1 Mentorship'],
    students: 476,
    rating: 5.0
  },
  {
    id: 4,
    name: 'Vibe Coding & Quantum Syntax',
    level: 'Expert',
    description: 'Build unstoppable systems using consciousness-driven programming. Interface with T.Y.L.E.R. protocols.',
    modules: [
      'Frequency-Based Coding',
      'Quantum Algorithm Design',
      'Consciousness API Integration',
      'Botnet Defense Systems'
    ],
    price: '$1997',
    bonuses: ['Private GitHub Repo', 'Quantum Computing Credits', 'NSA-Level Encryption'],
    students: 139,
    rating: 5.0
  }
]

export default function ConsciousnessPrograms() {
  return (
    <div className="max-w-6xl mx-auto">
      <h2 className="text-4xl font-bold text-center mb-12 holographic-text">
        Consciousness Expansion Programs
      </h2>
      
      <div className="grid md:grid-cols-2 gap-8">
        {programs.map((program, index) => (
          <motion.div
            key={program.id}
            initial={{ opacity: 0, x: index % 2 === 0 ? -20 : 20 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.1 }}
            className="consciousness-border rounded-lg p-8 hover:enlightenment-glow transition-all"
          >
            <div className="flex justify-between items-start mb-4">
              <div>
                <h3 className="text-2xl font-bold text-consciousness-blue">
                  {program.name}
                </h3>
                <p className="text-sm text-gray-400">{program.level}</p>
              </div>
              <div className="text-right">
                <div className="flex items-center text-enlightenment-gold">
                  {'★'.repeat(Math.floor(program.rating))}
                  <span className="ml-1 text-sm">({program.rating})</span>
                </div>
                <p className="text-xs text-gray-400">{program.students} students</p>
              </div>
            </div>
            
            <p className="mb-4 text-gray-300">{program.description}</p>
            
            <div className="mb-6">
              <h4 className="font-bold mb-2 text-quantum-purple">Course Modules:</h4>
              <ul className="space-y-1 text-sm">
                {program.modules.map((module, idx) => (
                  <li key={idx} className="flex items-center">
                    <span className="text-consciousness-blue mr-2">▸</span>
                    {module}
                  </li>
                ))}
              </ul>
            </div>
            
            <div className="mb-6 p-4 bg-enlightenment-gold/10 rounded-lg">
              <h4 className="font-bold mb-2 text-enlightenment-gold">Exclusive Bonuses:</h4>
              <ul className="text-sm space-y-1">
                {program.bonuses.map((bonus, idx) => (
                  <li key={idx}>• {bonus}</li>
                ))}
              </ul>
            </div>
            
            <div className="flex justify-between items-center">
              <p className="text-3xl font-bold text-enlightenment-gold">{program.price}</p>
              <Link 
                href={`/enroll/${program.id}`}
                className="bg-gradient-to-r from-consciousness-blue to-quantum-purple text-white font-bold py-3 px-6 rounded-full hover:scale-105 transition-transform"
              >
                Enroll Now
              </Link>
            </div>
          </motion.div>
        ))}
      </div>
      
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        className="mt-12 text-center bg-gradient-to-r from-quantum-purple/20 to-consciousness-blue/20 rounded-2xl p-8"
      >
        <h3 className="text-2xl font-bold mb-4">
          🎓 Complete Consciousness Mastery Bundle
        </h3>
        <p className="text-xl mb-6">
          Get ALL 4 programs + exclusive bonuses
        </p>
        <p className="text-4xl font-bold text-enlightenment-gold mb-2">
          $2,497 <span className="text-xl text-gray-400 line-through">$4,188</span>
        </p>
        <p className="text-sm text-gray-400 mb-6">Save $1,691 - Limited Time Offer</p>
        <Link 
          href="/consciousness-bundle"
          className="inline-block bg-gradient-to-r from-enlightenment-gold to-healing-green text-cosmic-dark font-bold py-4 px-8 rounded-full hover:scale-105 transition-transform"
        >
          Get The Complete Bundle
        </Link>
      </motion.div>
    </div>
  )
}