from app.services.download_service import DownloadService


class DownloadStage:

    def run(self, context):
        context.metadata["progress"]["download"] = "running"
        
        try:
            download_result = DownloadService.download(context.model_id)
            context.model_path = download_result["path"] if isinstance(download_result, dict) else download_result
        except Exception:
            # Fallback to local resolver if download fails
            from app.utils.model_path import get_model_path
            context.model_path = get_model_path(context.model_id) or context.model_id
            
        context.metadata["progress"]["download"] = "completed"
