"use client";

import Navbar from "@/components/layout/Navbar";
import Sidebar from "@/components/layout/Sidebar";
import { 
  Cpu, 
  Server, 
  Layers, 
  CheckCircle2, 
  Target, 
  Brain,
  Search,
  Eye,
  Activity,
  FileText,
  Package,
  ArrowRight
} from "lucide-react";

export default function AboutPage() {
  const features = [
    "AI Model Inspection",
    "Intelligent Backend Recommendation",
    "Arm Cloud Recommendation",
    "ONNX Runtime Optimization",
    "Dynamic Quantization",
    "Performance Benchmarking",
    "Deployment Package Generation",
    "PDF & HTML Reports"
  ];

  const cloudPlatforms = [
    { name: "AWS Graviton", desc: "Arm-based instances offering up to 40% better price performance", color: "from-orange-500 to-yellow-500" },
    { name: "Google Axion", desc: "Google's custom Arm-based CPU delivering industry-leading energy efficiency", color: "from-blue-500 to-emerald-500" },
    { name: "Microsoft Cobalt", desc: "Microsoft's customized Arm CPU designed for cloud-scale workloads", color: "from-purple-500 to-indigo-500" }
  ];

  const pipelineSteps = [
    { name: "Model Selection", desc: "Choose model from HF or use a downloaded model", icon: Search },
    { name: "Architecture Inspection", desc: "Inspect configurations, attention heads & parameters", icon: Eye },
    { name: "AI Recommendations", desc: "Get optimized backend & cloud configurations", icon: Brain },
    { name: "Optimization", desc: "Run ONNX export & quantization pipelines", icon: Cpu },
    { name: "Benchmark", desc: "Profile latency, memory & throughput", icon: Activity },
    { name: "Report Generation", desc: "Generate dynamic PDF & HTML reports", icon: FileText },
    { name: "Deployment Package", desc: "Produce production-ready Docker & K8s files", icon: Package }
  ];

  return (
    <>
      <Navbar />
      <div className="flex bg-slate-50/50 min-h-[calc(100vh-4rem)]">
        <Sidebar />
        
        <main className="flex-1 p-8 overflow-y-auto max-w-6xl mx-auto space-y-8">
          
          {/* Header Section (Hero) */}
          <div className="relative overflow-hidden rounded-2xl border border-slate-200/80 bg-white shadow-sm p-8 flex flex-col md:flex-row items-center justify-between gap-8">
            <div className="absolute top-0 right-0 w-96 h-96 bg-gradient-to-tr from-blue-100/30 to-green-100/30 rounded-full blur-3xl -z-10" />
            <div className="space-y-4 max-w-2xl">
              <div className="inline-flex items-center gap-2 px-2.5 py-0.5 rounded-full bg-blue-50 border border-blue-200 text-blue-700 text-xs font-semibold">
                <span>Version v1.0.0</span>
              </div>
              <h1 className="text-3xl md:text-4xl font-extrabold tracking-tight text-slate-900">
                About <span className="bg-gradient-to-r from-blue-600 to-green-600 bg-clip-text text-transparent">OptiMind AI</span>
              </h1>
              <p className="text-slate-600 leading-relaxed text-sm md:text-base">
                OptiMind AI is an intelligent platform for analyzing, optimizing, benchmarking, and preparing AI models for deployment on modern Arm-based cloud infrastructure. It helps developers choose the best inference backend, optimize model performance, and generate production-ready deployment artifacts.
              </p>
              
              {/* Mission statement */}
              <div className="flex gap-3 items-start p-3.5 rounded-xl bg-green-50/40 border border-green-100 text-green-800">
                <Target className="w-4 h-4 mt-0.5 text-green-600 shrink-0" />
                <div>
                  <span className="font-bold text-xs uppercase tracking-wider text-green-700 block">Our Mission</span>
                  <p className="text-xs md:text-sm italic mt-0.5 font-medium">
                    "Simplifying AI model optimization and enabling efficient deployment on Arm-powered cloud infrastructure."
                  </p>
                </div>
              </div>
            </div>
            
            <div className="shrink-0 w-32 h-32 relative rounded-xl overflow-hidden border border-slate-100 shadow bg-white p-3 flex items-center justify-center">
              <img src="/logo.png" alt="OptiMind AI Logo" className="w-full h-full object-contain" />
            </div>
          </div>

          {/* Grid: Features & Cloud Platforms */}
          <div className="grid md:grid-cols-2 gap-6">
            
            {/* Features Card */}
            <div className="rounded-2xl border border-slate-200/80 bg-white p-6 shadow-sm hover:shadow-md transition-all duration-300">
              <div className="flex items-center gap-2.5 mb-5 border-b border-slate-100 pb-3">
                <CheckCircle2 className="w-5 h-5 text-blue-600" />
                <h2 className="text-lg font-bold text-slate-800">Key Features</h2>
              </div>
              <div className="grid sm:grid-cols-2 gap-3">
                {features.map((feature, i) => (
                  <div key={i} className="flex gap-2 items-center">
                    <span className="w-4 h-4 rounded-full bg-green-100 text-green-700 flex items-center justify-center font-bold text-[10px] shrink-0">✓</span>
                    <span className="text-xs font-semibold text-slate-700 leading-snug">{feature}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Cloud Platforms Card */}
            <div className="rounded-2xl border border-slate-200/80 bg-white p-6 shadow-sm hover:shadow-md transition-all duration-300">
              <div className="flex items-center gap-2.5 mb-5 border-b border-slate-100 pb-3">
                <Server className="w-5 h-5 text-emerald-600" />
                <h2 className="text-lg font-bold text-slate-800">Supported Cloud Platforms</h2>
              </div>
              <div className="space-y-3.5">
                {cloudPlatforms.map((platform, i) => (
                  <div key={i} className="flex items-center gap-3">
                    <div className={`w-2.5 h-2.5 rounded-full bg-gradient-to-r ${platform.color} shrink-0 shadow-sm`} />
                    <div className="space-y-0.5">
                      <h4 className="font-bold text-slate-800 text-xs">{platform.name}</h4>
                      <p className="text-[10px] text-slate-500 font-medium leading-relaxed">{platform.desc}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>

          </div>

          {/* Pipeline Diagram Card */}
          <div className="rounded-2xl border border-slate-200/80 bg-white p-6 shadow-sm hover:shadow-md transition-all duration-300">
            <div className="flex items-center gap-2.5 mb-6 border-b border-slate-100 pb-3">
              <Layers className="w-5 h-5 text-purple-600" />
              <h2 className="text-lg font-bold text-slate-800">Optimization Pipeline</h2>
            </div>
            
            {/* Visual Pipeline flow */}
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-7 gap-4 relative">
              {pipelineSteps.map((step, i) => {
                const Icon = step.icon;
                return (
                  <div key={i} className="flex flex-col items-center text-center relative group">
                    {/* Step number badge */}
                    <div className="absolute -top-1.5 -left-1.5 w-4.5 h-4.5 rounded-full bg-slate-100 border border-slate-200 text-slate-600 flex items-center justify-center text-[9px] font-bold">
                      {i + 1}
                    </div>
                    
                    {/* Step Icon container */}
                    <div className="w-11 h-11 rounded-xl bg-slate-50 border border-slate-100 shadow-sm flex items-center justify-center text-slate-600 group-hover:scale-110 group-hover:bg-blue-50 group-hover:border-blue-200 group-hover:text-blue-600 transition-all duration-300">
                      <Icon className="w-5 h-5" />
                    </div>
                    
                    {/* Step Labels */}
                    <h4 className="font-bold text-slate-800 text-[11px] mt-2.5 leading-snug">{step.name}</h4>
                    <p className="text-[9px] text-slate-500 font-medium mt-1 leading-relaxed max-w-[100px] hidden sm:block">
                      {step.desc}
                    </p>

                    {/* Right Arrow (only visible between steps on large screens) */}
                    {i < pipelineSteps.length - 1 && (
                      <div className="hidden md:flex absolute top-3.5 -right-3.5 text-slate-300">
                        <ArrowRight className="w-3.5 h-3.5" />
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>

          {/* Footer Accent */}
          <footer className="text-center py-4 mt-8 border-t border-slate-100">
            <p className="text-xs font-semibold text-slate-400">
              Built for the Arm AI Optimization Challenge 2026
            </p>
          </footer>

        </main>
      </div>
    </>
  );
}
