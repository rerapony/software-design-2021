import sys

from cli.src.command.command import Command


class Exit(Command):
    """Implementation of 'exit' command"""
    def execute(self, result, count, *args):
        """Exit CLI emulator"""
        if args:
            raise ValueError("Incorrect arguments for 'exit' command")
        sys.exit()
