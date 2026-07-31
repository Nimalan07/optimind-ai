from app.cloud.instance_selector import InstanceSelector
from app.cloud.provider_ranker import ProviderRanker
from app.cloud.deployment_estimator import DeploymentEstimator


class CloudService:

    @staticmethod
    def recommend(inspection):

        instance = InstanceSelector.select(inspection)

        if instance is None:
            return {
                "error": "No suitable cloud instance found."
            }

        deployment = DeploymentEstimator.estimate(instance)

        deployment["provider_score"] = ProviderRanker.rank(instance)

        return deployment
