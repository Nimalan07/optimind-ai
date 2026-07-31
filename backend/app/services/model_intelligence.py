import os
import json


class ModelIntelligence:

    @staticmethod
    def inspect(model_path: str):

        config_path = os.path.join(model_path, "config.json")

        if not os.path.exists(config_path):

            return {
                "error": "config.json not found"
            }

        with open(config_path, "r") as f:

            config = json.load(f)

        architecture = config.get("architectures", ["Unknown"])[0]

        hidden_size = config.get("hidden_size", "Unknown")

        layers = config.get("num_hidden_layers", "Unknown")

        heads = config.get("num_attention_heads", "Unknown")

        vocab = config.get("vocab_size", "Unknown")

        dtype = config.get("torch_dtype", "Unknown")

        # Normalize architecture name
        arch_mapped = architecture
        arch_lower = architecture.lower()
        for k in ["bert", "roberta", "distilbert", "llama", "mistral", "phi", "gemma", "t5", "whisper"]:
            if k in arch_lower:
                arch_mapped = k
                break

        # Estimate parameters in billions
        parameters_b = 0.0
        if isinstance(hidden_size, int) and isinstance(layers, int):
            vocab_val = vocab if isinstance(vocab, int) else 32000
            params = (vocab_val * hidden_size) + (12 * (hidden_size ** 2) * layers)
            parameters_b = round(params / 1e9, 2)
            
            # Exact matches for standard models
            if "bert" in arch_lower and hidden_size == 768 and layers == 12:
                parameters_b = 0.11
            elif "llama" in arch_lower and hidden_size == 4096 and layers == 32:
                parameters_b = 6.74

        # Estimate RAM usage in GB (approx 4x parameters for FP32/original)
        ram_gb = round(parameters_b * 4, 1) if parameters_b > 0 else 0.0

        return {

            "architecture": arch_mapped,

            "hidden_size": hidden_size,

            "layers": layers,

            "attention_heads": heads,

            "vocab_size": vocab,

            "dtype": dtype,

            "estimated_parameters_billion": parameters_b,

            "estimated_ram_gb": ram_gb

        }