from sqlalchemy.orm import Session

from app.database.models import ModelRegistry


class RegistryService:

    @staticmethod
    def add_model(

        db: Session,

        model_name,

        repo_id,

        local_path,

        architecture,

        framework,

        fmt,

        size

    ):

        model = ModelRegistry(

            model_name=model_name,

            repo_id=repo_id,

            local_path=local_path,

            architecture=architecture,

            framework=framework,

            format=fmt,

            model_size=size,

            status="Downloaded"

        )

        db.add(model)

        db.commit()

        db.refresh(model)

        return model

    @staticmethod
    def get_models(db: Session):

        return db.query(ModelRegistry).all()

    @staticmethod
    def get_model(db: Session, model_id: int):

        return db.query(ModelRegistry).filter(

            ModelRegistry.id == model_id

        ).first()