class DecisionEngine:

    @staticmethod
    def choose_backend(inspection):

        architecture = inspection.get("architecture", "").lower()

        if architecture == "bert":
            return "ONNX Runtime"

        if architecture == "llama":
            return "llama.cpp"

        return "PyTorch"
