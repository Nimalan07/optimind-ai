class CloudCostEstimator:

    CLOUD_INSTANCES = {

        "AWS": {
            "c8g.large": {
                "processor": "Graviton4",
                "vcpus": 2,
                "ram": 4,
                "hourly_cost": 0.068
            },
            "c8g.xlarge": {
                "processor": "Graviton4",
                "vcpus": 4,
                "ram": 8,
                "hourly_cost": 0.136
            }
        },

        "Azure": {
            "Dps_v6": {
                "processor": "Cobalt 100",
                "vcpus": 2,
                "ram": 8,
                "hourly_cost": 0.081
            }
        },

        "GCP": {
            "c4a-standard-4": {
                "processor": "Axion",
                "vcpus": 4,
                "ram": 16,
                "hourly_cost": 0.121
            }
        }
    }

    @staticmethod
    def estimate(provider, instance):

        # Robust fallbacks to prevent KeyErrors for arbitrary recommendations
        p_info = CloudCostEstimator.CLOUD_INSTANCES.get(provider)
        if not p_info:
            provider = "AWS"
            p_info = CloudCostEstimator.CLOUD_INSTANCES[provider]

        info = p_info.get(instance)
        if not info:
            first_key = list(p_info.keys())[0]
            instance = first_key
            info = p_info[instance]

        hourly = info["hourly_cost"]
        daily = round(hourly * 24, 2)
        monthly = round(hourly * 24 * 30, 2)

        return {

            "provider": provider,

            "instance": instance,

            "processor": info["processor"],

            "vcpus": info["vcpus"],

            "ram_gb": info["ram"],

            "hourly_cost_usd": hourly,

            "daily_cost_usd": daily,

            "monthly_cost_usd": monthly

        }
