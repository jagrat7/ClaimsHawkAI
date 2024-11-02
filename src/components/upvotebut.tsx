"use client";
import { useState } from "react";

export default function Upvotebut() {
  const [count, setcount] = useState(0);
  return (
    <button
      onClick={()=>setcount(count + 1)}
      className="mt-5 bg-black text-white px-4 py-2 rounded"
    >
      poop x {count}
    </button>
  );
}
