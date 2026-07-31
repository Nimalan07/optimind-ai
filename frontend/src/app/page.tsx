import Navbar from "@/components/layout/Navbar";
import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <>
      <Navbar />

      <main className="min-h-screen flex flex-col items-center justify-center text-center px-10">

        <h1 className="text-6xl font-black">

          OptiMind AI

        </h1>

        <p className="mt-6 text-xl max-w-3xl text-gray-600">

          Optimize AI Models, Benchmark Performance,
          Compare Results and Deploy Efficiently
          on Arm CPUs.

        </p>

        <Link href="/workspace">

          <Button className="mt-10 px-10 py-7 text-lg">

            Get Started

          </Button>

        </Link>

      </main>
    </>
  );
}