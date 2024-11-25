'use client'

import { useState, useEffect } from 'react'
import Link from "next/link"

interface Video {
  id: string
  title: string
  // Add other properties as needed
}

export default function VideoList() {
  const [videos, setVideos] = useState<Video[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    async function fetchVideos() {
      try {
        const response = await fetch("/api/ai/videos", {
          next: { revalidate: 1 },
        })
        if (!response.ok) {
          throw new Error('Failed to fetch videos')
        }
        const data = await response.json()
        setVideos(data)
      } catch (err) {
        console.error('Error fetching videos:', err)
        setError('Failed to load videos. Please try again later.')
      } finally {
        setIsLoading(false)
      }
    }

    fetchVideos()
  }, [])

  if (isLoading) return <div>Loading...</div>
  if (error) return <div className="text-red-500">{error}</div>

  return (
    <div>
      <ul>
        {videos.map((video) => (
          <li className="text-left p-3 mb-5 hover:border-2 hover:border-solid rounded-lg" key={video.id}>
            <Link href={`/admin/${video.id}`}>{video.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  )
}

