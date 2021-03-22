import pathlib
from os import chdir
from cli.src.command.command import Command


class Cd(Command):
    """Implementation of 'cd' command"""

    def execute(self, result, count, *args):
        """Begin command 'cd' execution.

        Arguments:
        result -- ignored
        count -- ignored
        args -- should have 0 or 1 element.
        If empty, then directory is changed to home directory.
        Else tries to change directory to 'arg[0]'

        Returns nothing
        """
        if len(args) > 1:
            raise ValueError("too many arguments for cd command")
        if len(args) == 1:
            path = pathlib.Path(args[0]).expanduser()
        else:
            path = pathlib.Path.home()
        try:
            chdir(path)
        except FileNotFoundError as exc:
            raise ValueError(f"The directory '{path}' does not exist,"
                             f"{pathlib.Path.cwd()}") from exc
        except NotADirectoryError as exc:
            raise ValueError(f"'{path}' is not a directory") from exc
        except PermissionError as exc:
            raise ValueError(f"Permission denied: '{path}'") from exc
        return ''
