'use client'

import { useState, useEffect } from 'react'
import Link from "next/link"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Skeleton } from "@/components/ui/skeleton"

interface Video {
  id: string
  title: string
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

  if (isLoading) return (
    <div className="space-y-3">
      <Skeleton className="h-[125px] w-full rounded-xl" />
      <Skeleton className="h-[125px] w-full rounded-xl" />
      <Skeleton className="h-[125px] w-full rounded-xl" />
    </div>
  )
  
  if (error) return (
    <Card className="border-destructive">
      <CardContent className="pt-6">
        <p className="text-destructive">{error}</p>
      </CardContent>
    </Card>
  )

  return (
    <div className="space-y-4">
      {videos.map((video) => (
        <Card 
          key={video.id}
          className="transition-all hover:shadow-lg hover:border-primary"
        >
          <CardHeader className="p-4">
            <Link href={`/admin/${video.id}`}>
              <CardTitle className="text-lg hover:text-primary">{video.title}</CardTitle>
            </Link>
          </CardHeader>
        </Card>
      ))}
    </div>
  )
}

