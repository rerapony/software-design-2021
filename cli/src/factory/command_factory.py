from cli.src.command.cat import Cat
from cli.src.command.command import Command
from cli.src.command.echo import Echo
from cli.src.command.exit import Exit
from cli.src.command.pwd import Pwd
from cli.src.command.wc import Wc
from cli.src.factory.abstract_factory import AbstractFactory


class CommandFactory(AbstractFactory):
    """
    Commands factory interface implementation.
    Returns implemented commands:

    - cat
    - echo
    - pwd
    - wc
    - exit
    """
    def cat(*args) -> Command:
        return Cat()

    def echo(*args) -> Command:
        return Echo()

    def pwd(*args) -> Command:
        return Pwd()

    def wc(*args) -> Command:
        return Wc()

    def exit(*args) -> Command:
        return Exit()
