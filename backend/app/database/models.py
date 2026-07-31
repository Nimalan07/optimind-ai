from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from app.database.database import Base


class ModelRegistry(Base):

    __tablename__ = "models"

    id = Column(Integer, primary_key=True)

    model_name = Column(String)

    repo_id = Column(String)

    local_path = Column(String)

    architecture = Column(String)

    framework = Column(String)

    format = Column(String)

    model_size = Column(Float)

    status = Column(String)

    downloaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )