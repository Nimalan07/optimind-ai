from dataclasses import dataclass, field
from typing import Any


@dataclass
class PipelineContext:

    model_id: str

    model_path: str | None = None

    inspection: dict = field(default_factory=dict)

    recommendation: dict = field(default_factory=dict)

    optimization: dict = field(default_factory=dict)

    benchmark: dict = field(default_factory=dict)

    deployment: dict = field(default_factory=dict)

    report: dict = field(default_factory=dict)

    artifacts: dict = field(default_factory=dict)

    metadata: dict = field(default_factory=lambda: {
        "progress": {
            "download": "pending",
            "inspection": "pending",
            "recommendation": "pending",
            "optimization": "pending",
            "benchmark": "pending",
            "deployment": "pending",
            "report": "pending"
        }
    })
