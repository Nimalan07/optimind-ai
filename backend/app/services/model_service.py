from huggingface_hub import list_models


POPULAR_MODELS = [
    {
        "name": "Llama 3.2 3B",
        "framework": "GGUF",
        "size": "2 GB",
        "source": "Built-in",
    },
    {
        "name": "Gemma 2B",
        "framework": "GGUF",
        "size": "1.8 GB",
        "source": "Built-in",
    },
    {
        "name": "Qwen2.5 3B",
        "framework": "GGUF",
        "size": "2.2 GB",
        "source": "Built-in",
    },
    {
        "name": "Phi-3 Mini",
        "framework": "GGUF",
        "size": "2 GB",
        "source": "Built-in",
    },
]


class ModelService:

    @staticmethod
    def popular_models():
        return POPULAR_MODELS

    @staticmethod
    def search_huggingface(query: str):

        models = list_models(search=query, limit=10)

        results = []

        for model in models:
            results.append(
                {
                    "id": model.id,
                    "downloads": model.downloads,
                }
            )

        return results