import abc

class AbsCommand(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass
