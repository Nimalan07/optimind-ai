"use client";

import Link from "next/link";
import { Cpu } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="h-16 border-b bg-white flex items-center justify-between px-8">
      <div className="flex items-center gap-3">
        <img src="/logo.png" alt="OptiMind AI Logo" className="h-10 w-10 object-contain rounded-md" />
        <h1 className="font-extrabold text-xl tracking-tight bg-gradient-to-r from-blue-600 to-green-600 bg-clip-text text-transparent">
          OptiMind AI
        </h1>
      </div>

      <div className="flex gap-8">
        <Link href="/">Home</Link>
        <Link href="/workspace">Workspace</Link>
        <Link href="/history">History</Link>
        <Link href="/about">About</Link>
      </div>
    </nav>
  );
}