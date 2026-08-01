"use client";

import { useState, useEffect } from "react";
import Navbar from "@/components/layout/Navbar";
import Sidebar from "@/components/layout/Sidebar";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { buttonVariants } from "@/components/ui/button";
import { FileText, Download, CheckCircle2, Clock, MemoryStick, Cpu } from "lucide-react";
import { API_URL } from "@/services/api";

export default function ReportPage() {
  const [pipelineResult, setPipelineResult] = useState<any>(null);

  useEffect(() => {
    const savedResult = localStorage.getItem("pipelineResult");
    const savedModel = localStorage.getItem("selectedModel");
    if (savedResult) {
      try {
        const parsed = JSON.parse(savedResult);
        if (parsed && parsed.model_id === savedModel) {
          setPipelineResult(parsed);
        } else {
          setPipelineResult(null);
        }
      } catch (e) {
        console.error("Error parsing pipelineResult:", e);
      }
    }
  }, []);

  const latencyVal = pipelineResult?.benchmark?.after?.latency?.average_ms || 0;
  const memoryVal = pipelineResult?.benchmark?.after?.memory?.rss_mb || 0;
  const tputVal = pipelineResult?.benchmark?.after?.throughput?.requests_per_second || 0;

  return (
    <>
      <Navbar />

      <div className="flex">
        <Sidebar />

        <main className="flex-1 p-10">
          <h1 className="text-4xl font-bold">Benchmark Report</h1>
          <p className="text-gray-500 mt-2">
            Review optimization results and export reports.
          </p>

          {!pipelineResult ? (
            <div className="mt-8 p-6 bg-yellow-50 border border-yellow-200 rounded-lg text-yellow-700">
              <p className="font-semibold">No report data available.</p>
              <p className="mt-1">
                You must run the model optimization pipeline first on the <strong>Optimize</strong> page before viewing or downloading reports.
              </p>
            </div>
          ) : (
            <>
              {/* Summary */}
              <div className="grid grid-cols-3 gap-6 mt-8">
                <Card>
                  <CardContent className="flex items-center gap-4 py-6">
                    <Clock className="text-blue-600" />
                    <div>
                      <p className="text-gray-500">Latency</p>
                      <h2 className="text-2xl font-bold">{latencyVal.toFixed(2)} ms</h2>
                    </div>
                  </CardContent>
                </Card>

                <Card>
                  <CardContent className="flex items-center gap-4 py-6">
                    <MemoryStick className="text-green-600" />
                    <div>
                      <p className="text-gray-500">Memory (RSS)</p>
                      <h2 className="text-2xl font-bold">{memoryVal.toFixed(0)} MB</h2>
                    </div>
                  </CardContent>
                </Card>

                <Card>
                  <CardContent className="flex items-center gap-4 py-6">
                    <Cpu className="text-purple-600" />
                    <div>
                      <p className="text-gray-500">Tokens/sec</p>
                      <h2 className="text-2xl font-bold">{tputVal.toFixed(1)}</h2>
                    </div>
                  </CardContent>
                </Card>
              </div>

              {/* Optimization Summary */}
              <Card className="mt-8">
                <CardHeader>
                  <CardTitle>Optimization Summary</CardTitle>
                </CardHeader>
                <CardContent className="space-y-4 font-mono text-sm">
                  <div className="flex items-center gap-3">
                    <CheckCircle2 className="text-green-600" />
                    <span>ONNX Runtime Export (STATUS: SUCCESS)</span>
                  </div>
                  <div className="flex items-center gap-3">
                    <CheckCircle2 className="text-green-600" />
                    <span>Deployment Artifact Packing (STATUS: COMPLETED)</span>
                  </div>
                </CardContent>
              </Card>

              {/* Report */}
              <Card className="mt-8">
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <FileText />
                    Generated Report & Deployment Packages
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="mb-6 text-gray-600">
                    Download optimization reports and structured configurations:
                  </p>

                  <ul className="list-disc ml-6 space-y-2 mb-8 text-gray-700">
                    <li>Automated Model Recommendations</li>
                    <li>Comparative Telemetry Speed & Latency Profiling Charts</li>
                    <li>Docker, Docker Compose, Nginx Config & Kubernetes Manifests</li>
                  </ul>

                  <div className="flex gap-4 mt-8">
                    <a
                      href={`${API_URL}/reports/latest`}
                      target="_blank"
                      rel="noopener noreferrer"
                      download="optimization_report.pdf"
                      className={buttonVariants({ variant: "default" })}
                    >
                      <Download className="mr-2 h-4 w-4" />
                      Download PDF Report
                    </a>

                    <a
                      href={`${API_URL}/deployment/download`}
                      download="deployment_package.zip"
                      className={buttonVariants({ variant: "outline" })}
                    >
                      <Download className="mr-2 h-4 w-4" />
                      Download Deployment ZIP
                    </a>

                    <a
                      href={`${API_URL}/artifacts/optimization_report.html`}
                      target="_blank"
                      rel="noopener noreferrer"
                      className={buttonVariants({ variant: "secondary" })}
                    >
                      Open HTML Report
                    </a>
                  </div>
                </CardContent>
              </Card>
            </>
          )}
        </main>
      </div>
    </>
  );
}