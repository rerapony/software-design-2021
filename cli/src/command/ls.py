import pathlib
from cli.src.command.command import Command


class Ls(Command):
    """Implementation of 'ls' command"""

    def execute(self, result, count, *args):
        """Begin command 'ls' execution.

        Arguments:
        result -- ignored
        count -- ignored
        args -- should have 0 or 1 element.
        If empty, then lists contents of current directory
        Else tries to lists contents of 'arg[0]'
        Hidden files (files starting with '.') are not shown

        Returns sorted contents of directory separated by whitespace"""
        if len(args) > 1:
            raise ValueError("too many arguments for ls command")
        if len(args) == 1:
            path = pathlib.Path(args[0]).expanduser()
        else:
            path = pathlib.Path.cwd()

        if not path.exists():
            raise ValueError(f'{path} does not exist')
        if not path.is_dir():
            raise ValueError(f'{path} is not a directory')

        result = []
        for child in path.iterdir():
            if child.stem.startswith('.'):  # hidden file
                continue
            result.append(child.name)

        return ' '.join(sorted(result))
