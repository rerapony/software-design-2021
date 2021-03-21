import sys

from cli.src.factory.abstract_factory import AbstractFactory
from cli.src.parser import Parser


class Shell:

    def __init__(self, factory: AbstractFactory, parser: Parser, input_flow=sys.stdin, output_flow=sys.stdout):
        self.factory = factory
        self.parser = parser
        self.input_flow = input_flow
        self.output_flow = output_flow

    def run_shell(self):
        result = None
        count = 0

        line = self.input_flow.readline()
        while line:
            tokens_list = self.parser.parse(line)
            if tokens_list is not None:  # assignment
                for tokens in tokens_list:
                    if len(tokens) == 0:
                        raise Exception("Empty command")

                    command_name = tokens[0]
                    args = tokens[1:]

                    try:
                        command = getattr(self.factory, command_name)()
                    except Exception:
                        raise Exception("Bad command: {}".format(command_name))

                    result = command.execute(result, count, *args)
                    count += 1

                self.output_flow.write(result + '\n')
                self.output_flow.flush()
            line = self.input_flow.readline()
