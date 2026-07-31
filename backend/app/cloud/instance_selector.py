from app.cloud.cloud_catalog import CLOUD_CATALOG


class InstanceSelector:

    @staticmethod
    def select(inspection):

        required_ram = max(
            inspection.get("estimated_ram_gb", 1) * 2,
            2
        )

        candidates = [
            c for c in CLOUD_CATALOG
            if c.ram_gb >= required_ram
        ]

        if not candidates:
            return None

        candidates.sort(key=lambda x: x.hourly_cost)

        return candidates[0]
