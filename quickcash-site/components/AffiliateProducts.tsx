'use client'

import Image from 'next/image'
import Link from 'next/link'

// High-converting affiliate products with good commissions
const products = [
  {
    id: 1,
    name: 'ClickFunnels - Sales Funnel Builder',
    description: 'Build high-converting sales funnels in minutes. Perfect for selling anything online.',
    price: '$97/month',
    commission: '$38.80 recurring',
    image: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400',
    affiliateLink: 'https://www.clickfunnels.com/?cf_affiliate_id=YOUR_ID',
    rating: 4.8,
    urgency: 'Limited Time: 30-Day Free Trial'
  },
  {
    id: 2,
    name: 'Legendary Marketer - Online Business Training',
    description: 'Learn affiliate marketing from experts. Earn up to $2,500 per sale!',
    price: '$7 trial',
    commission: 'Up to $2,500',
    image: 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=400',
    affiliateLink: 'https://legendarymarketer.com/?affiliate=YOUR_ID',
    rating: 4.7,
    urgency: 'Flash Sale: 90% Off Today Only'
  },
  {
    id: 3,
    name: 'Bluehost Web Hosting',
    description: 'Start your money-making website for just $2.95/month. Essential for any online business.',
    price: '$2.95/month',
    commission: '$65 per sale',
    image: 'https://images.unsplash.com/photo-1484417894907-623942c8ee29?w=400',
    affiliateLink: 'https://www.bluehost.com/track/YOUR_ID',
    rating: 4.5,
    urgency: 'Special: Free Domain Included'
  },
  {
    id: 4,
    name: 'ConvertKit - Email Marketing',
    description: 'Build your email list and make money on autopilot. Free for up to 1,000 subscribers.',
    price: 'Free to start',
    commission: '$30 recurring',
    image: 'https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400',
    affiliateLink: 'https://convertkit.com?lmref=YOUR_ID',
    rating: 4.9,
    urgency: 'Bonus: Free Email Templates'
  },
  {
    id: 5,
    name: 'Teachable - Course Platform',
    description: 'Create and sell online courses. Keep 97% of your revenue!',
    price: '$39/month',
    commission: '$30 recurring',
    image: 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400',
    affiliateLink: 'https://teachable.com?affiliate=YOUR_ID',
    rating: 4.6,
    urgency: 'New: AI Course Builder Included'
  },
  {
    id: 6,
    name: 'Shopify - E-commerce Platform',
    description: 'Start dropshipping or sell your own products. Make money while you sleep!',
    price: '$1 for 3 months',
    commission: '$58 average',
    image: 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=400',
    affiliateLink: 'https://www.shopify.com/?ref=YOUR_ID',
    rating: 4.8,
    urgency: 'Limited Offer: $1 Trial'
  }
]

export default function AffiliateProducts() {
  return (
    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      {products.map((product) => (
        <div key={product.id} className="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
          <div className="relative h-48">
            <Image
              src={product.image}
              alt={product.name}
              fill
              className="object-cover"
            />
            <div className="absolute top-2 right-2 bg-red-600 text-white px-3 py-1 rounded-full text-sm font-bold">
              {product.urgency}
            </div>
          </div>
          
          <div className="p-6">
            <h3 className="text-xl font-bold mb-2">{product.name}</h3>
            <p className="text-gray-600 mb-4">{product.description}</p>
            
            <div className="flex items-center mb-4">
              <div className="flex text-yellow-400">
                {'★'.repeat(Math.floor(product.rating))}
              </div>
              <span className="ml-2 text-sm text-gray-500">({product.rating})</span>
            </div>
            
            <div className="mb-4">
              <p className="text-2xl font-bold text-money-green">{product.price}</p>
              <p className="text-sm text-gray-600">Earn: <span className="font-bold text-green-600">{product.commission}</span></p>
            </div>
            
            <a
              href={product.affiliateLink}
              target="_blank"
              rel="noopener noreferrer"
              className="money-button block text-center w-full"
            >
              Get Started Now →
            </a>
            
            <p className="text-xs text-center mt-2 text-gray-500">
              Affiliate disclosure: We earn commission at no cost to you
            </p>
          </div>
        </div>
      ))}
    </div>
  )
}