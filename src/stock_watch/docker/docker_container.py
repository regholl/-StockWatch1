from .command_line_interface import CommandLineInterface
from .models.command_sequence import CommandSequence

class DockerContainer(object):
    def __init__(self, command_sequence: CommandSequence):
        self._cli = CommandLineInterface()
        self.command_sequence = command_sequence

    def start(self):
        # What is this containers process? Do we need to stop it, start it, destroy it, etc, each time we run the app?
        # Execute each command in the command sequence
        for command in self.command_sequence.commands:
            self._cli.run_command(command)