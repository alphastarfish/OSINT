'use client'

import { motion } from 'framer-motion'
import Link from 'next/link'
import { FaRocket, FaFileAlt, FaMagic, FaDownload, FaChartLine, FaShieldAlt } from 'react-icons/fa'
import PricingSection from '@/components/PricingSection'
import TestimonialsSection from '@/components/TestimonialsSection'

export default function HomePage() {
  return (
    <div className="overflow-hidden">
      {/* Hero Section */}
      <section className="relative py-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-br from-primary-50 to-purple-50">
        <div className="max-w-7xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="text-center"
          >
            <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
              Build Your Dream Resume with <span className="gradient-text">AI Power</span>
            </h1>
            <p className="text-xl md:text-2xl text-gray-600 mb-8 max-w-3xl mx-auto">
              Create professional, ATS-optimized resumes in minutes. Let AI help you craft compelling content that gets you hired.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link href="/signup" className="btn-primary inline-flex items-center gap-2">
                <FaRocket /> Start Building Free
              </Link>
              <Link href="#pricing" className="btn-secondary inline-flex items-center gap-2">
                View Pricing
              </Link>
            </div>
            <p className="mt-4 text-sm text-gray-500">No credit card required • 3 free resumes</p>
          </motion.div>

          {/* Hero Image */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="mt-12"
          >
            <div className="relative rounded-2xl shadow-2xl overflow-hidden bg-white p-8">
              <img
                src="https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=1200&h=600&fit=crop"
                alt="Resume Builder Interface"
                className="rounded-lg"
              />
            </div>
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            transition={{ duration: 0.5 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              Everything You Need to Land Your Dream Job
            </h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Our AI-powered platform provides all the tools you need to create stunning resumes
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                viewport={{ once: true }}
                className="card"
              >
                <feature.icon className="text-4xl text-primary-600 mb-4" />
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-primary-600 text-white">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8 text-center">
            {stats.map((stat, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, scale: 0.9 }}
                whileInView={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                viewport={{ once: true }}
              >
                <div className="text-4xl font-bold mb-2">{stat.value}</div>
                <div className="text-primary-100">{stat.label}</div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <TestimonialsSection />

      {/* Pricing Section */}
      <PricingSection />

      {/* CTA Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-r from-primary-600 to-purple-600 text-white">
        <div className="max-w-4xl mx-auto text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl font-bold mb-4">
              Ready to Land Your Dream Job?
            </h2>
            <p className="text-xl mb-8 text-primary-100">
              Join thousands of job seekers who've successfully landed interviews with our AI-powered resumes
            </p>
            <Link href="/signup" className="bg-white text-primary-600 px-8 py-4 rounded-lg hover:bg-gray-100 transition-colors duration-200 font-semibold text-lg inline-flex items-center gap-2">
              <FaRocket /> Get Started Now - It's Free
            </Link>
          </motion.div>
        </div>
      </section>
    </div>
  )
}

const features = [
  {
    icon: FaMagic,
    title: 'AI-Powered Content',
    description: 'Generate compelling bullet points and summaries tailored to your target job with advanced AI.'
  },
  {
    icon: FaFileAlt,
    title: 'Professional Templates',
    description: 'Choose from dozens of ATS-optimized templates designed by HR professionals.'
  },
  {
    icon: FaChartLine,
    title: 'ATS Optimization',
    description: 'Ensure your resume passes through Applicant Tracking Systems with our optimization tools.'
  },
  {
    icon: FaDownload,
    title: 'Multiple Formats',
    description: 'Download your resume in PDF, Word, or plain text formats for any application.'
  },
  {
    icon: FaShieldAlt,
    title: 'Privacy First',
    description: 'Your data is encrypted and secure. We never share your information with third parties.'
  },
  {
    icon: FaRocket,
    title: 'Fast & Easy',
    description: 'Create a professional resume in under 10 minutes with our intuitive builder.'
  }
]

const stats = [
  { value: '50,000+', label: 'Resumes Created' },
  { value: '92%', label: 'Interview Rate' },
  { value: '4.9/5', label: 'User Rating' },
  { value: '$75k', label: 'Avg Salary Increase' }
]