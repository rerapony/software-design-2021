import pathlib
from os import chdir
from cli.src.command.command import Command


class Cd(Command):
    """Implementation of 'cd' command"""

    def execute(self, result, count, *args):
        """Begin command 'wc' execution.

        Arguments:
        result -- ignored
        count -- ignored
        args -- should have 0 or 1 element.
        If empty, then directory is changed to home directory.
        Else tries to change directory to 'arg[0]'
        """
        if len(args) > 1:
            raise ValueError("too many arguments for cd command")
        if len(args) == 1:
            path = pathlib.Path(args[0]).expanduser()
        else:
            path = pathlib.Path.home()
        try:
            chdir(path)
        except FileNotFoundError as e:
            raise ValueError(f"The directory '{path}' does not exist, {pathlib.Path.cwd()}") from e
        except NotADirectoryError as e:
            raise ValueError(f"'{path}' is not a directory") from e
        except PermissionError as e:
            raise ValueError(f"Permission denied: '{path}'") from e
        return ''
