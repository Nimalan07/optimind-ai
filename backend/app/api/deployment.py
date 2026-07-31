from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.deployment.deployment_service import DeploymentService

router = APIRouter(
    prefix="/deployment",
    tags=["Deployment"]
)


@router.get("/generate")
def generate():

    return DeploymentService.generate()


@router.get("/download")
def download():

    zip_path = DeploymentService.generate_zip_path()

    return FileResponse(
        path=zip_path,
        filename="deployment_package.zip",
        media_type="application/zip"
    )
