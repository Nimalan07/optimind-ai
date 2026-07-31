import platform
import psutil


class CPUDetector:

    @staticmethod
    def profile():

        freq = psutil.cpu_freq()

        return {
            "processor": platform.processor() or platform.machine(),
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
            "max_frequency_mhz": round(freq.max, 2) if freq else None,
            "current_frequency_mhz": round(freq.current, 2) if freq else None,
            "architecture": platform.machine()
        }
