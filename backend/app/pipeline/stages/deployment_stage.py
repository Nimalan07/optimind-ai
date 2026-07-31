from app.deployment.deployment_service import DeploymentService


class DeploymentStage:

    def run(self, context):
        context.metadata["progress"]["deployment"] = "running"
        context.deployment = DeploymentService.generate()
        context.metadata["progress"]["deployment"] = "completed"
