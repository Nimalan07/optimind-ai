from pathlib import Path


class ValidationStage:

    @staticmethod
    def run(model_path):

        path = Path(model_path)

        required = [

            "config.json"

        ]

        missing = []

        for file in required:

            if not (path / file).exists():

                missing.append(file)

        return {

            "valid": len(missing) == 0,

            "missing": missing

        }