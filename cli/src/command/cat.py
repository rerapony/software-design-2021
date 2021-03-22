import os.path

from cli.src.command.command import Command


class Cat(Command):
    """Implementation of Cat command"""

    def execute(self, result, count, *args):
        """Begin command 'cat' execution."""
        if not args:
            if count > 0:
                return result
            raise ValueError("No arguments for 'cat' command")

        path = args[0]
        if os.path.exists(path):
            with open(path, 'r') as file_to_cat:
                data = file_to_cat.read()
                return data
        raise ValueError("Invalid path: {}".format(path))
