from abc import ABC, abstractmethod


class Command(ABC):
    """The Command interface"""

    @abstractmethod
    def execute(self, *args):
        """Begin command execution"""
        pass
