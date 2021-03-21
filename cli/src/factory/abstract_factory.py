from abc import ABC, abstractmethod

from cli.src.command.command import Command


class AbstractFactory(ABC):
    """Abstract CLI parser interface.

    Declares set of commands:
    - cat
    - echo
    - pwd
    - wc
    - exit
    """

    @abstractmethod
    def cat(*args) -> Command:
        pass

    @abstractmethod
    def echo(*args) -> Command:
        pass

    @abstractmethod
    def pwd(*args) -> Command:
        pass

    @abstractmethod
    def wc(*args) -> Command:
        pass

    @abstractmethod
    def exit(*args) -> Command:
        pass
