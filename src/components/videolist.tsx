import Link from "next/link";
import prisma from "@/utils/db";
export default async function VideoList() {
  await new Promise((resolve) => setTimeout(resolve, 1000));

  // const response = await fetch("http://127.0.0.1:8000/videos/", {
  //   next: { revalidate: 1 },
  // });
  // const data = await response.json();

  const data = await prisma.videos.findMany()
  return (
    <div>
      <ul>
        {data.map((video) => (
          <li className="text-left p-3 mb-5 hover:border-2 hover:border-solid rounded-lg " key={video.id}>
          <Link href={`/admin/${video.id}`}>{video.title}</Link>
          </li>
        ))}
      </ul>{" "}
    </div>
  );
}
