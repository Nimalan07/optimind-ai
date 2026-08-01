"use client";

import { useState, useEffect } from "react";
import Navbar from "@/components/layout/Navbar";
import Sidebar from "@/components/layout/Sidebar";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { API_URL } from "@/services/api";

const initialModels = [
  {
    id: "meta-llama/Llama-3.2-3B-Instruct",
    name: "Llama 3.2 3B",
    size: "2.0 GB",
    framework: "GGUF",
  },
  {
    id: "Qwen/Qwen2.5-3B-Instruct",
    name: "Qwen 2.5 3B",
    size: "2.3 GB",
    framework: "GGUF",
  },
  {
    id: "google/gemma-2b-it",
    name: "Gemma 2B",
    size: "1.8 GB",
    framework: "GGUF",
  },
  {
    id: "microsoft/Phi-3-mini-4k-instruct",
    name: "Phi-3 Mini",
    size: "2.2 GB",
    framework: "GGUF",
  },
];

export default function ModelsPage() {
  const [selectedModel, setSelectedModel] = useState<string>("");
  const [hfModelId, setHfModelId] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [statusMsg, setStatusMsg] = useState<string>("");

  useEffect(() => {
    localStorage.removeItem("selectedModel");
    setSelectedModel("");
  }, []);

  const handleSelect = (modelId: string) => {
    localStorage.setItem("selectedModel", modelId);
    setSelectedModel(modelId);
    setStatusMsg(`Selected model: ${modelId}`);
  };

  const handleDownload = async () => {
    if (!hfModelId) return;
    setLoading(true);
    setStatusMsg("Querying model recommendation info from backend...");
    try {
      const res = await fetch(`${API_URL}/recommend/${encodeURIComponent(hfModelId)}`, {
        method: "POST"
      });
      if (res.ok) {
        localStorage.setItem("selectedModel", hfModelId);
        setSelectedModel(hfModelId);
        setStatusMsg(`Successfully loaded model: ${hfModelId}`);
      } else {
        setStatusMsg("Failed to download/query model from backend.");
      }
    } catch (e) {
      setStatusMsg("Connection error communicating with backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Navbar />

      <div className="flex">
        <Sidebar />

        <main className="flex-1 p-10">
          <h1 className="text-4xl font-bold">Model Selection</h1>
          <p className="text-gray-500 mt-2">
            Choose a model to optimize and benchmark.
          </p>

          {statusMsg && (
            <div className="mt-4 p-3 bg-blue-50 border border-blue-200 rounded text-blue-700">
              {statusMsg}
            </div>
          )}

          {/* Active Selection Banner */}
          {selectedModel && (
            <div className="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg flex justify-between items-center">
              <div>
                <span className="font-semibold text-green-800">Active Selection:</span>
                <span className="ml-2 text-green-700 font-mono">{selectedModel}</span>
              </div>
              <Button size="sm" variant="outline" onClick={() => {
                localStorage.removeItem("selectedModel");
                setSelectedModel("");
              }}>Clear</Button>
            </div>
          )}

          {/* Built-in Models */}
          <h2 className="text-2xl font-semibold mt-10 mb-5">Popular Models</h2>
          <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-6">
            {initialModels.map((model) => (
              <Card key={model.id} className={selectedModel === model.id ? "border-green-500 shadow-md" : ""}>
                <CardHeader>
                  <CardTitle>{model.name}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p>Framework: {model.framework}</p>
                  <p>Size: {model.size}</p>
                  <Button 
                    className="mt-5 w-full"
                    variant={selectedModel === model.id ? "secondary" : "default"}
                    onClick={() => handleSelect(model.id)}
                  >
                    {selectedModel === model.id ? "Selected" : "Select Model"}
                  </Button>
                </CardContent>
              </Card>
            ))}
          </div>

          {/* HuggingFace */}
          <Card className="mt-10">
            <CardHeader>
              <CardTitle>Download from Hugging Face</CardTitle>
            </CardHeader>
            <CardContent>
              <Input
                placeholder="meta-llama/Llama-3.2-3B-Instruct"
                value={hfModelId}
                onChange={(e) => setHfModelId(e.target.value)}
              />
              <Button className="mt-5" onClick={handleDownload} disabled={loading}>
                {loading ? "Downloading..." : "Download Model"}
              </Button>
            </CardContent>
          </Card>

          {/* Upload */}
          <Card className="mt-10">
            <CardHeader>
              <CardTitle>Upload Local Model</CardTitle>
            </CardHeader>
            <CardContent>
              <Input type="file" />
              <Button className="mt-5">Upload</Button>
            </CardContent>
          </Card>

          {/* Ollama */}
          <Card className="mt-10">
            <CardHeader>
              <CardTitle>Ollama Models</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {["llama3", "qwen3", "gemma3"].map((ollamaName) => (
                  <div key={ollamaName} className="flex justify-between border rounded-lg p-3 items-center">
                    <span>{ollamaName}</span>
                    <Button onClick={() => handleSelect(ollamaName)}>Select</Button>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </main>
      </div>
    </>
  );
}