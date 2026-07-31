import platform


class OSDetector:

    @staticmethod
    def profile():

        return {

            "system": platform.system(),

            "release": platform.release(),

            "version": platform.version(),

            "python": platform.python_version()

        }
