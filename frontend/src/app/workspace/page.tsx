"use client";

import { useEffect, useState } from "react";
import Sidebar from "@/components/layout/Sidebar";
import Navbar from "@/components/layout/Navbar";

const initialHistory = [
  {
    id: 1,
    model: "Llama 3.2 3B",
    optimization: "INT4 + GGUF",
    latency: "1.6 s",
    memory: "2.5 GB",
    status: "Completed",
  },
  {
    id: 2,
    model: "Gemma 2B",
    optimization: "ONNX",
    latency: "2.2 s",
    memory: "3.1 GB",
    status: "Completed",
  },
];

export default function Workspace() {
  const [stats, setStats] = useState({
    totalModels: 0,
    benchmarks: 0,
    optimizations: 0,
    reports: 0,
  });

  useEffect(() => {
    const saved = localStorage.getItem("optimindHistory");
    let historyList = saved ? JSON.parse(saved) : initialHistory;
    
    // Clean up any running/stale items (like Qwen 2.5)
    historyList = historyList.filter((item: any) => item.status !== "Running" && item.model !== "Qwen 2.5");
    localStorage.setItem("optimindHistory", JSON.stringify(historyList));

    // Calculate statistics
    const uniqueModels = new Set(historyList.map((item: any) => item.model)).size;
    const completedCount = historyList.filter((item: any) => item.status === "Completed").length;
    const totalRuns = historyList.length;
    const reportCount = completedCount;

    setStats({
      totalModels: uniqueModels,
      benchmarks: completedCount,
      optimizations: totalRuns,
      reports: reportCount,
    });
  }, []);

  return (
    <>
      <Navbar />

      <div className="flex">
        <Sidebar />

        <main className="flex-1 p-10">
          <h1 className="text-4xl font-bold">Dashboard</h1>

          <div className="grid grid-cols-4 gap-6 mt-10">
            <div className="border rounded-xl p-6 shadow-sm bg-white/50 backdrop-blur-md">
              <h2 className="text-sm font-medium text-gray-500">Total Models</h2>
              <p className="text-4xl font-extrabold mt-2 text-gray-900">
                {stats.totalModels}
              </p>
            </div>

            <div className="border rounded-xl p-6 shadow-sm bg-white/50 backdrop-blur-md">
              <h2 className="text-sm font-medium text-gray-500">Benchmarks</h2>
              <p className="text-4xl font-extrabold mt-2 text-gray-900">
                {stats.benchmarks}
              </p>
            </div>

            <div className="border rounded-xl p-6 shadow-sm bg-white/50 backdrop-blur-md">
              <h2 className="text-sm font-medium text-gray-500">Optimizations</h2>
              <p className="text-4xl font-extrabold mt-2 text-gray-900">
                {stats.optimizations}
              </p>
            </div>

            <div className="border rounded-xl p-6 shadow-sm bg-white/50 backdrop-blur-md">
              <h2 className="text-sm font-medium text-gray-500">Reports</h2>
              <p className="text-4xl font-extrabold mt-2 text-gray-900">
                {stats.reports}
              </p>
            </div>
          </div>
        </main>
      </div>
    </>
  );
}