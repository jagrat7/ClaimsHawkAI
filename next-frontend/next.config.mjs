/** @type {import('next').NextConfig} */
const nextConfig = async () => {
  return {
    images: {
      remotePatterns: [
        {
          protocol: "https",
          hostname: "bytegrad.com",
        },
      ],
    },
    rewrites: async () => [
      {
        source: "/api/fastapi/:path*",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8000/api/fastapi/:path*"
            : "/api/",
      },
      {
        source: "/docs",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8000/docs"
            : "/api/docs",
      },
      {
        source: "/openapi.json",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8000/openapi.json"
            : "/api/openapi.json",
      },
    ],
  };
};

export default nextConfig;
