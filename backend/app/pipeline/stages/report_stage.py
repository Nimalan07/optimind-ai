from app.reports.report_service import ReportService
from app.deployment.deployment_service import DeploymentService


class ReportStage:

    def run(self, context):
        context.metadata["progress"]["report"] = "running"
        
        # Prepare data for report generator
        report_data = {
            "inspection": context.inspection,
            "backend": context.recommendation.get("backend", {}),
            "cloud": context.recommendation.get("cloud", {}),
            "optimization_score": context.recommendation.get("optimization_score", 95),
            "benchmark": context.benchmark
        }
        
        report_res = ReportService.generate_report(report_data)
        context.report = report_res["report_content"]
        
        # Save artifacts
        context.artifacts = {
            "optimized_model": context.optimization.get("optimized_path", "") if isinstance(context.optimization, dict) else "",
            "report_pdf": report_res["pdf_path"],
            "report_html": report_res["html_path"],
            "deployment_package": DeploymentService.generate_zip_path()
        }
        
        context.metadata["progress"]["report"] = "completed"
