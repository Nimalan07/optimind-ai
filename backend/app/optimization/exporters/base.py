from abc import ABC, abstractmethod


class BaseExporter(ABC):

    @abstractmethod
    def supports(self, inspection: dict) -> bool:
        """Return True if this exporter supports the inspected model."""
        pass

    @abstractmethod
    def export(self, model_path: str, output_dir: str) -> dict:
        """Export the model to the target format."""
        pass