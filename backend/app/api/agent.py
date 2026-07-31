from fastapi import APIRouter
from pydantic import BaseModel

from app.agent.optimization_agent import OptimizationAgent


class OptimizationRequest(BaseModel):

    model_id: str

    target_cloud: str = "AWS"

    budget: float | None = None

    latency_target_ms: float | None = None


router = APIRouter(
    prefix="/agent",
    tags=["AI Agent"]
)


@router.post("/optimize")
def optimize(request: OptimizationRequest):

    return OptimizationAgent.optimize(request)
