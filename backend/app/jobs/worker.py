from app.pipeline.pipeline import OptimizationPipeline


class Worker:

    @staticmethod
    def run(job_id, model):

        OptimizationPipeline.run(
            job_id,
            model
        )