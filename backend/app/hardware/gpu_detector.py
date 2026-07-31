import importlib.util


class GPUDetector:

    @staticmethod
    def profile():

        if importlib.util.find_spec("torch") is None:
            return {
                "available": False,
                "reason": "PyTorch not installed"
            }

        import torch

        if not torch.cuda.is_available():
            return {
                "available": False,
                "reason": "CUDA not available"
            }

        return {

            "available": True,

            "device": torch.cuda.get_device_name(0),

            "memory_gb": round(
                torch.cuda.get_device_properties(0).total_memory / (1024**3),
                2
            )
        }
