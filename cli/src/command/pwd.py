import os

from cli.src.command.command import Command


class Pwd(Command):
    """Implementation of 'pwd' command"""
    def execute(self, result, count, *args):
        """Begin command 'pwd' execution."""
        return os.getcwd()
