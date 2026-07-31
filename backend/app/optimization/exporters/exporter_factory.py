from app.optimization.exporters.huggingface_exporter import HuggingFaceExporter


class ExporterFactory:

    @staticmethod
    def get_exporter(inspection):

        exporters = [
            HuggingFaceExporter(),
        ]

        for exporter in exporters:

            if exporter.supports(inspection):

                return exporter

        raise ValueError(
            "No exporter available for this model."
        )