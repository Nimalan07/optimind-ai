from app.download.profiles import DOWNLOAD_PROFILES


class DownloadStrategy:

    @staticmethod
    def get_profile(backend):

        backend = backend.lower()

        if backend in DOWNLOAD_PROFILES:

            return DOWNLOAD_PROFILES[backend]

        return DOWNLOAD_PROFILES["pytorch"]