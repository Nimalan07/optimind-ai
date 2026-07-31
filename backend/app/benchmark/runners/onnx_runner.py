import os
import time

import numpy as np
import onnxruntime as ort
import psutil

from app.benchmark.comparison.metrics import BenchmarkMetrics


class ONNXRunner:

    @staticmethod
    def run(model_path: str):

        process = psutil.Process(os.getpid())

        session = ort.InferenceSession(
            model_path,
            providers=["CPUExecutionProvider"]
        )

        inputs = {}

        for inp in session.get_inputs():

            shape = [
                d if isinstance(d, int) else 1
                for d in inp.shape
            ]

            if inp.type == "tensor(int64)":
                arr = np.ones(shape, dtype=np.int64)

            elif inp.type == "tensor(int32)":
                arr = np.ones(shape, dtype=np.int32)

            elif inp.type == "tensor(float)":
                arr = np.ones(shape, dtype=np.float32)

            else:
                arr = np.ones(shape, dtype=np.float32)

            inputs[inp.name] = arr

        # Warm-up
        for _ in range(3):
            session.run(None, inputs)

        # Reset CPU measurement
        psutil.cpu_percent(interval=None)

        runs = 20

        start = time.perf_counter()

        for _ in range(runs):
            session.run(None, inputs)

        end = time.perf_counter()

        latency = ((end - start) / runs) * 1000

        throughput = runs / (end - start)

        # Current memory usage (GB)
        memory = process.memory_info().rss / (1024 ** 3)

        cpu = psutil.cpu_percent(interval=0.1)

        # ONNX file size (GB)
        size = os.path.getsize(model_path) / (1024 ** 3)

        return BenchmarkMetrics(
            latency=round(latency, 2),
            memory=round(memory, 3),
            cpu=round(cpu, 2),
            size=round(size, 3),
            throughput=round(throughput, 2),
        )