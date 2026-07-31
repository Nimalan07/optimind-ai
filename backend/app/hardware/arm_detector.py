import platform


class ARMDetector:

    @staticmethod
    def detect():

        machine = platform.machine().lower()

        is_arm = machine.startswith("arm") or machine.startswith("aarch64")

        return {

            "is_arm": is_arm,

            "architecture": machine

        }
