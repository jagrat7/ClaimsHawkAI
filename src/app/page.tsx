import Image from "next/image";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import logo from "../../public/images/claimshawk_logo_with_transparent_background_more_robotic.jpeg";
export const mockSpeakers = [
  {
    id: "1",
    name: "John Hamilton",
    party: "Democratic",
    claims_count: 156,
    role: "Senator",
  },
  {
    id: "2",
    name: "Sarah Mitchell",
    party: "Republican",
    claims_count: 143,
    role: "Representative",
  },
  {
    id: "3",
    name: "Michael Chen",
    party: "Democratic",
    claims_count: 89,
    role: "Governor",
  },
  {
    id: "4",
    name: "Rachel Brooks",
    party: "Independent",
    claims_count: 67,
    role: "Senator",
  },
  {
    id: "5",
    name: "David Wilson",
    party: "Republican",
    claims_count: 234,
    role: "Representative",
  },
  {
    id: "6",
    name: "Lisa Rodriguez",
    party: "Democratic",
    claims_count: 178,
    role: "Senator",
  },
  {
    id: "7",
    name: "Thomas Anderson",
    party: "Republican",
    claims_count: 145,
    role: "Governor",
  },
  {
    id: "8",
    name: "Emily Parker",
    party: "Independent",
    claims_count: 92,
    role: "Representative",
  }
];
export default async function Home() {
  const speakers = mockSpeakers;
  
  return (
    <main className="min-h-screen">
      {/* Hero Section */}
      <section className="relative min-h-[calc(100vh-4rem)] flex items-center justify-center overflow-hidden py-16">
        {/* Background Effects */}
        <div className="absolute inset-0 bg-grid-white/10" />
        <div className="absolute inset-0 bg-gradient-to-b from-background via-background/90 to-background/50" />
        
        {/* Content */}
        <div className="relative z-10 container mx-auto px-4 flex flex-col items-center text-center max-w-6xl">
          <div className="relative w-[250px] h-[250px] mb-8">
            <Image
              src={logo}
              alt="ClaimsHawk Logo"
              fill
              className="object-contain"
              priority
              style={{
                maskImage: 'radial-gradient(circle, black 60%, transparent 70%)',
                WebkitMaskImage: 'radial-gradient(circle, black 60%, transparent 70%)'
              }}
            />
          </div>
          
          <h1 className="text-5xl md:text-7xl lg:text-8xl font-bold mb-6">
            <span className="bg-gradient-to-r from-primary to-primary/60 text-transparent bg-clip-text">
              ClaimsHawk
            </span>
          </h1>
          
          <p className="text-xl md:text-2xl text-muted-foreground max-w-3xl mb-12">
            AI-powered claim-tracking that keeps politicians accountable. Automatically analyze claims and uncover the truth.
          </p>
          
          <div className="flex flex-col justify-center sm:flex-row gap-4 w-full max-w-lg">
            <Button 
              size="lg" 
              className="w-full sm:w-auto bg-primary hover:bg-primary/90 text-lg"
            >
              Get Started
            </Button>
            <Button 
              variant="outline" 
              size="lg" 
              className="w-full sm:w-auto border-primary/20 hover:bg-primary/5 text-lg"
            >
              Watch Demo
            </Button>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-2 md:grid-cols-3 gap-12 mt-20 w-full max-w-4xl mx-auto place-items-center">
            <div className="space-y-3 text-center">
              <h3 className="text-5xl font-bold text-primary">1.2K+</h3>
              <p className="text-lg text-muted-foreground">Claims Analyzed</p>
            </div>
            <div className="space-y-3 text-center">
              <h3 className="text-5xl font-bold text-primary">98%</h3>
              <p className="text-lg text-muted-foreground">Accuracy Rate</p>
            </div>
            <div className="space-y-3 text-center col-span-2 md:col-span-1">
              <h3 className="text-5xl font-bold text-primary">24/7</h3>
              <p className="text-lg text-muted-foreground">Monitoring</p>
            </div>
          </div>
        </div>

        {/* Decorative Elements */}
        <div className="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-primary/20 to-transparent" />
        <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce text-primary/40">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
        </div>
      </section>

      {/* Speakers Section */}
      <section className="container mx-auto px-4 py-16">
        <h2 className="text-3xl font-bold mb-8 bg-gradient-to-r from-primary to-primary/60 text-transparent bg-clip-text">
          Speakers & Claims
        </h2>
        <Card>
          <CardContent className="p-6">
            <Table>
              <TableHeader>
                <TableRow className="hover:bg-primary/5">
                  <TableHead className="w-[50%]">Speaker</TableHead>
                  <TableHead>Party</TableHead>
                  <TableHead className="text-right">Claims</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {speakers.map((speaker: any) => (
                  <TableRow 
                    key={speaker.id}
                    className="hover:bg-primary/5"
                  >
                    <TableCell className="font-medium">{speaker.name}</TableCell>
                    <TableCell>{speaker.party}</TableCell>
                    <TableCell className="text-right">{speaker.claims_count}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </section>
    </main>
  );
}
