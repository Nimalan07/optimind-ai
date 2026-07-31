from app.services.model_intelligence import ModelIntelligence


class InspectionStage:

    def run(self, context):
        context.metadata["progress"]["inspection"] = "running"
        context.inspection = ModelIntelligence.inspect(context.model_path)
        context.metadata["progress"]["inspection"] = "completed"
