class DeploymentEstimator:

    @staticmethod
    def estimate(instance):

        hourly = instance.hourly_cost

        return {

            "provider": instance.provider,

            "instance": instance.instance,

            "processor": instance.processor,

            "vcpus": instance.vcpus,

            "ram_gb": instance.ram_gb,

            "hourly_cost_usd": hourly,

            "daily_cost_usd": round(hourly * 24, 2),

            "monthly_cost_usd": round(hourly * 24 * 30, 2)

        }
