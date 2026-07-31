from app.hardware.runtime_profiler import RuntimeProfiler


class HardwareService:

    @staticmethod
    def get_profile():

        profile = RuntimeProfiler.profile()

        ram = profile["memory"]["total_gb"]

        cores = profile["cpu"]["logical_cores"]

        recommendation = "Small"

        if ram >= 16 and cores >= 8:
            recommendation = "Medium"

        if ram >= 32 and cores >= 16:
            recommendation = "Large"

        profile["deployment_profile"] = recommendation

        return profile
