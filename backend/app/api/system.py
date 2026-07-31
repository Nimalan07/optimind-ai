from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/")
def home():
    return {
        "message": "OptiMind AI API",
        "version": "1.0.0"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }