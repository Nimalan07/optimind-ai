from pathlib import Path
import json


class ModelFamily:

    @staticmethod
    def detect(model_path: str):

        config = Path(model_path) / "config.json"

        if not config.exists():
            return "unknown"

        try:

            with open(config, "r", encoding="utf-8") as f:
                cfg = json.load(f)

            architectures = cfg.get("architectures", [])

            if architectures:

                arch = architectures[0]

                if any(
                    x in arch.lower()
                    for x in [
                        "bert",
                        "gpt",
                        "phi",
                        "llama",
                        "whisper",
                        "t5",
                        "roberta",
                    ]
                ):
                    return "huggingface"

            return "pytorch"

        except Exception:

            return "unknown"