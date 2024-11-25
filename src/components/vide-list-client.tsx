'use client'
import Link from "next/link"
import { useQuery } from "@tanstack/react-query"

interface Video {
  id: string
  title: string
}

const fetchVideos = async () => {
  const response = await fetch("/api/ai/videos/")
  return response.json()
}

export default function VideoListClient({ initialData }: { initialData: Video[] }) {
  const { data, isLoading, error } = useQuery({
    queryKey: ['videos'],
    queryFn: fetchVideos,
  })

  if (isLoading) return <div>Loading videos...</div>
  if (error) return <div>Error loading videos</div>

  return (
    <div>
      <ul>
        {data?.map((video: Video) => (
          <li 
            className="text-left p-3 mb-5 hover:border-2 hover:border-solid rounded-lg" 
            key={video.id}
          >
            <Link href={`/admin/${video.id}`}>{video.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  )
}
