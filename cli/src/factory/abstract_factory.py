from abc import ABC, abstractmethod


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
    def cat_cmd(self):
        pass

    @abstractmethod
    def echo_cmd(self):
        pass

    @abstractmethod
    def pwd_cmd(self):
        pass

    @abstractmethod
    def wc_cmd(self):
        pass

    @abstractmethod
    def exit_cmd(self):
        pass

    @abstractmethod
    def grep_cmd(self):
        pass
