import Image from "next/image";
import logo from "../../public/images/claimshawk_logo_with_transparent_background_more_robotic.jpeg"
export default function Home() {
  return (
    <main className="text-center pt-32 px-5">
      <h1 className="text-4xl md:text-5xl font-bold mb-5" >ClaimsHawk</h1>
      <p>
        Subtly Hawk tauhing on useless politicians. 
      </p>
      <div className="flex flex-col items-center gap-10 pt-9">
        <Image
          src={logo}
          alt="ClaimsHawk Logo with Transparent Background (More Robotic)"
          width={400}
          height={400}
          style={{
            maskImage: 'radial-gradient(circle, black 50%, transparent 70%)',
            WebkitMaskImage: 'radial-gradient(circle, black 50%, transparent 70%)'
          }}
        />
      </div>
    </main>
  );
}
