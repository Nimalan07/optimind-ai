from app.optimization.executors.quantization_executor import QuantizationExecutor
from app.optimization.plugins.base_plugin import BasePlugin


class QuantizationPlugin(BasePlugin):

    name = "Quantization"
    stage = "INT8 Dynamic Quantization"

    @staticmethod
    def supports(inspection):
        architecture = inspection["architecture"].lower()

        supported = [
            "bert",
            "distilbert",
            "roberta",
            "t5",
            "llama",
            "phi",
            "whisper",
        ]

        return any(model in architecture for model in supported)

    @staticmethod
    def optimize(model_path: str):
        return QuantizationExecutor.execute(model_path)