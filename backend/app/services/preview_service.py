from app.services.model_intelligence import ModelIntelligence
from app.services.decision_engine import DecisionEngine


class PreviewService:

    @staticmethod
    def preview(model_path):

        inspection = ModelIntelligence.inspect(model_path)

        recommendation = DecisionEngine.recommend(inspection)

        params = recommendation["estimated_parameters_billion"]

        original_ram = recommendation["estimated_ram_gb"]

        backend = recommendation["recommended_backend"]

        quantization = recommendation["recommended_quantization"]

        speed = recommendation["expected_speedup"]

        memory = recommendation["memory_reduction"]

        if params is None:
            estimated_size = "Unknown"
        else:
            estimated_size = round(params * 2, 2)

        optimized_size = round(
            estimated_size * 0.55,
            2
        ) if isinstance(estimated_size, float) else "Unknown"

        return {

            "architecture":
                inspection["architecture"],

            "parameters_billion":
                params,

            "original_size_gb":
                estimated_size,

            "optimized_size_gb":
                optimized_size,

            "estimated_ram_gb":
                original_ram,

            "backend":
                backend,

            "quantization":
                quantization,

            "speedup":
                speed,

            "memory_reduction":
                memory

        }