from cli.src.command.command import Command


class Echo(Command):
    """Implementation of Echo command"""

    def execute(self, result, count, *args):
        """Begin command 'echo' execution."""
        ans = ""
        for arg in args:
            if ans != "":
                ans = " ".join([ans, arg])
            else:
                ans = "".join([ans, arg])
        return ans
