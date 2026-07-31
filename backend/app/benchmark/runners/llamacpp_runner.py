from app.benchmark.runners.pytorch_runner import PyTorchRunner


class LlamaCppRunner:

    @staticmethod
    def run(model_path):

        return PyTorchRunner.run(model_path)