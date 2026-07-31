import os
import zipfile
import tempfile

from app.deployment.docker_generator import DockerGenerator
from app.deployment.compose_generator import ComposeGenerator
from app.deployment.kubernetes_generator import KubernetesGenerator
from app.deployment.nginx_generator import NginxGenerator
from app.deployment.startup_generator import StartupGenerator
from app.deployment.templates import Templates


class DeploymentService:

    @staticmethod
    def generate():

        return {

            "Dockerfile":
                DockerGenerator.generate(),

            "docker-compose.yml":
                ComposeGenerator.generate(),

            "deployment.yaml":
                KubernetesGenerator.deployment(),

            "service.yaml":
                KubernetesGenerator.service(),

            "nginx.conf":
                NginxGenerator.generate(),

            "start.sh":
                StartupGenerator.generate(),

            "README.md":
                Templates.readme()

        }

    @staticmethod
    def generate_zip_path():

        files = DeploymentService.generate()

        temp_dir = tempfile.gettempdir()
        zip_path = os.path.join(temp_dir, "deployment_package.zip")

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for name, content in files.items():
                zip_file.writestr(name, content)

        return zip_path
