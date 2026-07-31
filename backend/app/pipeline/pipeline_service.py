from app.pipeline.pipeline import OptimizationPipeline
from app.pipeline.pipeline_context import PipelineContext
from app.pipeline.pipeline_result import PipelineResult


class PipelineService:

    @staticmethod
    def run(model_id: str):

        context = PipelineContext(
            model_id=model_id
        )

        pipeline = OptimizationPipeline()

        context = pipeline.run(context)

        return PipelineResult(

            status="completed",

            model_id=model_id,

            inspection=context.inspection,

            recommendation=context.recommendation,

            optimization=context.optimization,

            benchmark=context.benchmark,

            deployment=context.deployment,

            report=context.report,

            artifacts=context.artifacts

        )
