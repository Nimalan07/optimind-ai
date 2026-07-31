class OptimizationScore:

    @staticmethod
    def calculate(inspection, backend):

        score = 50

        architecture = inspection["architecture"].lower()

        if "bert" in architecture:
            score += 20

        if "llama" in architecture:
            score += 15

        if backend == "ONNX Runtime":
            score += 20

        if backend == "llama.cpp":
            score += 25

        parameters = inspection.get(
            "estimated_parameters_billion",
            0
        )

        if parameters < 1:
            score += 10

        return min(score, 100)
