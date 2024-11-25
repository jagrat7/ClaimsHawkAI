import VideoList from "@/components/videolist"
import Link from "next/link"
import { Suspense } from "react"

export default function AdminPage() {
  return (
    <div className="text-center pt-32 px-5">
      <h1 className="text-4xl md:text-5xl font-bold mb-5">Admin panel</h1>

      <h2 className="text-3xl text-left md:text-3xl font-bold mb-5 mt-9">Videos</h2>
      <Link
        href="/addvideo"
        className="flex items-center mb-5 text-black hover:underline"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-5 w-5 mr-2"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fillRule="evenodd"
            d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z"
            clipRule="evenodd"
          />
        </svg>
        Add New Video
      </Link>
      <VideoList />
    </div>
  )
}

