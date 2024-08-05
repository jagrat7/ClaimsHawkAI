import { createVideo } from "@/actions/actions";
import { getKindeServerSession } from "@kinde-oss/kinde-auth-nextjs/server";
import { redirect } from 'next/navigation';
import { LogoutLink } from "@kinde-oss/kinde-auth-nextjs/components";

export default async function AdddVideo() {
  // const {isAuthenticated} = getKindeServerSession();
  // if (! (await isAuthenticated()) ) {
  //   redirect("/api/auth/login?redirect_url=/addvideo");
  // }
  return (
    <main>
      <h1 className="text-4xl text-center mt-6 md:text-5xl font-bold mb-5">
        Add Video
      </h1>
      <form
       action={createVideo}
       className="flex flex-col max-w-[400px] mx-auto gap-2 my-10">
        <input
          type="text"
          name="id"
          placeholder="Youtube video ID for new video"
          className="border rounded px-3 h-10"
          required
        />
        <input
          type="text"
          name="speaker"
          placeholder="Speaker for new video"
          className="border rounded px-3 h-10"
          required
        />
        <button className="h-10 bg-black px-5 rounded text-white">
          Submit
        </button>
      </form>

      <LogoutLink><button>Logout</button></LogoutLink>
      {/* {formState?.success && (
        <div className="text-green-600 text-center mt-4">
          Video successfully created!
        </div>
      )}
        {formState?.success === false && (
        <div className="text-red-600 text-center mt-4">
            Failed to create video
        </div>
        )} */}

    </main>
  );
}
