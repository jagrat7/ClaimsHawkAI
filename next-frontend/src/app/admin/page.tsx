import Link from "next/link"

export default async function admin() {
  const response = await fetch('http://127.0.0.1:8000/videos')
  const data =await response.json()
  
  return <div className="text-center pt-32 px-5">
    <h1 className="text-4xl md:text-5xl font-bold mb-5">admin</h1>

    <h2>Videos</h2>
    {data.map(video=>(
      <li key={video.id} className='mb-5'> 
        <Link href={`/admin/${video.id}`}>{video.title}</Link>
      </li>
    )
    )
    }
    
  </div>
}

