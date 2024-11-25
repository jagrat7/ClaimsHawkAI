'use server'

import { revalidatePath } from 'next/cache'

export async function fetchVideos() {
  const response = await fetch("/api/ai/videos", {
    headers: {
      'Content-Type': 'application/json',
    },
  })

  if (!response.ok) {
    throw new Error('Failed to fetch videos')
  }

  const videos = await response.json()
  
  // Revalidate the admin page to reflect any changes
  revalidatePath('/admin')

  return videos
}

