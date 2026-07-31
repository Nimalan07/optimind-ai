from pathlib import Path


class ArtifactManager:

    ROOT = Path("artifacts")

    @classmethod
    def register(cls, name, path):

        cls.ROOT.mkdir(exist_ok=True)

        return {

            "name": name,

            "path": str(path)

        }
