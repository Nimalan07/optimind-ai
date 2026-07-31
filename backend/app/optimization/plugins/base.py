from abc import ABC
from abc import abstractmethod


class OptimizationPlugin(ABC):

    @abstractmethod
    def supports(self, inspection):
        pass

    @abstractmethod
    def optimize(self, model_path):
        pass