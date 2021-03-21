from src.factory.abstract_factory import AbstractFactory
from src.command.cat import Cat
from src.command.command import Command
from src.command.echo import Echo
from src.command.exit import Exit
from src.command.pwd import Pwd
from src.command.wc import Wc


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
