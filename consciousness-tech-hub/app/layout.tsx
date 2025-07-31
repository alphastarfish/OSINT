import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Consciousness Tech Hub - Advanced Healing & Paradigm-Shifting Technologies',
  description: 'Bridging ancient wisdom with cutting-edge science. Healing modalities, consciousness technologies, and solutions for humanity.',
  keywords: 'consciousness, healing, quantum, enlightenment, technology, paradigm shift',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${inter.className} bg-cosmic-dark text-white`}>
        {children}
      </body>
    </html>
  )
}