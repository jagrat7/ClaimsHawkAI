"use server"; //creates server actions
import { revalidatePath } from "next/cache";
import prisma from "@/utils/db";
import { getKindeServerSession } from "@kinde-oss/kinde-auth-nextjs/server";
import { redirect } from "next/navigation";

export async function createVideo(formData: FormData) {
  const id = formData.get("id") as string;
  const speaker = formData.get("speaker") as string;
  const response = await fetch("http://127.0.0.1:8000/videos/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      id,
      speaker,
    }),
  });
  console.log(response);

  redirect("/admin");
  // USALLY write straight to db here
  // await prisma.videos.create({
  //   data:{
  //     "id":id,
  //     "speaker":speaker
  //   }

  // })
  revalidatePath("/admin")
}