from app.optimization.executors.onnx_executor import ONNXExecutor
from app.optimization.plugins.base_plugin import BasePlugin

class ONNXPlugin(BasePlugin):
    def supports(self, inspection):

        architecture = inspection["architecture"]

        supported = [

            "Phi3ForCausalLM",

            "BertModel",

            "BertForMaskedLM",

            "DistilBertModel",

            "WhisperForConditionalGeneration"

        ]

        return architecture in supported

    from app.optimization.executors.onnx_executor import ONNXExecutor

    def optimize(self, model_path):

        result = ONNXExecutor.execute(model_path)

        return {

            "plugin": "ONNX",

            "stage": "Export to ONNX",

            **result

        }