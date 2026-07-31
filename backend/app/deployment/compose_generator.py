class ComposeGenerator:

    @staticmethod
    def generate():

        compose = """
version: '3.9'

services:

  optimizer:

    build: .

    ports:
      - "8000:8000"

    restart: unless-stopped
"""

        return compose.strip()
