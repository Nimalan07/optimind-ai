from abc import ABC, abstractmethod


class BasePlugin(ABC):

    name = ""
    stage = ""

    @staticmethod
    def supports(inspection) -> bool:
        return True

    @staticmethod
    @abstractmethod
    def optimize(model_path: str):
        pass