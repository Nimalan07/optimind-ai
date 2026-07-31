import os
import time
from pathlib import Path

import psutil
import torch
from transformers import AutoModel, AutoTokenizer

from app.benchmark.comparison.metrics import BenchmarkMetrics


class PyTorchRunner:

    @staticmethod
    def run(model_path: str):

        process = psutil.Process(os.getpid())

        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModel.from_pretrained(model_path)

        model.eval()

        inputs = tokenizer(
            "Hello, this is a benchmark test.",
            return_tensors="pt",
        )

        # Warm-up
        with torch.no_grad():
            for _ in range(3):
                model(**inputs)

        # Reset CPU measurement
        psutil.cpu_percent(interval=None)

        runs = 20

        start = time.perf_counter()

        with torch.no_grad():
            for _ in range(runs):
                model(**inputs)

        end = time.perf_counter()

        latency = ((end - start) / runs) * 1000

        throughput = runs / (end - start)

        # Current process memory (GB)
        memory = process.memory_info().rss / (1024 ** 3)

        cpu = psutil.cpu_percent(interval=0.1)

        size = sum(
            f.stat().st_size
            for f in Path(model_path).rglob("*")
            if f.is_file()
        ) / (1024 ** 3)

        return BenchmarkMetrics(
            latency=round(latency, 2),
            memory=round(memory, 3),
            cpu=round(cpu, 2),
            size=round(size, 3),
            throughput=round(throughput, 2),
        )