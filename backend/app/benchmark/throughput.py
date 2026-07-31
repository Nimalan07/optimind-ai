import time


class ThroughputBenchmark:

    @staticmethod
    def measure(func, *args, duration=2): # Use a smaller default duration like 2 seconds to keep benchmarks fast!

        count = 0

        start = time.perf_counter()

        while True:

            try:
                func(*args)
            except Exception:
                pass

            count += 1

            if time.perf_counter() - start >= duration:
                break

        elapsed = time.perf_counter() - start
        throughput = count / elapsed if elapsed > 0 else 0

        return {

            "requests_per_second": round(throughput, 2)

        }