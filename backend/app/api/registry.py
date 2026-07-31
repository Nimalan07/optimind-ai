from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.registry_service import RegistryService

router = APIRouter(

    prefix="/registry",

    tags=["Registry"]

)


@router.get("/")
def models(

    db: Session = Depends(get_db)

):

    return RegistryService.get_models(db)


@router.get("/{model_id}")
def model(

    model_id: int,

    db: Session = Depends(get_db)

):

    return RegistryService.get_model(db, model_id)