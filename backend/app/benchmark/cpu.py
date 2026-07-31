import psutil


class CPUBenchmark:

    @staticmethod
    def usage():

        return psutil.cpu_percent(interval=1)