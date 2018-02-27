import abc

class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        pass

    def __enter__(self):
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

