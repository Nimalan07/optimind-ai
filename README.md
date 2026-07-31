# OptiMind AI (Cloud AI Platform)

Welcome to **OptiMind AI**, an agentic developer platform built to inspect, profile, recommend, optimize, and bundle AI models for deployment on modern Arm-based Cloud CPU architectures (such as **AWS Graviton**, **Microsoft Cobalt 100**, and **Google Cloud Axion**).

This platform acts as an end-to-end sandbox enabling developers to compile models (e.g., Llama, Phi, Gemma, BERT) to high-performance runtimes (ONNX Runtime, Llama.cpp) with dynamic quantization, analyze cost-efficiency metrics, and instantly generate production-ready cloud deployment packages.

---

## 🚀 Key Features

### 1. Zero-Lag Model Selection & Inspection
* Search and load any Hugging Face Repository instantly.
* **Metadata Lazy-Loading**: Recommendations fetch only the `config.json` header (taking milliseconds and using <2KB) to identify attention heads, layers, and architectures. Heavy model weights are deferred to the actual compilation stage to preserve system memory and network bandwidth.

### 2. AI Recommendation Heuristic
* Recommends the optimal inference engine based on architecture (e.g., **ONNX Runtime** for Bert classification, **Llama.cpp** for Llama text-generation).
* Recommends the most cost-efficient instance on AWS, Azure, or GCP.
* Dynamically calculates **Estimated Hosting Costs** using real-world public cloud billing rates (e.g., AWS Graviton on-demand rates of \$48.96/mo).

### 3. Dynamic Model-Aware Benchmarking
* Features dynamic benchmarking simulations scaled realistically according to parameter sizes and runtime engines. 
* Reflects realistic RAM savings (up to 75% for LLM INT4 quantization) and speedups (2x - 4x) with built-in model-specific variance.

### 4. Bypassed Native Download Packages
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
* **Libraries**: Hugging Face Hub (downloader/exporter), Optimum, Pydantic.
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

---

## 📂 Repository Layout

```text
├── backend/
│   ├── app/
│   │   ├── api/            # API endpoints (models, pipeline, reports, cloud)
│   │   ├── benchmark/      # Memory, latency, throughput measurement suites
│   │   ├── deployment/     # Container & orchestrator code generators
│   │   ├── download/       # HF Hub downloader strategy and profiles
│   │   ├── pipeline/       # Optimization multi-stage pipeline state machine
│   │   └── recommendation/ # Backend and cloud recommender systems
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── app/            # Next.js workspace routing (models, optimize, benchmark, reports)
│   │   ├── components/     # UI layouts (Navbar, Sidebar, shadcn Cards/Buttons)
│   │   └── services/       # API clients
│   └── package.json
└── .gitignore              # Main project git exclusion list
```
