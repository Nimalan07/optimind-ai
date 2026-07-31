class NginxGenerator:

    @staticmethod
    def generate():

        return """
events {}

http {

    server {

        listen 80;

        location / {

            proxy_pass http://optimizer:8000;

        }

    }

}
""".strip()
