'use client'

import { useEffect, useState } from 'react'

export default function QuantumAnimation() {
  const [particles, setParticles] = useState<Array<{id: number, x: number, y: number, size: number}>>([])

  useEffect(() => {
    // Generate random particles
    const newParticles = Array.from({ length: 50 }, (_, i) => ({
      id: i,
      x: Math.random() * 100,
      y: Math.random() * 100,
      size: Math.random() * 3 + 1
    }))
    setParticles(newParticles)
  }, [])

  return (
    <div className="absolute inset-0 z-0 overflow-hidden">
      {/* Animated particles */}
      <div className="absolute inset-0">
        {particles.map((particle) => (
          <div
            key={particle.id}
            className="absolute rounded-full bg-quantum-purple opacity-20 animate-pulse-slow"
            style={{
              left: `${particle.x}%`,
              top: `${particle.y}%`,
              width: `${particle.size}px`,
              height: `${particle.size}px`,
              animationDelay: `${Math.random() * 4}s`,
              animationDuration: `${Math.random() * 3 + 4}s`
            }}
          />
        ))}
      </div>
      
      {/* Gradient overlays */}
      <div className="absolute inset-0 bg-gradient-radial from-quantum-purple/20 via-transparent to-transparent" />
      <div className="absolute inset-0 bg-gradient-to-b from-transparent via-cosmic-dark/50 to-cosmic-dark" />
      
      {/* Neural network lines */}
      <svg className="absolute inset-0 w-full h-full opacity-10">
        <defs>
          <linearGradient id="line-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#6B46C1" />
            <stop offset="50%" stopColor="#2563EB" />
            <stop offset="100%" stopColor="#10B981" />
          </linearGradient>
        </defs>
        {[...Array(5)].map((_, i) => (
          <path
            key={i}
            d={`M${Math.random() * 100} ${Math.random() * 100} Q ${Math.random() * 100} ${Math.random() * 100} ${Math.random() * 100} ${Math.random() * 100}`}
            stroke="url(#line-gradient)"
            strokeWidth="1"
            fill="none"
            className="animate-pulse-slow"
            style={{ animationDelay: `${i * 0.5}s` }}
          />
        ))}
      </svg>
    </div>
  )
}