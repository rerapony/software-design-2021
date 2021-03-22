import os.path

from cli.src.command.command import Command


class Wc(Command):
    """Implementation of 'wc' command"""
    def execute(self, result, count, *args):
        """Begin command 'wc' execution."""

        if not args:
            if count > 0:

                return "{} {} {}".format(len(result.split('\n')), len(result.split()), len(result))
            raise ValueError("No arguments for 'wc' command")

        path = args[0]
        if os.path.exists(path):
            chars = 0
            words = 0
            lines = 0
            with open(path, 'r') as file_to_count:
                for line in file_to_count:
                    lines += 1
                    words += len(line.split())
                    chars += len(line)

            return "{} {} {}".format(lines, words, chars)

        raise ValueError("Invalid path: {}".format(path))
