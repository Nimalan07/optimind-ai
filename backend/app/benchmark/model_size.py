import os
from pathlib import Path


class ModelSizeBenchmark:

    @staticmethod
    def measure(path: str):

        total = 0
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    try:
                        total += os.path.getsize(os.path.join(root, file))
                    except OSError:
                        pass
        else:
            try:
                total = Path(path).stat().st_size
            except OSError:
                total = 0

        return {

            "bytes": total,

            "mb": round(total / (1024 * 1024), 2)

        }

    @staticmethod
    def size(path: str):
        return ModelSizeBenchmark.measure(path)["mb"]