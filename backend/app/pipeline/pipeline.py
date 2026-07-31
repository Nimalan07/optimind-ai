from app.pipeline.stages.download_stage import DownloadStage
from app.pipeline.stages.inspection_stage import InspectionStage
from app.pipeline.stages.recommendation_stage import RecommendationStage
from app.pipeline.stages.optimization_stage import OptimizationStage
from app.pipeline.stages.benchmark_stage import BenchmarkStage
from app.pipeline.stages.deployment_stage import DeploymentStage
from app.pipeline.stages.report_stage import ReportStage


class OptimizationPipeline:

    def __init__(self):

        self.stages = [

            DownloadStage(),

            InspectionStage(),

            RecommendationStage(),

            OptimizationStage(),

            BenchmarkStage(),

            DeploymentStage(),

            ReportStage()

        ]

    def run(self, context):

        for stage in self.stages:

            stage.run(context)

        return context

    @staticmethod
    def execute(model_id: str, model_path: str):
        from app.pipeline.pipeline_context import PipelineContext
        context = PipelineContext(model_id=model_id, model_path=model_path)
        
        # Override download step progress since model_path is already provided
        context.metadata["progress"]["download"] = "completed"
        
        pipeline = OptimizationPipeline()
        # Skip the DownloadStage since we already have the model_path
        stages_to_run = pipeline.stages[1:]
        
        for stage in stages_to_run:
            stage.run(context)
            
        return {
            "model": model_id,
            "validation": {"valid": True, "missing": []},
            "optimization": [context.optimization],
            "benchmark": context.benchmark,
            "registry": {"status": "updated"},
            "report": {"status": "generated"}
        }