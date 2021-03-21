import os.path

from cli.src.command.command import Command


class Cat(Command):
    """Implementation of Cat command"""

    def execute(self, result, pipe_count, *args):
        """Begin command 'cat' execution."""
        print(args)
        if len(args) == 0:
            if pipe_count > 0:
                return result
            raise ValueError("No arguments for 'cat' command")

        path = args[0]
        if os.path.exists(path):
            with open(path, 'r') as file:
                data = file.read()
                return data
        raise ValueError("Invalid path: {}".format(path))
