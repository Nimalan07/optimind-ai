import json


class BenchmarkReport:

    @staticmethod
    def generate(comparison):

        return {

            "status": "generated",

            "summary": comparison,

            "json": json.dumps(
                comparison,
                indent=4
            )

        }