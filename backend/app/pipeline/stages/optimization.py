from app.optimization.executors.onnx_executor import ONNXExecutor


class OptimizationStage:

    @staticmethod
    def run(model_path):

        return ONNXExecutor.execute(

            model_path

        )