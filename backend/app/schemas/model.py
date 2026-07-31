from pydantic import BaseModel


class ModelInfo(BaseModel):
    name: str
    framework: str
    size: str
    source: str