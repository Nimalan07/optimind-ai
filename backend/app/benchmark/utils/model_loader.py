def load_model(model_path, inspection):
    from transformers import (
        AutoModel,
        AutoModelForCausalLM,
        AutoModelForSeq2SeqLM,
        WhisperModel,
    )

    arch = inspection["architecture"].lower()

    if "bert" in arch or "roberta" in arch or "distilbert" in arch:
        return AutoModel.from_pretrained(model_path)

    elif "llama" in arch or "phi" in arch:
        return AutoModelForCausalLM.from_pretrained(model_path)

    elif "t5" in arch:
        return AutoModelForSeq2SeqLM.from_pretrained(model_path)

    elif "whisper" in arch:
        return WhisperModel.from_pretrained(model_path)

    raise ValueError(f"Unsupported architecture: {arch}")