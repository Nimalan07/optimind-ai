"use client";

import Navbar from "@/components/layout/Navbar";
import Sidebar from "@/components/layout/Sidebar";
import { 
  Cpu, 
  Server, 
  Layers, 
  CheckCircle2, 
  Info, 
  Target, 
  ExternalLink, 
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

  const techStack = {
    frontend: ["Next.js", "React", "Tailwind CSS", "TypeScript"],
    backend: ["FastAPI", "Python", "ONNX Runtime", "Hugging Face", "Optimum", "Transformers"]
  };

  const optimizationTech = [
    "ONNX Runtime",
    "Dynamic INT8 Quantization",
    "INT4 Quantization",
    "GGUF Conversion (llama.cpp)",
    "Docker Deployment",
    "Kubernetes Deployment"
  ];

  return (
    <>
      <Navbar />
      <div className="flex bg-slate-50/50 min-h-[calc(100vh-4rem)]">
        <Sidebar />
        
        <main className="flex-1 p-8 overflow-y-auto max-w-7xl mx-auto space-y-10">
          
          {/* Header Section */}
          <div className="relative overflow-hidden rounded-3xl border border-slate-200/80 bg-white shadow-sm p-8 md:p-12 flex flex-col md:flex-row items-center justify-between gap-8">
            <div className="absolute top-0 right-0 w-96 h-96 bg-gradient-to-tr from-blue-100/40 to-green-100/40 rounded-full blur-3xl -z-10" />
            <div className="space-y-4 max-w-2xl">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-700 text-xs font-semibold">
                <span>Version v1.0.0</span>
              </div>
              <h1 className="text-4xl md:text-5xl font-black tracking-tight text-slate-900">
                About <span className="bg-gradient-to-r from-blue-600 to-green-600 bg-clip-text text-transparent">OptiMind AI</span>
              </h1>
              <p className="text-slate-600 leading-relaxed text-base">
                OptiMind AI is an intelligent platform for analyzing, optimizing, benchmarking, and preparing AI models for deployment on modern Arm-based cloud infrastructure. It helps developers choose the best inference backend, optimize model performance, and generate production-ready deployment artifacts.
              </p>
              
              {/* Mission statement */}
              <div className="flex gap-3 items-start p-4 rounded-xl bg-green-50/50 border border-green-100 text-green-800">
                <Target className="w-5 h-5 mt-0.5 text-green-600 shrink-0" />
                <div>
                  <span className="font-bold text-xs uppercase tracking-wider text-green-700 block">Our Mission</span>
                  <p className="text-sm italic mt-0.5 font-medium">
                    "Simplifying AI model optimization and enabling efficient deployment on Arm-powered cloud infrastructure."
                  </p>
                </div>
              </div>
            </div>
            
            <div className="shrink-0 w-40 h-40 relative rounded-2xl overflow-hidden border border-slate-100 shadow-lg bg-white p-4 flex items-center justify-center">
              <img src="/logo.png" alt="OptiMind AI Logo" className="w-full h-full object-contain" />
            </div>
          </div>

          {/* Grid: Features & Cloud Platforms */}
          <div className="grid md:grid-cols-2 gap-8">
            
            {/* Features Card */}
            <div className="rounded-2xl border border-slate-200/80 bg-white p-6 shadow-sm flex flex-col justify-between hover:shadow-md transition-all duration-300">
              <div>
                <div className="flex items-center gap-3 mb-6">
                  <div className="p-2.5 rounded-lg bg-blue-50 border border-blue-100 text-blue-600">
                    <CheckCircle2 className="w-6 h-6" />
                  </div>
                  <h2 className="text-xl font-bold text-slate-800">🚀 Key Features</h2>
                </div>
                <div className="grid sm:grid-cols-2 gap-4">
                  {features.map((feature, i) => (
                    <div key={i} className="flex gap-2.5 items-center p-2 rounded-lg hover:bg-slate-50 transition-colors">
                      <span className="w-5 h-5 rounded-full bg-green-100 border border-green-200 text-green-700 flex items-center justify-center font-bold text-xs shrink-0">✓</span>
                      <span className="text-sm font-semibold text-slate-700 leading-snug">{feature}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Cloud Platforms Card */}
            <div className="rounded-2xl border border-slate-200/80 bg-white p-6 shadow-sm flex flex-col justify-between hover:shadow-md transition-all duration-300">
              <div>
                <div className="flex items-center gap-3 mb-6">
                  <div className="p-2.5 rounded-lg bg-emerald-50 border border-emerald-100 text-emerald-600">
                    <Server className="w-6 h-6" />
                  </div>
                  <h2 className="text-xl font-bold text-slate-800">☁️ Supported Cloud Platforms</h2>
                </div>
                <div className="space-y-4">
                  {cloudPlatforms.map((platform, i) => (
                    <div key={i} className="flex items-center gap-4 p-3 rounded-xl border border-slate-100 bg-slate-50/50 hover:bg-white hover:border-slate-200 hover:shadow-sm transition-all duration-300">
                      <div className={`w-3.5 h-3.5 rounded-full bg-gradient-to-r ${platform.color} shrink-0 shadow-sm`} />
                      <div className="space-y-0.5">
                        <h4 className="font-bold text-slate-800 text-sm">{platform.name}</h4>
                        <p className="text-xs text-slate-500 font-medium leading-relaxed">{platform.desc}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>

          </div>

          {/* Pipeline Diagram Card */}
          <div className="rounded-2xl border border-slate-200/80 bg-white p-6 md:p-8 shadow-sm hover:shadow-md transition-all duration-300">
            <div className="flex items-center gap-3 mb-8">
              <div className="p-2.5 rounded-lg bg-purple-50 border border-purple-100 text-purple-600">
                <Layers className="w-6 h-6" />
              </div>
              <h2 className="text-xl font-bold text-slate-800">⚙️ Optimization Pipeline</h2>
            </div>
            
            {/* Visual Pipeline flow */}
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-7 gap-4 relative">
              {pipelineSteps.map((step, i) => {
                const Icon = step.icon;
                return (
                  <div key={i} className="flex flex-col items-center text-center relative group">
                    {/* Step number badge */}
                    <div className="absolute -top-2 -left-2 w-5 h-5 rounded-full bg-slate-100 border border-slate-200 text-slate-600 flex items-center justify-center text-[10px] font-bold">
                      {i + 1}
                    </div>
                    
                    {/* Step Icon container */}
                    <div className="w-12 h-12 rounded-xl bg-slate-50 border border-slate-100 shadow-sm flex items-center justify-center text-slate-600 group-hover:scale-110 group-hover:bg-blue-50 group-hover:border-blue-200 group-hover:text-blue-600 transition-all duration-300">
                      <Icon className="w-5.5 h-5.5" />
                    </div>
                    
                    {/* Step Labels */}
                    <h4 className="font-bold text-slate-800 text-xs mt-3 leading-snug">{step.name}</h4>
                    <p className="text-[10px] text-slate-500 font-medium mt-1 leading-relaxed max-w-[120px] hidden sm:block">
                      {step.desc}
                    </p>

                    {/* Right Arrow (only visible between steps on large screens) */}
                    {i < pipelineSteps.length - 1 && (
                      <div className="hidden md:flex absolute top-4 -right-3 text-slate-300">
                        <ArrowRight className="w-4 h-4" />
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>

          {/* Grid: Tech Stack & Optimization Technologies */}
          <div className="grid md:grid-cols-2 gap-8">
            
            {/* Tech Stack Card */}
            <div className="rounded-2xl border border-slate-200/80 bg-white p-6 shadow-sm hover:shadow-md transition-all duration-300">
              <div className="flex items-center gap-3 mb-6">
                <div className="p-2.5 rounded-lg bg-blue-50 border border-blue-100 text-blue-600">
                  <Layers className="w-6 h-6" />
                </div>
                <h2 className="text-xl font-bold text-slate-800">📊 Tech Stack</h2>
              </div>
              <div className="space-y-5">
                <div>
                  <h4 className="font-bold text-xs uppercase tracking-wider text-blue-700 mb-2">Frontend</h4>
                  <div className="flex flex-wrap gap-2">
                    {techStack.frontend.map((tech, i) => (
                      <span key={i} className="px-3 py-1 rounded-full text-xs font-semibold bg-blue-50/50 border border-blue-100/80 text-blue-700">
                        {tech}
                      </span>
                    ))}
                  </div>
                </div>
                <div>
                  <h4 className="font-bold text-xs uppercase tracking-wider text-green-700 mb-2">Backend</h4>
                  <div className="flex flex-wrap gap-2">
                    {techStack.backend.map((tech, i) => (
                      <span key={i} className="px-3 py-1 rounded-full text-xs font-semibold bg-green-50/50 border border-green-100/80 text-green-700">
                        {tech}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            </div>

            {/* Optimization Technologies Card */}
            <div className="rounded-2xl border border-slate-200/80 bg-white p-6 shadow-sm hover:shadow-md transition-all duration-300">
              <div className="flex items-center gap-3 mb-6">
                <div className="p-2.5 rounded-lg bg-orange-50 border border-orange-100 text-orange-600">
                  <Cpu className="w-6 h-6" />
                </div>
                <h2 className="text-xl font-bold text-slate-800">🧠 Supported Optimization Technologies</h2>
              </div>
              <div className="flex flex-wrap gap-2.5">
                {optimizationTech.map((tech, i) => (
                  <span key={i} className="px-3 py-1.5 rounded-xl text-xs font-semibold bg-orange-50/50 border border-orange-100 text-orange-700">
                    {tech}
                  </span>
                ))}
              </div>
            </div>

          </div>

          {/* Project Information */}
          <div className="rounded-2xl border border-slate-200/80 bg-white p-6 shadow-sm hover:shadow-md transition-all duration-300">
            <div className="flex items-center gap-3 mb-6">
              <div className="p-2.5 rounded-lg bg-slate-100 border border-slate-200 text-slate-600">
                <Info className="w-6 h-6" />
              </div>
              <h2 className="text-xl font-bold text-slate-800">📄 Project Information</h2>
            </div>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-sm">
              <div className="p-4 rounded-xl border border-slate-50 bg-slate-50/30">
                <span className="text-xs text-slate-400 font-bold uppercase tracking-wider block">Project</span>
                <span className="font-extrabold text-slate-800 block mt-1">OptiMind AI</span>
              </div>
              <div className="p-4 rounded-xl border border-slate-50 bg-slate-50/30">
                <span className="text-xs text-slate-400 font-bold uppercase tracking-wider block">Version</span>
                <span className="font-extrabold text-slate-800 block mt-1">v1.0.0</span>
              </div>
              <div className="p-4 rounded-xl border border-slate-50 bg-slate-50/30">
                <span className="text-xs text-slate-400 font-bold uppercase tracking-wider block">License</span>
                <span className="font-extrabold text-slate-800 block mt-1">MIT License</span>
              </div>
              <div className="p-4 rounded-xl border border-slate-50 bg-slate-50/30">
                <span className="text-xs text-slate-400 font-bold uppercase tracking-wider block">Repository</span>
                <a 
                  href="https://github.com/Nimalan07/optimind-ai" 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="inline-flex items-center gap-1.5 font-extrabold text-blue-600 hover:text-blue-800 mt-1 transition-colors"
                >
                  <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path><path d="M9 18c-4.51 2-5-2-7-2"></path></svg>
                  GitHub
                  <ExternalLink className="w-3 h-3" />
                </a>
              </div>
            </div>
          </div>

          {/* Footer Accent */}
          <footer className="text-center py-6 border-t border-slate-200/80 mt-12">
            <p className="text-sm font-extrabold bg-gradient-to-r from-blue-700 to-green-700 bg-clip-text text-transparent">
              Built for the Arm AI Optimization Challenge 2026
            </p>
          </footer>

        </main>
      </div>
    </>
  );
}
