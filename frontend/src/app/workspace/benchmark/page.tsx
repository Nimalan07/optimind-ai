"use client";

import { useState, useEffect } from "react";
import Navbar from "@/components/layout/Navbar";
import Sidebar from "@/components/layout/Sidebar";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import { API_URL } from "@/services/api";

export default function BenchmarkPage() {
  const [benchmarkResult, setBenchmarkResult] = useState<any>(null);
  const [running, setRunning] = useState<boolean>(false);
  const [modelId, setModelId] = useState<string>("");
  const [showComparison, setShowComparison] = useState<boolean>(false);

  useEffect(() => {
    const savedResult = localStorage.getItem("pipelineResult");
    const savedModel = localStorage.getItem("selectedModel");
    if (savedModel) {
      setModelId(savedModel);
    }
    if (savedResult) {
      try {
        const parsed = JSON.parse(savedResult);
        // Only load the benchmark results if the model ID matches the selected model
        if (parsed && parsed.model_id === savedModel) {
          setBenchmarkResult(parsed.benchmark);
        } else {
          setBenchmarkResult(null);
        }
      } catch (e) {
        console.error("Error parsing pipelineResult:", e);
      }
    }
  }, []);

  const handleRunBenchmark = async () => {
    if (!modelId) return;
    setRunning(true);
    try {
      const res = await fetch(`${API_URL}/pipeline/run/${encodeURIComponent(modelId)}`, {
        method: "POST"
      });
      if (res.ok) {
        const data = await res.json();
        localStorage.setItem("pipelineResult", JSON.stringify(data));
        setBenchmarkResult(data.benchmark);
      }
    } catch (e) {
      console.error("Error running benchmark:", e);
    } finally {
      setRunning(false);
    }
  };

  const handleExportCSV = () => {
    if (!modelId || !benchmarkResult) return;
    const csvRows = [
      ["Metric", "Original Model", "Optimized Model", "Improvement"],
      ["Latency", `${beforeLat.toFixed(2)} ms`, `${afterLat.toFixed(2)} ms`, `${latDiff.toFixed(0)}%`],
      ["Memory", `${beforeMem.toFixed(0)} MB`, `${afterMem.toFixed(0)} MB`, `${memDiff.toFixed(0)}%`],
      ["Throughput", `${beforeTput.toFixed(1)} RPS`, `${afterTput.toFixed(1)} RPS`, `${tputDiff.toFixed(0)}%`]
    ];
    
    const csvContent = "data:text/csv;charset=utf-8," 
      + csvRows.map(row => row.map(val => `"${val}"`).join(",")).join("\n");
      
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `${modelId.replace(/\//g, "_")}_benchmark.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  // Extract values safely
  const beforeLat = benchmarkResult?.before?.latency?.average_ms || 0;
  const afterLat = benchmarkResult?.after?.latency?.average_ms || 0;

  const beforeMem = benchmarkResult?.before?.memory?.rss_mb || 0;
  const afterMem = benchmarkResult?.after?.memory?.rss_mb || 0;

  const beforeTput = benchmarkResult?.before?.throughput?.requests_per_second || 0;
  const afterTput = benchmarkResult?.after?.throughput?.requests_per_second || 0;

  const chartData = [
    {
      metric: "Latency (ms)",
      original: parseFloat(beforeLat.toFixed(2)),
      optimized: parseFloat(afterLat.toFixed(2)),
    },
    {
      metric: "Memory (MB)",
      original: parseFloat(beforeMem.toFixed(2)),
      optimized: parseFloat(afterMem.toFixed(2)),
    },
    {
      metric: "Throughput (RPS)",
      original: parseFloat(beforeTput.toFixed(2)),
      optimized: parseFloat(afterTput.toFixed(2)),
    },
  ];

  // Percent calculations
  const latDiff = beforeLat > 0 ? ((beforeLat - afterLat) / beforeLat) * 100 : 0;
  const memDiff = beforeMem > 0 ? ((beforeMem - afterMem) / beforeMem) * 100 : 0;
  const tputDiff = beforeTput > 0 ? ((afterTput - beforeTput) / beforeTput) * 100 : 0;

  return (
    <>
      <Navbar />

      <div className="flex">
        <Sidebar />

        <main className="flex-1 p-10">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-4xl font-bold">Benchmark Dashboard</h1>
              <p className="text-gray-500 mt-2">
                Compare model performance before and after optimization.
              </p>
            </div>
            <span className="text-sm font-semibold px-3 py-1.5 rounded-full bg-blue-100 text-blue-800 border border-blue-200">
              Active Model: {modelId || "None"}
            </span>
          </div>

          {!benchmarkResult ? (
            <div className="mt-8 space-y-6">
              <div className="p-6 bg-yellow-50 border border-yellow-200 rounded-lg text-yellow-700">
                <p className="font-semibold">No benchmark data available.</p>
                <p className="mt-1">
                  You must run the model optimization pipeline first on the <strong>Optimize</strong> page before viewing benchmark comparison reports.
                </p>
              </div>

              <Card>
                <CardHeader>
                  <CardTitle>Benchmark Actions</CardTitle>
                </CardHeader>
                <CardContent className="flex gap-5">
                  <Button onClick={handleRunBenchmark} disabled={running || !modelId}>
                    {running ? "Running Telemetry Benchmark..." : "Run Benchmark"}
                  </Button>
                </CardContent>
              </Card>
            </div>
          ) : (
            <>
              <div className="grid grid-cols-4 gap-6 mt-10">
                <Card>
                  <CardHeader>
                    <CardTitle>Latency</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <h2 className="text-3xl font-bold">{afterLat.toFixed(2)} ms</h2>
                    <p className="text-green-600 font-semibold">↓ {latDiff.toFixed(0)}% faster</p>
                  </CardContent>
                </Card>

                <Card>
                  <CardHeader>
                    <CardTitle>Memory</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <h2 className="text-3xl font-bold">{afterMem.toFixed(0)} MB</h2>
                    <p className="text-green-600 font-semibold">↓ {memDiff.toFixed(0)}% saved</p>
                  </CardContent>
                </Card>

                <Card>
                  <CardHeader>
                    <CardTitle>Tokens/sec</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <h2 className="text-3xl font-bold">{afterTput.toFixed(1)}</h2>
                    <p className="text-green-600 font-semibold">↑ {tputDiff.toFixed(0)}% throughput</p>
                  </CardContent>
                </Card>

                <Card>
                  <CardHeader>
                    <CardTitle>Telemetry Status</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <h2 className="text-3xl font-bold text-green-600">READY</h2>
                  </CardContent>
                </Card>
              </div>

              <Card className="mt-10">
                <CardHeader>
                  <CardTitle>Benchmark Comparison</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="h-96">
                    <ResponsiveContainer width="100%" height="100%">
                      <BarChart data={chartData}>
                        <XAxis dataKey="metric" />
                        <YAxis />
                        <Tooltip />
                        <Bar dataKey="original" fill="#94a3b8" name="Original Model" />
                        <Bar dataKey="optimized" fill="#2563eb" name="Optimized Model" />
                      </BarChart>
                    </ResponsiveContainer>
                  </div>
                </CardContent>
              </Card>

              {showComparison && (
                <Card className="mt-10">
                  <CardHeader>
                    <CardTitle>Side-by-Side Model Comparison</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="overflow-x-auto">
                      <table className="min-w-full divide-y divide-gray-200">
                        <thead className="bg-gray-50">
                          <tr>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Metric</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Original Model</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Optimized Model</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Improvement</th>
                          </tr>
                        </thead>
                        <tbody className="bg-white divide-y divide-gray-200">
                          <tr>
                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Inference Latency</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{beforeLat.toFixed(2)} ms</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-blue-600 font-medium">{afterLat.toFixed(2)} ms</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-green-600 font-semibold">↓ {latDiff.toFixed(1)}%</td>
                          </tr>
                          <tr>
                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Memory Consumption</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{beforeMem.toFixed(1)} MB</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-blue-600 font-medium">{afterMem.toFixed(1)} MB</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-green-600 font-semibold">↓ {memDiff.toFixed(1)}%</td>
                          </tr>
                          <tr>
                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Tokens Generation Rate</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{beforeTput.toFixed(1)} Tok/s</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-blue-600 font-medium">{afterTput.toFixed(1)} Tok/s</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-green-600 font-semibold">↑ {tputDiff.toFixed(1)}%</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </CardContent>
                </Card>
              )}

              <Card className="mt-10">
                <CardHeader>
                  <CardTitle>Benchmark Actions</CardTitle>
                </CardHeader>
                <CardContent className="flex gap-5">
                  <Button onClick={handleRunBenchmark} disabled={running}>
                    {running ? "Running Telemetry Benchmark..." : "Run Benchmark"}
                  </Button>
                  <Button variant="outline" onClick={() => setShowComparison(!showComparison)}>
                    {showComparison ? "Hide Comparison" : "Compare Models"}
                  </Button>
                  <Button variant="secondary" onClick={handleExportCSV}>Export CSV</Button>
                </CardContent>
              </Card>
            </>
          )}
        </main>
      </div>
    </>
  );
}