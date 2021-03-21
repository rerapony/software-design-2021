from src.command.command import Command
import os


class Pwd(Command):
    """Implementation of 'pwd' command"""
    def execute(*args):
        """Begin command 'pwd' execution."""
        return os.getcwd()

    def __str__(self):
        return "pwd"
