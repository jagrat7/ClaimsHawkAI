import { prisma } from "@/server/db";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import Link from "next/link";
import { GenerateButton } from "./generateButton";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button";
import { ChevronLeft } from "lucide-react";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { cn } from "@/lib/utils"

export default async function VideoPage(
  props: {
    params: Promise<{ id: string }>;
  }
) {
  const params = await props.params;

  const response = await fetch(`http://127.0.0.1:8000/videos/${params.id}`, { next: { revalidate: 1 } });
  const data = await response.json();
  const claims = await prisma.claims.findMany({
    where: { video_id: params.id },
  });

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <Link href="/admin">
          <Button variant="ghost" className="text-primary hover:text-primary/80 hover:bg-primary/10">
            <ChevronLeft className="mr-2 h-4 w-4" />
            Back to Admin
          </Button>
        </Link>
      </div>

      <div className="space-y-8">
        <div>
          <h1 className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-primary to-primary/60 text-transparent bg-clip-text">
            {data.title}
          </h1>
        </div>

        <Table>
          <TableBody>
            <TableRow>
              <TableHead className="text-right">ID</TableHead>
              <TableCell>{data.id}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead className="text-right">Description</TableHead>
              <TableCell>{data.description || data.title}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead className="text-right">Processed</TableHead>
              <TableCell>{data.processed ? "Yes" : "No"}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead className="text-right">Captions Location</TableHead>
              <TableCell>{data.captions_location || "N/A"}</TableCell>
            </TableRow>
            <TableRow>
              <TableHead className="text-right">Date Published</TableHead>
              <TableCell>
                {data.date_published ? new Date(data.date_published).toLocaleString() : "N/A"}
              </TableCell>
            </TableRow>
          </TableBody>
        </Table>

        <div className="space-y-4">
          <h2 className="text-2xl font-semibold text-primary/80">Claims</h2>
          {claims.length <= 0 ? (
            <GenerateButton videoId={params.id} />
          ) : (
            <ul className="grid gap-3">
              {claims.map((claim) => (
                <li 
                  key={claim.id} 
                  className={cn(
                    "p-6 rounded-lg",
                    "bg-gradient-to-r from-primary/5 to-secondary/50",
                    "border border-primary/30",
                    "shadow-lg shadow-primary/5",
                    "relative overflow-hidden",
                    "transition-all duration-300",
                    "hover:shadow-primary/20 hover:border-primary/50",
                    "hover:from-primary/10 hover:to-secondary/60"
                  )}
                >
                  <div className="absolute top-0 left-0 w-1 h-full bg-primary/40" />
                  <p className="relative z-10 text-foreground/90">{claim.claim}</p>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}
