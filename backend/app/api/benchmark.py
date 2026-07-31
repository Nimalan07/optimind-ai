from fastapi import APIRouter, HTTPException

from app.benchmark.benchmark_runner import BenchmarkRunner
from app.utils.model_path import get_model_path

router = APIRouter(
    prefix="/benchmark",
    tags=["Benchmark"]
)


@router.get("/{model_id:path}")
def benchmark(model_id: str):

    model_path = get_model_path(model_id)

    if model_path is None:
        raise HTTPException(
            status_code=404,
            detail="Model not found"
        )

    return BenchmarkRunner.benchmark(model_path)