from abc import ABC, abstractmethod


class Command(ABC):
    """The Command interface"""

    @abstractmethod
    def execute(self, result, count, *args):
        """Begin command execution"""
