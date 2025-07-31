'use client'

import PricingSection from '@/components/PricingSection'
import { FaCheckCircle } from 'react-icons/fa'
import { motion } from 'framer-motion'

export default function PricingPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <section className="py-16 px-4 sm:px-6 lg:px-8 bg-gradient-to-br from-primary-50 to-purple-50">
        <div className="max-w-7xl mx-auto text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
          >
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
              Choose Your Career Success Plan
            </h1>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">
              Join thousands of professionals who've landed their dream jobs. 
              Start free and upgrade when you're ready.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Pricing Cards */}
      <PricingSection />

      {/* FAQs */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">Frequently Asked Questions</h2>
          
          <div className="space-y-6">
            {faqs.map((faq, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                viewport={{ once: true }}
                className="bg-white rounded-lg shadow-md p-6"
              >
                <h3 className="text-lg font-semibold mb-2">{faq.question}</h3>
                <p className="text-gray-600">{faq.answer}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Money Back Guarantee */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-primary-600 text-white">
        <div className="max-w-4xl mx-auto text-center">
          <FaCheckCircle className="text-6xl mx-auto mb-6" />
          <h2 className="text-3xl font-bold mb-4">30-Day Money-Back Guarantee</h2>
          <p className="text-xl text-primary-100 mb-8">
            Try ResumeAI risk-free. If you're not completely satisfied within 30 days, 
            we'll give you a full refund. No questions asked.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <div className="bg-primary-700 rounded-lg p-4">
              <p className="font-semibold">✓ Cancel anytime</p>
            </div>
            <div className="bg-primary-700 rounded-lg p-4">
              <p className="font-semibold">✓ No hidden fees</p>
            </div>
            <div className="bg-primary-700 rounded-lg p-4">
              <p className="font-semibold">✓ Instant refunds</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

const faqs = [
  {
    question: "Can I try ResumeAI before purchasing?",
    answer: "Yes! Our free plan allows you to create and download up to 3 resumes with basic templates and AI assistance. This gives you a chance to experience our platform before committing to a paid plan."
  },
  {
    question: "What's included in the AI assistance?",
    answer: "Our AI helps you write compelling bullet points, optimize for ATS keywords, generate professional summaries, and tailor your resume to specific job descriptions. The AI learns from successful resumes in your industry."
  },
  {
    question: "Can I cancel my subscription anytime?",
    answer: "Absolutely! You can cancel your subscription at any time from your account settings. You'll continue to have access until the end of your billing period, and we offer a 30-day money-back guarantee."
  },
  {
    question: "What file formats can I export?",
    answer: "Free users can export to PDF. Professional and Career Pro subscribers can export to PDF, Microsoft Word (.docx), and plain text formats. All formats are optimized for ATS systems."
  },
  {
    question: "Do you offer student discounts?",
    answer: "Yes! Students with a valid .edu email address receive 50% off any paid plan. Simply sign up with your student email to automatically receive the discount."
  },
  {
    question: "What makes Career Pro worth the extra cost?",
    answer: "Career Pro includes personalized 1-on-1 coaching sessions, interview preparation, salary negotiation strategies, and custom resume templates. Our coaches have helped clients increase their salaries by an average of $20,000."
  }
]