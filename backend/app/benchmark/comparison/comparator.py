from app.benchmark.comparison.metrics import BenchmarkMetrics


class BenchmarkComparator:

    @staticmethod
    def compare(
        original: BenchmarkMetrics,
        optimized: BenchmarkMetrics
    ):

        def percentage_reduction(original_value, optimized_value):
            if original_value <= 0:
                return 0.0
            return ((original_value - optimized_value) / original_value) * 100

        def throughput_improvement(original_value, optimized_value):
            if original_value <= 0:
                return 0.0
            return ((optimized_value - original_value) / original_value) * 100

        latency_improvement = percentage_reduction(
            original.latency,
            optimized.latency
        )

        memory_reduction = percentage_reduction(
            original.memory,
            optimized.memory
        )

        cpu_reduction = percentage_reduction(
            original.cpu,
            optimized.cpu
        )

        size_reduction = percentage_reduction(
            original.size,
            optimized.size
        )

        throughput_gain = throughput_improvement(
            original.throughput,
            optimized.throughput
        )

        return {

            "original": original.to_dict(),

            "optimized": optimized.to_dict(),

            "improvements": {

                "latency_improvement":
                    round(latency_improvement, 2),

                "memory_reduction":
                    round(memory_reduction, 2),

                "cpu_reduction":
                    round(cpu_reduction, 2),

                "size_reduction":
                    round(size_reduction, 2),

                "throughput_gain":
                    round(throughput_gain, 2)

            }

        }


class BenchmarkComparison:

    @staticmethod
    def compare(before, after):

        def improvement(old, new):

            if old == 0:
                return 0

            return round(((old - new) / old) * 100, 2)

        return {

            "latency_improvement_percent":

                improvement(

                    before["latency"]["average_ms"],

                    after["latency"]["average_ms"]

                ),

            "memory_improvement_percent":

                improvement(

                    before["memory"]["rss_mb"],

                    after["memory"]["rss_mb"]

                ),

            "model_size_improvement_percent":

                improvement(

                    before["size"]["mb"],

                    after["size"]["mb"]

                )

        }