'use client'

import { motion } from 'framer-motion'
import { FaCheck, FaCrown, FaRocket } from 'react-icons/fa'
import Link from 'next/link'

export default function PricingSection() {
  return (
    <section id="pricing" className="py-20 px-4 sm:px-6 lg:px-8 bg-gray-50">
      <div className="max-w-7xl mx-auto">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
          viewport={{ once: true }}
          className="text-center mb-12"
        >
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Simple, Transparent Pricing
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Choose the perfect plan for your career journey. All plans include AI assistance.
          </p>
        </motion.div>

        <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          {plans.map((plan, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              viewport={{ once: true }}
              className={`relative rounded-2xl p-8 ${
                plan.featured
                  ? 'bg-gradient-to-br from-primary-600 to-purple-600 text-white shadow-2xl scale-105'
                  : 'bg-white shadow-lg'
              }`}
            >
              {plan.featured && (
                <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                  <span className="bg-yellow-400 text-gray-900 px-4 py-1 rounded-full text-sm font-semibold inline-flex items-center gap-1">
                    <FaCrown /> MOST POPULAR
                  </span>
                </div>
              )}

              <div className="text-center mb-8">
                <h3 className={`text-2xl font-bold mb-2 ${plan.featured ? 'text-white' : 'text-gray-900'}`}>
                  {plan.name}
                </h3>
                <div className="mb-4">
                  <span className={`text-4xl font-bold ${plan.featured ? 'text-white' : 'text-gray-900'}`}>
                    ${plan.price}
                  </span>
                  {plan.price > 0 && (
                    <span className={`${plan.featured ? 'text-primary-100' : 'text-gray-600'}`}>
                      /{plan.period}
                    </span>
                  )}
                </div>
                <p className={`${plan.featured ? 'text-primary-100' : 'text-gray-600'}`}>
                  {plan.description}
                </p>
              </div>

              <ul className="space-y-3 mb-8">
                {plan.features.map((feature, idx) => (
                  <li key={idx} className="flex items-start gap-3">
                    <FaCheck className={`flex-shrink-0 mt-1 ${plan.featured ? 'text-primary-100' : 'text-primary-600'}`} />
                    <span className={`${plan.featured ? 'text-white' : 'text-gray-700'}`}>
                      {feature}
                    </span>
                  </li>
                ))}
              </ul>

              <Link
                href="/signup"
                className={`block text-center py-3 px-6 rounded-lg font-semibold transition-all duration-200 ${
                  plan.featured
                    ? 'bg-white text-primary-600 hover:bg-gray-100'
                    : 'bg-primary-600 text-white hover:bg-primary-700'
                }`}
              >
                {plan.cta}
              </Link>
            </motion.div>
          ))}
        </div>

        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.5, delay: 0.4 }}
          viewport={{ once: true }}
          className="text-center mt-12"
        >
          <p className="text-gray-600">
            All plans include 30-day money-back guarantee • Cancel anytime • Secure payment
          </p>
        </motion.div>
      </div>
    </section>
  )
}

const plans = [
  {
    name: 'Starter',
    price: 0,
    period: 'forever',
    description: 'Perfect for trying out our service',
    features: [
      '3 resume downloads',
      'Basic templates',
      'AI content suggestions',
      'PDF export only',
      'Email support'
    ],
    cta: 'Start Free',
    featured: false
  },
  {
    name: 'Professional',
    price: 19,
    period: 'month',
    description: 'For active job seekers',
    features: [
      'Unlimited resumes',
      'All premium templates',
      'Advanced AI optimization',
      'PDF, Word, TXT exports',
      'Cover letter builder',
      'LinkedIn optimization',
      'Priority support',
      'Resume tracking'
    ],
    cta: 'Get Started',
    featured: true
  },
  {
    name: 'Career Pro',
    price: 49,
    period: 'month',
    description: 'For career professionals',
    features: [
      'Everything in Professional',
      'Personal career coach',
      'Interview preparation',
      'Salary negotiation tips',
      'Job search strategy',
      'Weekly 1-on-1 calls',
      'Custom templates',
      'White-label options'
    ],
    cta: 'Level Up',
    featured: false
  }
]