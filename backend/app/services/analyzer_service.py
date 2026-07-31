import os


class AnalyzerService:

    @staticmethod
    def analyze(path: str):

        total = 0

        for root, _, files in os.walk(path):

            for file in files:

                total += os.path.getsize(
                    os.path.join(root, file)
                )

        return {

            "size_mb": round(total / (1024 * 1024), 2),

            "path": path,

            "files": len(os.listdir(path))

        }