from app.pipeline.pipeline_service import PipelineService
from app.agent.job_manager import JobManager


class OptimizationAgent:

    @staticmethod
    def optimize(request):

        job_id = JobManager.create()

        result = PipelineService.run(
            request.model_id
        )

        return {
            "status": "completed",
            "job_id": job_id,
            "optimized_model": result.artifacts.get("optimized_model", ""),
            "benchmark": "reports/benchmark.json",
            "report": result.artifacts.get("report_pdf", ""),
            "deployment": result.artifacts.get("deployment_package", "")
        }
