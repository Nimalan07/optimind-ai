from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter(
    prefix="/artifacts",
    tags=["Artifacts"]
)


@router.get("/{artifact_name}")
def get_artifact(artifact_name: str):
    # Look in the artifacts/ or reports/ directories
    search_dirs = ["reports", "artifacts", "."]
    for directory in search_dirs:
        file_path = os.path.join(directory, artifact_name)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
            
    raise HTTPException(
        status_code=404,
        detail=f"Artifact '{artifact_name}' not found."
    )
