from fastapi import APIRouter

from app.services.download_service import DownloadService
from app.services.model_intelligence import ModelIntelligence
from app.cloud.cloud_service import CloudService

router = APIRouter(
    prefix="/cloud",
    tags=["Cloud"]
)


@router.post("/{model_id:path}")
def recommend_cloud(model_id: str):

    try:
        download_result = DownloadService.download(model_id)
        model_path = download_result["path"] if isinstance(download_result, dict) else download_result
    except Exception:
        from app.utils.model_path import get_model_path
        model_path = get_model_path(model_id) or model_id

    inspection = ModelIntelligence.inspect(model_path)

    return CloudService.recommend(inspection)


@router.post("/recommend")
def recommend_cloud_post(model_id: str):
    return recommend_cloud(model_id)
