from src.factory.command_factory import CommandFactory
from src.parser import Parser
from sys import stdout as console


def main():
    parser = Parser(CommandFactory())

    while True:
        console.flush()
        console.write("> ")

        cmd = input()
        parser.parse(cmd)


if __name__ == "__main__":
    main()
