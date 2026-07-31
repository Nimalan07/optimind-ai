class CloudRecommender:

    @staticmethod
    def recommend(backend: str):

        backend = backend.lower()

        if backend == "onnx runtime":

            return {
                "provider": "AWS",
                "instance": "c8g.large",
                "processor": "Graviton4",
                "reason": [
                    "Arm CPU",
                    "ONNX Runtime supported",
                    "Low deployment cost"
                ]
            }

        if backend == "llama.cpp":

            return {
                "provider": "AWS",
                "instance": "c8g.2xlarge",
                "processor": "Graviton4",
                "reason": [
                    "CPU optimized",
                    "GGUF acceleration"
                ]
            }

        return {
            "provider": "AWS",
            "instance": "c7i.large",
            "processor": "Intel Xeon",
            "reason": [
                "Generic deployment"
            ]
        }
