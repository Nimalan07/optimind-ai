class OptimizationPlanner:

    @staticmethod
    def plan(inspection: dict):

        architecture = inspection.get("architecture", "").lower()

        steps = [
            "Validation",
            "Inspection"
        ]

        if any(x in architecture for x in [
            "bert",
            "roberta",
            "distilbert",
            "phi",
            "llama",
            "t5"
        ]):

            steps.extend([
                "Export to ONNX",
                "Dynamic Quantization",
                "Benchmark",
                "Generate Report"
            ])

        else:

            steps.extend([
                "Benchmark",
                "Generate Report"
            ])

        return steps
