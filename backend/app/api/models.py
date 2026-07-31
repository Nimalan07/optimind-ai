from fastapi import APIRouter

from app.services.model_service import ModelService
from app.services.download_service import DownloadService
from app.services.analyzer_service import AnalyzerService
from app.services.model_intelligence import ModelIntelligence
from app.services.decision_engine import DecisionEngine
from fastapi import HTTPException
from app.utils.model_path import get_model_path
router = APIRouter(
    prefix="/models",
    tags=["Models"],
)


@router.get("/popular")
def popular_models():
    return ModelService.popular_models()


@router.get("/search")
def search_models(query: str):
    return ModelService.search_huggingface(query)



@router.post("/download")
def download_model(
    repo_id: str,
    backend: str = "pytorch"
):

    return DownloadService.download(
        repo_id,
        backend
    )

@router.get("/analyze/{model_id:path}")
def analyze_model(model_id: str):

    path = get_model_path(model_id)

    if path is None:
        raise HTTPException(
            status_code=404,
            detail="Model not found"
        )

    return AnalyzerService.analyze(path)
@router.get("/inspect/{model_id:path}")
def inspect_model(model_id: str):

    path = get_model_path(model_id)

    if path is None:
        raise HTTPException(
            status_code=404,
            detail="Model not found"
        )

    return ModelIntelligence.inspect(path)

@router.get("/recommend/{model_id:path}")
def recommend_model(model_id: str):

    path = get_model_path(model_id)

    if path is None:
        raise HTTPException(
            status_code=404,
            detail="Model not found"
        )

    info = ModelIntelligence.inspect(path)

    return DecisionEngine.recommend(info)
@router.get("/details/{model_id:path}")
def model_details(model_id: str):

    path = get_model_path(model_id)

    if path is None:
        raise HTTPException(
            status_code=404,
            detail="Model not found"
        )

    analysis = AnalyzerService.analyze(path)

    inspection = ModelIntelligence.inspect(path)

    recommendation = DecisionEngine.recommend(inspection)

    return {
        "analysis": analysis,
        "inspection": inspection,
        "recommendation": recommendation,
    }