from app.cloud.cloud_catalog import CLOUD_CATALOG


class ProviderRanker:

    @staticmethod
    def rank(instance):

        score = 0

        if "Graviton" in instance.processor:
            score += 40

        if instance.hourly_cost < 0.08:
            score += 30

        if instance.vcpus >= 4:
            score += 15

        if instance.ram_gb >= 8:
            score += 15

        return min(score, 100)
