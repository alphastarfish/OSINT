'use client'

import { useState } from 'react'
import emailjs from '@emailjs/browser'

export default function EmailCapture() {
  const [email, setEmail] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [message, setMessage] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsSubmitting(true)
    
    try {
      // Store email in your database here
      // For now, we'll just show a success message
      
      // You can also send yourself an email notification
      // Replace with your EmailJS credentials
      /*
      await emailjs.send(
        'YOUR_SERVICE_ID',
        'YOUR_TEMPLATE_ID',
        {
          email: email,
          to_email: 'your-email@example.com',
        },
        'YOUR_PUBLIC_KEY'
      )
      */
      
      setMessage('Success! Check your email for the free guide.')
      setEmail('')
      
      // In a real app, you'd redirect to a thank you page with the download
      setTimeout(() => {
        window.location.href = '/thank-you'
      }, 2000)
      
    } catch (error) {
      setMessage('Error! Please try again.')
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto">
      <div className="flex flex-col sm:flex-row gap-4">
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Enter your best email"
          className="flex-1 px-4 py-3 rounded-lg text-gray-900 text-lg"
          required
        />
        <button
          type="submit"
          disabled={isSubmitting}
          className="bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-bold py-3 px-6 rounded-lg transition-colors"
        >
          {isSubmitting ? 'Sending...' : 'Get Free Guide'}
        </button>
      </div>
      {message && (
        <p className="mt-4 text-center">{message}</p>
      )}
    </form>
  )
}