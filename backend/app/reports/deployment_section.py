class DeploymentSection:

    @staticmethod
    def build(report):
        return {
            "docker": "Ready",
            "kubernetes": "Ready",
            "fastapi": "Ready",
            "onnx_runtime": "Ready"
        }
