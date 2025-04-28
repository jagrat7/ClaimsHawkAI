import VideoList from "@/components/videolist"
import { Suspense } from "react"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { AddVideoDialog } from "@/components/add-video-dialog"

export default function AdminPage() {
  return (
    <div className="container mx-auto px-4 py-16">
      <div className="space-y-8">
        <div className="text-center">
          <h1 className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-primary to-primary/60 text-transparent bg-clip-text">
            Admin Panel
          </h1>
        </div>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between">
            <CardTitle className="text-2xl">Videos</CardTitle>
            <AddVideoDialog />
          </CardHeader>
          <CardContent>
            <VideoList />
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

