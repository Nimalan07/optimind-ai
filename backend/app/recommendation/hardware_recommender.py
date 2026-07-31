import os


class HardwareRecommender:

    @staticmethod
    def recommend():

        cpu_count = os.cpu_count() or 4

        if cpu_count <= 4:

            return {
                "hardware": "CPU",
                "profile": "Small"
            }

        if cpu_count <= 16:

            return {
                "hardware": "CPU",
                "profile": "Medium"
            }

        return {
            "hardware": "CPU",
            "profile": "Large"
        }
