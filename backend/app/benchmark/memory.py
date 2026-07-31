import psutil
import os


class MemoryBenchmark:

    @staticmethod
    def measure():

        process = psutil.Process(os.getpid())

        memory = process.memory_info()

        return {

            "rss_mb": round(memory.rss / (1024**3) * 1024, 2),

            "vms_mb": round(memory.vms / (1024**3) * 1024, 2)

        }

    @staticmethod
    def usage():
        return MemoryBenchmark.measure()["rss_mb"]