import uuid

jobs = {}


class JobManager:

    @staticmethod
    def create_job(task, model):

        job_id = str(uuid.uuid4())

        jobs[job_id] = {

            "job_id": job_id,

            "task": task,

            "model": model,

            "status": "Queued",

            "progress": 0

        }

        return jobs[job_id]

    @staticmethod
    def update(job_id, status, progress):

        jobs[job_id]["status"] = status

        jobs[job_id]["progress"] = progress

    @staticmethod
    def get(job_id):

        return jobs.get(job_id)