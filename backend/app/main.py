from fastapi import FastAPI
from app.api import registry
from app.api import jobs


from app.api import (
    system,
    models,
    optimization,
    benchmark,
    reports
)
from app.api.recommendation import router as recommendation_router
from app.api.hardware import router as hardware_router
from app.api.cloud import router as cloud_router
from app.api.deployment import router as deployment_router
from app.api.pipeline import router as pipeline_router
from app.api.agent import router as agent_router
from app.api.artifacts import router as artifacts_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(

    title="OptiMind AI",

    version="1.0.0"

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(system.router)

app.include_router(models.router)

app.include_router(optimization.router)

app.include_router(benchmark.router)

app.include_router(reports.router)

app.include_router(jobs.router)

app.include_router(recommendation_router)

app.include_router(hardware_router)

app.include_router(cloud_router)

app.include_router(deployment_router)

app.include_router(pipeline_router)

app.include_router(agent_router)

app.include_router(artifacts_router)
