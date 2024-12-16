import Upvotebut from "@/components/upvotebut";
import prisma from "@/utils/db";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import { GenerateButton } from "./generateButton";

export default async function VideoPage({
  params,
}: {
  params: { id: string };
}) {

  const response = await fetch(`http://127.0.0.1:8000/videos/${params.id}` ,{ next: { revalidate: 1 } });
  const data = await response.json();
  const claims = await prisma.claims.findMany({
    where: { video_id: params.id },
  });
  console.log(claims);

  return (
    <div className="text-center pt-32 px-5">
      <h1 className="text-4xl md:text-5xl font-bold mb-5">{data.title}</h1>
      <div className="text-left">
        <p className="mb-2">
          <strong>ID:</strong> {data.id}
        </p>
        <p className="mb-2">
          <strong>Description:</strong> {data.title}
        </p>
        <p className="mb-2">
          <strong>Processed:</strong> {data.processed ? "Yes" : "No"}
        </p>
        <p className="mb-2">
          <strong>Captions Location:</strong> {data.captions_location || "N/A"}
        </p>
        <p className="mb-2">
          <strong>Date Published:</strong>{" "}
          {data.date_published
            ? new Date(data.date_published).toLocaleString()
            : "N/A"}
        </p>
        <p className="mb-2">
          <strong>Created At:</strong>{" "}
          {data.created_at ? new Date(data.created_at).toLocaleString() : "N/A"}
        </p>
        <p className="mb-2">
          <strong>Updated At:</strong>{" "}
          {data.updated_at ? new Date(data.updated_at).toLocaleString() : "N/A"}
        </p>
      </div>

      <section className="text-left mt-10">
        <h1 className="text-4xl md:text-5xl font-bold mb-5">Claims</h1>
        <ul>
          {claims.length <= 0 ? (
            <GenerateButton videoId={params.id} />
          ) : (
            claims.map((claim) => <li key={claim.id}>{claim.claim}</li>)
          )}
        </ul>
      </section>
    </div>
  );
}

// console.log(params);
// const { params: { id } } = params;
// console.log(id);

// const response = await fetch(`http://127.0.0.1:8000/videos/${params.id}` ,{ next: { revalidate: 1 } });
// const data = await response.json();
