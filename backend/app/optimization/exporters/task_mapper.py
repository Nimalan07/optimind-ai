TASK_MAP = {
    "bert": "fill-mask",
    "distilbert": "fill-mask",
    "roberta": "fill-mask",
    "t5": "text2text-generation",
    "llama": "text-generation",
    "phi": "text-generation",
    "whisper": "automatic-speech-recognition",
}
def get_task(inspection):
    architecture = inspection["architecture"].lower()

    for model, task in TASK_MAP.items():
        if model in architecture:
            return task

    return "feature-extraction"