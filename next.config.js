/** @type {import('next').NextConfig} */
const nextConfig = {
      images: {
      remotePatterns: [
        {
          protocol: "https",
          hostname: "bytegrad.com",
        },
      ],
    },
    async rewrites() {
    return [
      {
        source: '/api/ai/:path*',
        destination: 'http://127.0.0.1:8000/:path*',
      },
    ]
  },
}

module.exports = nextConfig

