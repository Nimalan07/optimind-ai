"use client";

import { useState, useEffect } from "react";
import Navbar from "@/components/layout/Navbar";
import Sidebar from "@/components/layout/Sidebar";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { API_URL } from "@/services/api";
import { useRouter } from "next/navigation";
import { Cpu, Cloud, DollarSign, Gauge } from "lucide-react";

export default function OptimizePage() {
  const [modelId, setModelId] = useState<string>("");
  const [recommendation, setRecommendation] = useState<any>(null);
  const [loadingRecommendation, setLoadingRecommendation] = useState<boolean>(false);
  
  const [optimizing, setOptimizing] = useState<boolean>(false);
  const [currentStage, setCurrentStage] = useState<string>("");
  const [progressMsg, setProgressMsg] = useState<string>("");
  const [abortController, setAbortController] = useState<AbortController | null>(null);
  const router = useRouter();

  useEffect(() => {
    const savedModel = localStorage.getItem("selectedModel");
    if (savedModel) {
      setModelId(savedModel);
      fetchRecommendation(savedModel);
    }
  }, []);

  const fetchRecommendation = async (id: string) => {
    setLoadingRecommendation(true);
    try {
      const res = await fetch(`${API_URL}/recommend/${encodeURIComponent(id)}`, {
        method: "POST"
      });
      if (res.ok) {
        const data = await res.json();
        setRecommendation(data);
      }
    } catch (e) {
      console.error("Failed to load recommendation:", e);
    } finally {
      setLoadingRecommendation(false);
    }
  };

  const handleCancel = () => {
    try {
      if (abortController) {
        abortController.abort();
      }
    } catch (err) {
      console.warn("Fetch abort signal dispatched:", err);
    }
    setOptimizing(false);
    setCurrentStage("Optimization cancelled.");
    setProgressMsg("Pipeline execution was aborted by the user.");
  };

  const handleOptimize = async () => {
    if (!modelId) return;
    setOptimizing(true);
    setCurrentStage("Starting Optimization Pipeline...");
    
    // Setup stages for progress simulation
    const stages = [
      "Downloading Model weights...",
      "Inspecting model config schema...",
      "Generating platform recommendation heuristics...",
      "Exporting to ONNX Runtime model representation...",
      "Running dynamic INT8/INT4 Quantization passes...",
      "Benchmarking original vs optimized models...",
      "Packaging deployment files (Dockerfile, Compose, K8s)...",
      "Generating report PDF & HTML sheets..."
    ];

    let currentIdx = 0;
    const interval = setInterval(() => {
      if (currentIdx < stages.length) {
        setCurrentStage(stages[currentIdx]);
        currentIdx++;
      }
    }, 2000);

    const controller = new AbortController();
    setAbortController(controller);

    try {
      const res = await fetch(`${API_URL}/pipeline/run/${encodeURIComponent(modelId)}`, {
        method: "POST",
        signal: controller.signal
      });
      
      clearInterval(interval);
      
      if (res.ok) {
        const result = await res.json();
        localStorage.setItem("pipelineResult", JSON.stringify(result));
        setCurrentStage("Complete!");
        setProgressMsg("Redirecting to Benchmark dashboard...");
        setTimeout(() => {
          router.push("/workspace/benchmark");
        }, 1500);
      } else {
        setCurrentStage("Optimization failed.");
        setProgressMsg("Backend pipeline endpoint returned an error status.");
        setOptimizing(false);
      }
    } catch (e: any) {
      clearInterval(interval);
      if (e.name === 'AbortError') {
        setCurrentStage("Optimization cancelled.");
        setProgressMsg("Pipeline execution was aborted by the user.");
      } else {
        setCurrentStage("Error during optimization.");
        setProgressMsg("Failed to communicate with backend optimization agent.");
      }
      setOptimizing(false);
    }
  };

  const inspection = recommendation?.inspection || {};
  const recBackend = recommendation?.backend || {};
  const recCost = recommendation?.cloud_cost || {};

  return (
    <>
      <Navbar />

      <div className="flex">
        <Sidebar />

        <main className="flex-1 p-10">
          <h1 className="text-4xl font-bold">Model Optimization</h1>
          <p className="text-gray-500 mt-2">
            Select optimization techniques before benchmarking.
          </p>

          {!modelId ? (
            <div className="mt-8 p-6 bg-yellow-50 border border-yellow-200 rounded-lg text-yellow-700">
              <p className="font-semibold">No active model selected.</p>
              <p className="mt-1">Please select a model on the Models page first before proceeding.</p>
            </div>
          ) : (
            <>
              {/* Selected Model */}
              <Card className="mt-8">
                <CardHeader>
                  <CardTitle>Selected Model Details</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="grid grid-cols-2 gap-6 font-mono text-sm">
                    <div>
                      <p className="font-semibold text-gray-500">Model Name/ID</p>
                      <p className="text-gray-800">{modelId}</p>
                    </div>
                    <div>
                      <p className="font-semibold text-gray-500">Architecture</p>
                      <p className="text-gray-800">{inspection.architecture || "Loading..."}</p>
                    </div>
                    <div>
                      <p className="font-semibold text-gray-500">Attention Heads</p>
                      <p className="text-gray-800">{inspection.attention_heads || "Loading..."}</p>
                    </div>
                    <div>
                      <p className="font-semibold text-gray-500">Parameters (Est.)</p>
                      <p className="text-gray-800">{inspection.estimated_parameters_billion ? `${inspection.estimated_parameters_billion} B` : "Loading..."}</p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* Optimization Options */}
              <Card className="mt-8">
                <CardHeader>
                  <CardTitle>Optimization Techniques</CardTitle>
                </CardHeader>
                <CardContent className="space-y-5">
                  <div className="flex items-center gap-3">
                    <Checkbox defaultChecked />
                    <span>Convert to ONNX Runtime</span>
                  </div>
                  <div className="flex items-center gap-3">
                    <Checkbox defaultChecked />
                    <span>INT8 Quantization</span>
                  </div>
                  <div className="flex items-center gap-3">
                    <Checkbox />
                    <span>INT4 Quantization</span>
                  </div>
                  <div className="flex items-center gap-3">
                    <Checkbox />
                    <span>GGUF Conversion (llama.cpp)</span>
                  </div>
                  <div className="flex items-center gap-3">
                    <Checkbox />
                    <span>Model Pruning</span>
                  </div>
                </CardContent>
              </Card>

              {/* AI Recommendation */}
              <Card className="mt-8">
                <CardHeader>
                  <CardTitle>AI Recommendation Heuristic</CardTitle>
                </CardHeader>
                <CardContent>
                  {loadingRecommendation ? (
                    <p className="text-gray-500">Loading AI heuristics from backend...</p>
                  ) : recommendation ? (
                    <div className="grid grid-cols-2 gap-4">
                      <div className="flex items-center gap-3 p-3 bg-muted/40 rounded-lg border border-border/50">
                        <div className="p-2 bg-blue-500/10 text-blue-600 dark:text-blue-400 rounded-md">
                          <Cpu className="h-5 w-5" />
                        </div>
                        <div>
                          <p className="text-xs text-gray-500 font-medium">Recommended Backend</p>
                          <p className="text-sm font-semibold text-gray-800 dark:text-gray-200">
                            {recBackend.backend || "ONNX Runtime"}
                          </p>
                        </div>
                      </div>

                      <div className="flex items-center gap-3 p-3 bg-muted/40 rounded-lg border border-border/50">
                        <div className="p-2 bg-green-500/10 text-green-600 dark:text-green-400 rounded-md">
                          <Cloud className="h-5 w-5" />
                        </div>
                        <div>
                          <p className="text-xs text-gray-500 font-medium">Recommended Cloud VM</p>
                          <p className="text-sm font-semibold text-gray-800 dark:text-gray-200">
                            {recommendation.cloud?.provider} ({recommendation.cloud?.instance} - {recommendation.cloud?.processor})
                          </p>
                        </div>
                      </div>

                      <div className="flex items-center gap-3 p-3 bg-muted/40 rounded-lg border border-border/50">
                        <div className="p-2 bg-amber-500/10 text-amber-600 dark:text-amber-400 rounded-md">
                          <DollarSign className="h-5 w-5" />
                        </div>
                        <div>
                          <p className="text-xs text-gray-500 font-medium">Estimated Hosting Cost</p>
                          <p className="text-sm font-semibold text-gray-800 dark:text-gray-200">
                            ${recCost.monthly_cost_usd}/mo
                          </p>
                        </div>
                      </div>

                      <div className="flex items-center gap-3 p-3 bg-muted/40 rounded-lg border border-border/50">
                        <div className="p-2 bg-purple-500/10 text-purple-600 dark:text-purple-400 rounded-md">
                          <Gauge className="h-5 w-5" />
                        </div>
                        <div>
                          <p className="text-xs text-gray-500 font-medium">Optimization Score</p>
                          <p className="text-sm font-semibold text-gray-800 dark:text-gray-200">
                            {recommendation.optimization_score}/100
                          </p>
                        </div>
                      </div>
                    </div>
                  ) : (
                    <p className="text-gray-500">AI recommendation details will display once model is queried.</p>
                  )}
                </CardContent>
              </Card>

              {/* Start */}
              {optimizing ? (
                <div className="mt-10 p-6 border border-blue-200 bg-blue-50 rounded-lg flex justify-between items-center">
                  <div className="flex items-center gap-4">
                    <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-600"></div>
                    <div>
                      <h4 className="font-semibold text-blue-800">{currentStage}</h4>
                      {progressMsg && <p className="text-sm text-blue-600 mt-1">{progressMsg}</p>}
                    </div>
                  </div>
                  <Button variant="destructive" onClick={handleCancel}>
                    Cancel Optimization
                  </Button>
                </div>
              ) : (
                <div className="mt-10">
                  <Button size="lg" onClick={handleOptimize}>
                    Start Optimization
                  </Button>
                </div>
              )}
            </>
          )}
        </main>
      </div>
    </>
  );
}