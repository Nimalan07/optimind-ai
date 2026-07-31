from app.services.recommendation_service import RecommendationService


class RecommendationStage:

    def run(self, context):
        context.metadata["progress"]["recommendation"] = "running"
        context.recommendation = RecommendationService.recommend(
            context.model_path
        )
        context.metadata["progress"]["recommendation"] = "completed"
