import psutil


class MemoryDetector:

    @staticmethod
    def profile():

        memory = psutil.virtual_memory()

        return {

            "total_gb": round(memory.total / (1024**3), 2),

            "available_gb": round(memory.available / (1024**3), 2),

            "used_percent": memory.percent

        }
