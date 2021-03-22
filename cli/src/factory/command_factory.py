from cli.src.command.cat import Cat
from cli.src.command.echo import Echo
from cli.src.command.exit import Exit
from cli.src.command.grep import Grep
from cli.src.command.pwd import Pwd
from cli.src.command.wc import Wc
from cli.src.command.cd import Cd
from cli.src.command.ls import Ls
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
    - grep
    """

    def cat_cmd(self):
        return Cat()

    def echo_cmd(self):
        return Echo()

    def pwd_cmd(self):
        return Pwd()

    def wc_cmd(self):
        return Wc()

    def exit_cmd(self):
        return Exit()

    def grep_cmd(self):
        return Grep()

    def cd_cmd(self):
        return Cd()

    def ls_cmd(self):
        return Ls()
