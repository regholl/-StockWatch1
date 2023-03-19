from typing import Optional, Dict, Any
from .docker_command_option import DockerCommandOption

class DockerCommand:

    def __init__(self,
                 command: DockerCommandOption,
                 parent_options: Optional[Dict[str, Any]] = None,
                 child_options: Optional[Dict[str, Any]] = None,
                 *args
                 ):
        self.command = command
        self.parent_options = parent_options
        self.child_options = child_options
        self.args = args

    def __name__(self):
        return self.__class__.__name__

    # noinspection PyMethodMayBeStatic
    def cli_format(self):
        # TODO: Implement this method
        return f'docker {self._format_parent_options()} {self.command.value} {self._format_child_options()} ' \
               f'{self._format_args()} '

    def _format_parent_options(self):
        option_string = ''
        if self.parent_options:
            for option in self.parent_options:
                if self.parent_options[option]:
                    option_string += f'{option} {self.parent_options[option]} '
                else:
                    option_string += f'{option} '
            option_string = option_string[:-1]
        return option_string

    def _format_child_options(self):
        option_string = ''
        if self.child_options:
            for option in self.child_options:
                if self.child_options[option]:
                    option_string += f'{option} {self.child_options[option]} '
                else:
                    option_string += f'{option} '
            option_string = option_string[:-1]
        return option_string

    def _format_args(self):
        args_string = ''
        if self.args:
            for arg in self.args:
                args_string += f'{arg} '
            args_string = args_string[:-1]
        return args_string
