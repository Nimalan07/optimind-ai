from app.services.model_intelligence import ModelIntelligence

from app.services.decision_engine import DecisionEngine

from app.optimization.optimizer_factory import OptimizerFactory
from app.pipeline.pipeline import OptimizationPipeline
from app.pipeline.pipeline import OptimizationPipeline
class OptimizationService:

    @staticmethod
    def plan(model_path: str):

        inspection = ModelIntelligence.inspect(model_path)

        recommendation = DecisionEngine.recommend(inspection)

        backend = recommendation["recommended_backend"]

        if backend == "ONNX Runtime":

            pipeline = [

                "Export Model to ONNX",

                "Optimize Graph",

                "Dynamic INT8 Quantization",

                "Run Benchmark",

                "Generate Report"

            ]

        elif backend == "llama.cpp":

            pipeline = [

                "Convert to GGUF",

                "Apply Q4/Q5 Quantization",

                "Benchmark llama.cpp",

                "Generate Report"

            ]

        else:

            pipeline = [

                "Native PyTorch Benchmark"

            ]

        return {

            "inspection": inspection,

            "recommendation": recommendation,

            "pipeline": pipeline

        }

    @staticmethod
    def optimize(model_id, model_path):

        return OptimizationPipeline.execute(

            model_id,

            model_path

        )