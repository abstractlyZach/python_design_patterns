import abc

class Strategy(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self, order):
        """Calculate the shipping cost of the order."""
