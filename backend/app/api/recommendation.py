from fastapi import APIRouter

from app.services.download_service import DownloadService
from app.services.recommendation_service import RecommendationService


router = APIRouter(
    prefix="/recommend",
    tags=["Recommendation"]
)


@router.post("/{model_id:path}")
def recommend(model_id: str):

    download_result = DownloadService.download_config_only(
        model_id
    )

    model_path = download_result["path"] if isinstance(download_result, dict) else download_result

    return RecommendationService.recommend(
        model_path
    )
