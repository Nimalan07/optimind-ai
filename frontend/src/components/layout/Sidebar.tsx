"use client";

import Link from "next/link";

import {
    Gauge,
    Bot,
    Cpu,
    BarChart3,
    FileText,
    Settings
} from "lucide-react";

export default function Sidebar() {

    return (

        <aside className="w-64 h-screen border-r bg-white p-5">

            <div className="space-y-6">

                <Link href="/workspace" className="flex gap-3">

                    <Gauge />

                    Dashboard

                </Link>

                <Link href="/workspace/models" className="flex gap-3">

                    <Bot />

                    Models

                </Link>

                <Link href="/workspace/optimize" className="flex gap-3">

                    <Cpu />

                    Optimize

                </Link>

                <Link href="/workspace/benchmark" className="flex gap-3">

                    <BarChart3 />

                    Benchmark

                </Link>

                <Link href="/workspace/report" className="flex gap-3">

                    <FileText />

                    Reports

                </Link>

                <Link href="/settings" className="flex gap-3">

                    <Settings />

                    Settings

                </Link>

            </div>

        </aside>

    )

}