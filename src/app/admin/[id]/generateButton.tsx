"use client"
import { revalidatePath } from 'next/cache';
import { useState } from 'react';

export function GenerateButton ({ videoId }: { videoId: string }) 
{
  const [isGenerating, setIsGenerating] = useState(false);
  const [generationError, setGenerationError] = useState(null);

  const handleClick = async () => {
    setIsGenerating(true);
    setGenerationError(null);

    try {
      const response = await fetch(`http://localhost:8000/extract_claims/${videoId}`, {
        method: 'POST' 
      });

      if (!response.ok) {
        const errorData = await response.json();
        // throw new Error(errorData.message || 'Failed to extract claims');
      }

      // Assuming your API returns a success message
      const data = await response.json();
      console.log(data.message); // Log the success message
      revalidatePath(`admin/${videoId}`)
    } catch (error:any) {
      setGenerationError(error.message);
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div>
      <button
        onClick={handleClick}
        className="mt-5 bg-black text-white px-4 py-2 rounded-sm"
        disabled={isGenerating}
      >
        {isGenerating ? 'Generating...' : 'Generate Claims'}
      </button>
      {generationError && (
        <p className="text-red-500 mt-2">{generationError}</p>
      )}
    </div>
  );
};

