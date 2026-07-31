from pydantic import BaseModel


class PipelineResult(BaseModel):

    status: str

    model_id: str

    inspection: dict

    recommendation: dict

    optimization: dict

    benchmark: dict

    deployment: dict

    report: dict

    artifacts: dict
