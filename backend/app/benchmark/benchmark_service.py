from app.benchmark.benchmark_runner import BenchmarkRunner
from app.benchmark.comparison import BenchmarkComparison


class BenchmarkService:

    @staticmethod
    def run_benchmark(model_path, inference_function=None, sample_input=None):
        return BenchmarkRunner.benchmark(model_path, inference_function, sample_input)

    @staticmethod
    def compare_benchmarks(before, after):
        return BenchmarkComparison.compare(before, after)
