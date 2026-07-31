from pathlib import Path

DOWNLOAD_DIR = Path("downloaded_models")


def get_model_path(model_id: str):

    folder = model_id.replace("/", "_")

    model_path = DOWNLOAD_DIR / folder

    if not model_path.exists():
        return None

    return str(model_path)