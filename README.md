# OptiMind AI (Cloud AI Platform)

Welcome to **OptiMind AI**, a production-grade, agentic developer platform built to inspect, profile, recommend, optimize, and bundle AI models for deployment on modern Arm-based Cloud CPU architectures (such as **AWS Graviton**, **Microsoft Cobalt 100**, and **Google Cloud Axion**).

The application acts as an end-to-end sandbox enabling developers to compile models (e.g., Llama, Phi, Gemma, BERT) to high-performance runtimes (ONNX Runtime, Llama.cpp) with dynamic quantization, analyze cost-efficiency metrics, and instantly generate production-ready cloud deployment packages.

---

## 📂 Detailed Folder Structure

Here is the complete file and folder architecture of the OptiMind AI monorepo:

```text
optimised/
├── backend/
│   ├── app/
│   │   ├── api/                      # REST API Endpoint Routers
│   │   │   ├── agent.py              # Natural language agent optimization triggers
│   │   │   ├── artifacts.py          # Serves HTML sheets and deployment ZIP packages
│   │   │   ├── benchmark.py          # Hardware benchmarking endpoints
│   │   │   ├── cloud.py              # Cloud instance recommendation endpoint
│   │   │   ├── deployment.py         # Deployment configuration generation endpoints
│   │   │   ├── hardware.py           # On-prem CPU/GPU detection endpoint
│   │   │   ├── jobs.py               # Background job tracking and registry
│   │   │   ├── models.py             # Popular models and search endpoints
│   │   │   ├── optimization.py       # Quantization configurations endpoints
│   │   │   ├── recommendation.py     # Unified backend, hardware, and cost recommendation
│   │   │   ├── reports.py            # Latency speedup PDF/HTML report generators
│   │   │   └── system.py             # Root message and health check endpoint
│   │   ├── benchmark/                # Telemetry & Performance Suites
│   │   │   ├── benchmark_runner.py   # Simulates model-aware latency/throughput/RSS metrics
│   │   │   ├── benchmark_service.py  # Coordinates benchmark execution jobs
│   │   │   ├── comparison.py         # Calculates delta improvements between runs
│   │   │   ├── latency.py            # Local latency measurement logic
│   │   │   ├── memory.py             # RSS/VMS memory usage monitors
│   │   │   ├── model_size.py         # Inspects physical storage footprints of weights
│   │   │   ├── throughput.py         # Computes tokens/sec and request throughput rates
│   │   │   └── utils.py              # Telemetry helper utilities
│   │   ├── cloud/                    # Cloud Catalog & Selection
│   │   │   ├── cloud_catalog.py      # Database of AWS Graviton, Azure Cobalt, & GCP Axion VMs
│   │   │   ├── cloud_service.py      # Instance query service
│   │   │   ├── deployment_estimator.py# Estimates scale, threads, and container limits
│   │   │   ├── instance_selector.py  # Maps model specifications to optimal VM sizes
│   │   │   └── provider_ranker.py    # Ranks AWS, GCP, and Azure by efficiency/cost
│   │   ├── deployment/               # Cloud Infrastructure Codegen
│   │   │   ├── compose_generator.py  # Builds compose stacks with server and nginx containers
│   │   │   ├── deployment_service.py # Compiles configs and zips the deployment assets
│   │   │   ├── docker_generator.py   # Generates Arm64-optimized Dockerfiles
│   │   │   ├── kubernetes_generator.py# Generates Kubernetes deployment and service YAMLs
│   │   │   ├── nginx_generator.py    # Builds Nginx reverse-proxy load balancers
│   │   │   ├── startup_generator.py  # Generates bash script setup scripts for VMs
│   │   │   └── templates.py          # Asset base templates
│   │   ├── download/                 # Model Ingestion Strategy
│   │   │   ├── downloader.py         # Hugging Face model downloader (full vs config-only)
│   │   │   ├── profiles.py           # Pattern filters (ONNX, PyTorch, Llama.cpp)
│   │   │   └── strategy.py           # Decides which files to fetch based on backend
│   │   ├── pipeline/                 # Stage-Based Orchestrator
│   │   │   ├── pipeline.py           # Runs the optimization pipeline state machine
│   │   │   ├── pipeline_context.py   # Stores metadata, model paths, and logs
│   │   │   ├── pipeline_result.py    # Data structure returning optimization records
│   │   │   ├── pipeline_service.py   # Spawns background worker tasks
│   │   │   └── stages/               # Individual Pipeline Steps
│   │   │       ├── benchmark_stage.py   # Benchmarks base vs optimized models
│   │   │       ├── deployment_stage.py  # Generates deployment packages
│   │   │       ├── download_stage.py    # Fetches model files from HF Hub
│   │   │       ├── inspection_stage.py  # Parses architecture, layer counts, and heads
│   │   │       ├── optimization_stage.py# Triggers optimum-cli compilation/quantization
│   │   │       ├── recommendation_stage.# Resolves cloud VM sizing and configurations
│   │   │       └── report_stage.py      # Generates output PDF/HTML documents
│   │   ├── recommendation/           # AI Decision Engines
│   │   │   ├── backend_recommender.py# Recommends ONNX Runtime or Llama.cpp
│   │   │   ├── cloud_recommender.py  # Matches runtime with AWS/Azure/GCP VMs
│   │   │   ├── hardware_recommender.py# Detects local processor features
│   │   │   └── optimization_planner.py# Plans quantization levels (INT4/INT8/FP16)
│   │   └── reports/                  # Report Compilation Services
│   │       ├── charts.py             # Generates telemetry bar charts in base64
│   │       ├── html_generator.py     # Generates interactive HTML report sheets
│   │       └── pdf_generator.py      # Compiles ReportLab PDF documents with charts
│   └── main.py                       # FastAPI application entryway
├── frontend/
│   ├── public/                       # Static Website Assets
│   │   ├── favicon.svg               # Scalable logo used as tab favicon
│   │   └── logo.png                  # Original logo with branding text
│   ├── src/
│   │   ├── app/                      # Next.js App Router Page Layouts
│   │   │   ├── about/                # Product details and version information
│   │   │   ├── history/              # View logs of past runs
│   │   │   ├── settings/             # Environment variables and API token configuration
│   │   │   ├── workspace/            # Application Workspace Pages
│   │   │   │   ├── benchmark/        # Performance charts, tables, and CSV exports
│   │   │   │   ├── models/           # Model search, preloaded selection, and query page
│   │   │   │   ├── optimize/         # Optimization configs, recommendations, and execution
│   │   │   │   └── report/           # Download PDF/ZIP and preview HTML reports
│   │   │   ├── globals.css           # Global CSS variables & Tailwind directives
│   │   │   ├── icon.svg              # Tab icon reference
│   │   │   └── layout.tsx            # Root HTML layout with title metadata
│   │   ├── components/               # Shareable Layout components
│   │   │   └── layout/
│   │   │       ├── Navbar.tsx        # Branded header with logo & gradient typography
│   │   │       └── Sidebar.tsx       # Sidebar navigation for Workspace pages
│   │   ├── services/
│   │   │   └── api.ts                # API client configuration pointing to Backend
│   │   ├── components.json           # Tailwind shadcn configurations
│   │   ├── package.json              # Frontend package registry
│   │   └── tsconfig.json             # TypeScript compiler rules
└── .gitignore                        # Root gitignore excluding caches and model weights
```

---

## 🚀 Key Features

### 1. Lazy-Ingestion Model Selection
* Search and load any Hugging Face Repository instantly.
* **Metadata Lazy-Loading**: Recommendations fetch only the `config.json` header (taking milliseconds and using <2KB) to identify attention heads, layers, and architectures. Heavy model weights are deferred to the actual compilation stage to preserve system memory and network bandwidth.

### 2. AI Recommendation Heuristic
* Recommends the optimal inference engine based on architecture (e.g., **ONNX Runtime** for Bert classification, **Llama.cpp** for Llama text-generation).
* Recommends the most cost-efficient instance on AWS, Azure, or GCP.
* Dynamically calculates **Estimated Hosting Costs** using real-world public cloud billing rates (e.g., AWS Graviton on-demand rates of \$48.96/mo).

### 3. Dynamic Model-Aware Benchmarking
* Features dynamic benchmarking simulations scaled realistically according to parameter sizes and runtime engines. 
* Reflects realistic RAM savings (up to 75% for LLM INT4 quantization) and speedups (2x - 4x) with built-in model-specific variance.

### 4. Interactive Cancel Button
* Includes a fully functional **Cancel Optimization** button in the workspace UI that cleanly aborts active fetch requests mid-flight and safely halts the pipeline without runtime crashes.

### 5. Bypassed Native Download Packages
* Replaced programmatic Javascript links with native standard HTML anchors styled via shadcn/base-ui `buttonVariants`.
* **Download PDF Report**: Generates a detailed audit of latency speedups and architecture details.
* **Download Deployment ZIP**: Automatically bundles containerized deployment assets:
  - Custom `Dockerfile` optimized for Arm CPU instruction sets.
  - `docker-compose.yml` for multi-container orchestration.
  - `nginx.conf` configured for request reverse-proxying.
  - Kubernetes `deployment.yaml` and `service.yaml` manifests for hosting.
* **Open HTML Report**: Opens a clean, responsive layout of the report inside a new tab.

---

## 🛠️ Tech Stack

### Frontend (Next.js)
* **Core**: Next.js 15 (App Router), React, TypeScript.
* **Styling**: Tailwind CSS & Base-UI/Radix primitives.
* **Icons**: Lucide React.

### Backend (FastAPI)
* **Framework**: FastAPI (Python 3.13), Uvicorn.
* **Libraries**: Hugging Face Hub (downloader/exporter), Optimum, Pydantic, ReportLab.
* **Telemetry**: Native profiling, memory measurement, and performance estimation.

---

## ⚙️ How to Get Started

### Prerequisites
* **Node.js** (v18 or higher)
* **Python** (v3.10 - v3.13)

### 1. Run the Backend
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server with reload enabled:
   ```bash
   uvicorn app.main:app --reload
   ```
   *The backend will boot up at `http://127.0.0.1:8000`.*

### 2. Run the Frontend
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```
2. Install Node packages:
   ```bash
   npm install
   ```
3. Boot the development server:
   ```bash
   npm run dev
   ```
   *The frontend dashboard will load at `http://localhost:3000`.*
