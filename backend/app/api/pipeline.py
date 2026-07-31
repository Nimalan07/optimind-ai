from fastapi import APIRouter

from app.pipeline.pipeline_service import PipelineService

router = APIRouter(
    prefix="/pipeline",
    tags=["Pipeline"]
)


@router.post("/run/{model_id:path}")
def run_pipeline(model_id: str):

    return PipelineService.run(model_id)
