from app.optimization.plugins.onnx_plugin import ONNXPlugin
from app.optimization.plugins.quantization_plugin import QuantizationPlugin



class OptimizerFactory:

    @staticmethod
    def get_plugins():

        return [

            ONNXPlugin(),

            QuantizationPlugin(),


        ]