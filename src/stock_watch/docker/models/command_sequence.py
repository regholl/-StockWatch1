from .docker_compose_command import DockerComposeCommand
from .docker_command import DockerCommand

from typing import TypeVar
T = TypeVar('T',
            DockerComposeCommand,
            DockerCommand)

class CommandSequence(object):
    def __init__(self, commands: list[T] = None):
        self.commands = commands if commands else []

    def add_command(self, command: T):
        self.commands.append(command)

    def add_commands(self, commands: list[T]):
        for command in commands:
            self.add_command(command)