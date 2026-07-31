from app.hardware.cpu_detector import CPUDetector
from app.hardware.memory_detector import MemoryDetector
from app.hardware.os_detector import OSDetector
from app.hardware.arm_detector import ARMDetector
from app.hardware.gpu_detector import GPUDetector


class RuntimeProfiler:

    @staticmethod
    def profile():

        return {

            "cpu": CPUDetector.profile(),

            "memory": MemoryDetector.profile(),

            "os": OSDetector.profile(),

            "arm": ARMDetector.detect(),

            "gpu": GPUDetector.profile()

        }
