class BackendRecommender:

    @staticmethod
    def recommend(inspection: dict):

        architecture = inspection.get("architecture", "").lower()
        parameters = inspection.get("estimated_parameters_billion", 0)

        # Large language models
        if any(x in architecture for x in ["llama", "mistral", "phi", "gemma"]):

            if parameters <= 7:
                return {
                    "backend": "ONNX Runtime",
                    "reason": [
                        "CPU optimized",
                        "Supports transformer inference",
                        "Best latency on cloud CPUs"
                    ]
                }

            return {
                "backend": "llama.cpp",
                "reason": [
                    "Large LLM",
                    "GGUF quantization supported",
                    "Excellent CPU inference"
                ]
            }

        # Encoder models
        if any(x in architecture for x in [
            "bert",
            "roberta",
            "distilbert",
            "t5",
            "whisper"
        ]):

            return {
                "backend": "ONNX Runtime",
                "reason": [
                    "Transformer encoder model",
                    "Supports dynamic quantization",
                    "Fast CPU inference"
                ]
            }

        return {
            "backend": "PyTorch",
            "reason": [
                "No optimized backend available"
            ]
        }
