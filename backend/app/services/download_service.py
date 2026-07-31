import os

from app.download import ModelDownloader


DOWNLOAD_DIR = "downloaded_models"


class DownloadService:

    @staticmethod
    def download_config_only(repo_id: str):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        model_path = os.path.join(
            DOWNLOAD_DIR,
            repo_id.replace("/", "_")
        )
        
        result = ModelDownloader.download_config_only(
            model_id=repo_id,
            output_dir=model_path
        )
        
        return {
            "status": result["status"],
            "path": result["path"],
            "model": repo_id
        }

    @staticmethod
    def download(
        repo_id: str,
        backend: str = "pytorch"
    ):

        os.makedirs(DOWNLOAD_DIR, exist_ok=True)

        model_path = os.path.join(
            DOWNLOAD_DIR,
            repo_id.replace("/", "_")
        )

        result = ModelDownloader.download(
            model_id=repo_id,
            output_dir=model_path,
            backend=backend
        )

        return {
            "status": result["status"],
            "path": result["path"],
            "model": repo_id,
            "backend": backend
        }