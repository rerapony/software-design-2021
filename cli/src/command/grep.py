import re
import glob

from cli.src.command.command import Command


class Grep(Command):
    """Implementation of 'grep' command"""

    def execute(self, result, count, *args):
        """Begin command 'grep' execution."""

        if len(args) == 1 & count > 1:
            pattern = args[0]
            for line in result.split('\n'):
                if re.search(line, pattern):
                    return line
        elif len(args) > 1:
            pattern, files = args
            for arg in args:
                for file in glob.iglob(arg):
                    for line in open(file, 'r'):
                        if re.search(pattern, line):
                            return line
        else:
            raise ValueError("No arguments for 'grep' command")
