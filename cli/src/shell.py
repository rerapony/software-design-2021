import sys


class Shell:
    """Class Shell, which implements logic of using
    Parser and CommandFactory for processing bash command"""

    def __init__(self, factory, parser, input_flow=sys.stdin, output_flow=sys.stdout):
        self.factory = factory
        self.parser = parser
        self.input_flow = input_flow
        self.output_flow = output_flow

    def run_shell(self):
        """
        Runs one iteration of parsing and implementing bash commands.
        :return: str, command execution result
        """
        result = None
        count = 0

        line = self.input_flow.readline()
        while line:
            tokens_list = self.parser.parse(line)
            if tokens_list is not None:  # assignment
                for tokens in tokens_list:
                    if not tokens:
                        raise Exception("Empty command")

                    command_name = tokens[0]
                    command_name += "_cmd"
                    args = tokens[1:]

                    try:
                        command = getattr(self.factory, command_name)()
                    except Exception as exc:
                        raise Exception("Bad command: {}".format(command_name)) from exc

                    result = command.execute(result, count, *args)
                    count += 1

                self.output_flow.write(result + '\n')
                self.output_flow.flush()
            line = self.input_flow.readline()
