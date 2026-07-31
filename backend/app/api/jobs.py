from fastapi import APIRouter, HTTPException
from threading import Thread

from app.jobs.job_manager import JobManager
from app.jobs.worker import Worker

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post("/optimize")
def optimize(model: str):

    job = JobManager.create_job(
        "Optimization",
        model
    )

    Thread(
    target=Worker.run,
    args=(
        job["job_id"],
        model,
    ),
    daemon=True
).start()
    return job


@router.get("/{job_id}")
def status(job_id: str):

    job = JobManager.get(job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job