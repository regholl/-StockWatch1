from .docker_container import DockerContainer

class ContainerManager(object):
    def __init__(self, containers: list = None):
        self.containers = containers if containers else []

    def add_container(self, container: DockerContainer):
        self.containers.append(container)

    def add_containers(self, containers: list):
        for container in containers:
            self.add_container(container)

    def start_containers(self):
        for container in self.containers:
            container.start()
