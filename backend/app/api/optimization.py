from fastapi import APIRouter
from fastapi import HTTPException

from app.utils.model_path import get_model_path

from app.services.optimization_service import OptimizationService
from app.services.preview_service import PreviewService
router = APIRouter(

    prefix="/optimization",

    tags=["Optimization"]

)


@router.get("/plan/{model_id:path}")

def plan(model_id: str):

    path = get_model_path(model_id)

    if path is None:

        raise HTTPException(404, "Model not found")

    return OptimizationService.plan(path)


@router.post("/run/{model_id:path}")

def run(model_id: str):

    path = get_model_path(model_id)

    if path is None:

        raise HTTPException(404, "Model not found")

    return OptimizationService.optimize(

        model_id,

        path

    )

@router.get("/preview/{model_id:path}")
def preview(model_id: str):

    path = get_model_path(model_id)

    if path is None:
        raise HTTPException(
            404,
            "Model not found"
        )

    return PreviewService.preview(path)