import abc

from . import abc_observer

class AbsSubject(metaclass=abc.ABCMeta):
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        if not isinstance(observer, abc_observer.Observer):
            raise TypeError("Tried to attach a non-observer class.")
        self._observers.update({observer})

    def detach(self, observer):
        self._observers.remove(observer)

    @abc.abstractmethod
    def notify(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observers.clear()