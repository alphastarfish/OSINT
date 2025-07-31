'use client'

interface AdBannerProps {
  position: 'top' | 'middle' | 'bottom'
}

export default function AdBanner({ position }: AdBannerProps) {
  // Different ad sizes for different positions
  const adConfig = {
    top: { width: 728, height: 90, slot: '1234567890' },
    middle: { width: 336, height: 280, slot: '0987654321' },
    bottom: { width: 728, height: 90, slot: '1122334455' }
  }

  const config = adConfig[position]

  return (
    <div className="flex justify-center my-8">
      <div 
        className="bg-gray-100 border-2 border-dashed border-gray-300 flex items-center justify-center"
        style={{ width: config.width, height: config.height }}
      >
        {/* Replace this with your actual ad code */}
        <div className="text-center p-4">
          <p className="text-gray-500 text-sm">Advertisement</p>
          <p className="text-xs text-gray-400">
            {config.width}x{config.height}
          </p>
          {/* Google AdSense code would go here */}
          {/* <ins className="adsbygoogle"
               style={{ display: 'block' }}
               data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
               data-ad-slot={config.slot}
               data-ad-format="auto"
               data-full-width-responsive="true">
          </ins> */}
        </div>
      </div>
    </div>
  )
}