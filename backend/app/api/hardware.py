from fastapi import APIRouter

from app.hardware.hardware_service import HardwareService

router = APIRouter(
    prefix="/hardware",
    tags=["Hardware"]
)


@router.get("/profile")
def profile():

    return HardwareService.get_profile()
