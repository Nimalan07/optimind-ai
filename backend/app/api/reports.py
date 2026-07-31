import os
from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/latest")
def latest_report():
    pdf_path = os.path.join("reports", "optimization_report.pdf")
    if os.path.exists(pdf_path):
        return FileResponse(
            path=pdf_path,
            filename="optimization_report.pdf",
            media_type="application/pdf"
        )
    return {"message": "No reports generated yet."}


@router.post("/{model_id:path}")
def generate_report(model_id: str):
    from app.services.recommendation_service import RecommendationService
    from app.reports.report_service import ReportService
    from app.benchmark.benchmark_runner import BenchmarkRunner

    try:
        from app.services.download_service import DownloadService
        download_result = DownloadService.download(model_id)
        model_path = download_result["path"] if isinstance(download_result, dict) else download_result
    except Exception:
        from app.utils.model_path import get_model_path
        model_path = get_model_path(model_id) or model_id

    rec = RecommendationService.recommend(model_path)
    before, after = BenchmarkRunner.generate_dynamic_results(model_id, rec.get("inspection", {}))
    from app.benchmark.comparison import BenchmarkComparison
    improvements = BenchmarkComparison.compare(before, after)

    report_data = {
        "inspection": rec.get("inspection", {}),
        "backend": rec.get("backend", {}),
        "cloud": rec.get("cloud", {}),
        "optimization_score": rec.get("optimization_score", 95),
        "benchmark": {
            "before": before,
            "after": after,
            "improvements": improvements
        }
    }

    return ReportService.generate_report(report_data)