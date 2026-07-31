from app.benchmark.benchmark_runner import BenchmarkRunner
from app.benchmark.comparison import (
    BenchmarkComparator,
    BenchmarkReport,
)


class BenchmarkStage:

    @staticmethod
    def run(
        original_model_path: str,
        optimized_model_path: str,
        backend: str,
    ):

        original = BenchmarkRunner.run(
            original_model_path,
            "PyTorch"
        )

        optimized = BenchmarkRunner.run(
            optimized_model_path,
            backend
        )

        comparison = BenchmarkComparator.compare(
            original,
            optimized
        )

        return BenchmarkReport.generate(
            comparison
        )