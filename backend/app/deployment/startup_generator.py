class StartupGenerator:

    @staticmethod
    def generate():

        return """
#!/bin/bash

uvicorn main:app --host 0.0.0.0 --port 8000
""".strip()
