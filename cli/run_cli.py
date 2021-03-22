import sys

from cli.src.factory.command_factory import CommandFactory
from cli.src.parser import Parser
from cli.src.shell import Shell


def run_cli(input_flow, output_flow):
    parser = Parser()
    command_factory = CommandFactory()
    shell = Shell(command_factory, parser, input_flow, output_flow)

    while True:
        shell.run_shell()


if __name__ == "__main__":
    run_cli(sys.stdin, sys.stdout)
