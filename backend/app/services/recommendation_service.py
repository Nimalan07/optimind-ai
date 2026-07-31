from app.services.model_intelligence import ModelIntelligence

from app.recommendation.backend_recommender import BackendRecommender
from app.recommendation.hardware_recommender import HardwareRecommender
from app.recommendation.cloud_recommender import CloudRecommender
from app.recommendation.optimization_planner import OptimizationPlanner

from app.analytics.cloud_cost_estimator import CloudCostEstimator
from app.analytics.optimization_score import OptimizationScore


class RecommendationService:

    @staticmethod
    def recommend(model_path: str):

        inspection = ModelIntelligence.inspect(model_path)

        backend = BackendRecommender.recommend(
            inspection
        )

        hardware = HardwareRecommender.recommend()

        cloud = CloudRecommender.recommend(
            backend["backend"]
        )

        cost = CloudCostEstimator.estimate(
            cloud["provider"],
            cloud["instance"]
        )

        score = OptimizationScore.calculate(
            inspection,
            backend["backend"]
        )

        plan = OptimizationPlanner.plan(
            inspection
        )

        return {

            "inspection": inspection,

            "backend": backend,

            "hardware": hardware,

            "cloud": cloud,

            "cloud_cost": cost,

            "optimization_score": score,

            "optimization_plan": plan

        }
