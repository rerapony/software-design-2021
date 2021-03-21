from abc import ABC, abstractmethod


class Command(ABC):
    """The Command interface"""

    @abstractmethod
    def execute(*args):
        """Begin command execution"""
        pass

    @abstractmethod
    def __str__(self):
        pass
