import time


class LatencyBenchmark:

    @staticmethod
    def measure(func, *args, warmup=3, runs=20):

        for _ in range(warmup):
            try:
                func(*args)
            except Exception:
                pass

        timings = []

        for _ in range(runs):

            start = time.perf_counter()

            try:
                func(*args)
            except Exception:
                pass

            end = time.perf_counter()

            timings.append((end - start) * 1000)

        if not timings:
            timings = [0.0]

        avg = sum(timings) / len(timings)

        return {

            "average_ms": round(avg, 3),

            "min_ms": round(min(timings), 3),

            "max_ms": round(max(timings), 3)

        }