from app.optimization.executors.onnx_executor import ONNXExecutor


class OptimizationStage:

    def run(self, context):
        context.metadata["progress"]["optimization"] = "running"
        context.optimization = ONNXExecutor.execute(context.model_path)
        context.metadata["progress"]["optimization"] = "completed"
