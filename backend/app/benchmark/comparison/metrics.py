from dataclasses import dataclass, asdict


@dataclass
class BenchmarkMetrics:

    latency: float
    memory: float
    cpu: float
    size: float
    throughput: float

    def to_dict(self):
        return asdict(self)