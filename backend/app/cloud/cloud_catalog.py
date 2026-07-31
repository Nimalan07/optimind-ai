from dataclasses import dataclass


@dataclass
class CloudInstance:
    provider: str
    instance: str
    processor: str
    vcpus: int
    ram_gb: int
    hourly_cost: float


CLOUD_CATALOG = [

    CloudInstance(
        "AWS",
        "c8g.large",
        "Graviton4",
        2,
        4,
        0.068
    ),

    CloudInstance(
        "AWS",
        "c8g.xlarge",
        "Graviton4",
        4,
        8,
        0.136
    ),

    CloudInstance(
        "Azure",
        "Dps_v6",
        "Cobalt",
        2,
        8,
        0.081
    ),

    CloudInstance(
        "Google",
        "c4a-standard-4",
        "Axion",
        4,
        16,
        0.121
    )

]
