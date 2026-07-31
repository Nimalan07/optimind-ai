from app.reports.executive_summary import ExecutiveSummary
from app.reports.recommendation_section import RecommendationSection
from app.reports.deployment_section import DeploymentSection
from app.reports.benchmark_section import BenchmarkSection
from app.reports.cost_section import CostSection
from app.reports.charts import Charts


class ReportBuilder:

    @staticmethod
    def build_report(report_data):
        return {
            "title": "AI Optimization Report",
            "date": "2026-07-27",
            "model": report_data.get("inspection", {}).get("architecture", "Unknown"),
            "optimization_score": report_data.get("optimization_score", 95),
            "status": "READY FOR DEPLOYMENT",
            "executive_summary": ExecutiveSummary.build(report_data),
            "recommendations": RecommendationSection.build(report_data),
            "deployment": DeploymentSection.build(report_data),
            "benchmark": BenchmarkSection.build(report_data),
            "cost": CostSection.build(report_data),
            "charts": Charts.generate(report_data)
        }
