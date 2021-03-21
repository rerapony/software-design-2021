from src.command.command import Command
import sys


class Exit(Command):
    """Implementation of 'exit' command"""
    def execute(*args):
        """Exit CLI emulator"""
        sys.exit()

    def __str__(self):
        return "exit"
