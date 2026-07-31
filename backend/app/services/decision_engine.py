import math


class DecisionEngine:

    @staticmethod
    def estimate_parameters(hidden_size, layers):

        if hidden_size == "Unknown" or layers == "Unknown":
            return None

        # Approximate transformer parameter count
        params = 12 * (hidden_size ** 2) * layers

        return round(params / 1e9, 2)

    @staticmethod
    def estimate_ram(parameters):

        if parameters is None:
            return "Unknown"

        return round(parameters * 2, 1)

    @staticmethod
    def choose_backend(architecture):

        architecture = architecture.lower()

        if "llama" in architecture:
            return "llama.cpp"

        if "mistral" in architecture:
            return "llama.cpp"

        if "phi" in architecture:
            return "ONNX Runtime"

        if "bert" in architecture:
            return "ONNX Runtime"

        if "vit" in architecture:
            return "ONNX Runtime"

        return "PyTorch"

    @staticmethod
    def choose_quantization(parameters, backend):

        if backend == "ONNX Runtime":

            if parameters is None:
                return "INT8 Dynamic"

            if parameters > 7:
                return "INT8 Static"

            return "INT8 Dynamic"

        if backend == "llama.cpp":

            if parameters is None:
                return "Q4_K_M"

            if parameters > 20:
                return "Q4_K_M"

            if parameters > 7:
                return "Q5_K_M"

            return "Q8_0"

        return "None"

    @staticmethod
    def estimate_speedup(backend):

        mapping = {

            "llama.cpp": "2.8x",

            "ONNX Runtime": "2.3x",

            "PyTorch": "1.0x"

        }

        return mapping.get(backend)

    @staticmethod
    def estimate_memory_reduction(quantization):

        mapping = {

            "Q4_K_M": "70%",

            "Q5_K_M": "60%",

            "Q8_0": "45%",

            "INT8": "55%"

        }

        return mapping.get(quantization)

    @classmethod
    def recommend(cls, info):

        architecture = info["architecture"]

        hidden = info["hidden_size"]

        layers = info["layers"]

        parameters = cls.estimate_parameters(hidden, layers)

        backend = cls.choose_backend(architecture)

        quantization = cls.choose_quantization(
    parameters,
    backend
)

        return {

            "estimated_parameters_billion": parameters,

            "estimated_ram_gb": cls.estimate_ram(parameters),

            "recommended_backend": backend,

            "recommended_quantization": quantization,

            "expected_speedup": cls.estimate_speedup(backend),

            "memory_reduction": cls.estimate_memory_reduction(
                quantization
            )

        }