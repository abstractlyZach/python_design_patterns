from collections import defaultdict
from . import abc_observer

class Subscriber(abc_observer.Observer):
    def __init__(self, name):
        self._magazines_received = defaultdict(int)
        self._name = name

    def update(self, magazine_name):
        self._magazines_received[magazine_name] += 1

    @property
    def magazines_received(self):
        return self._magazines_received

    @property
    def name(self):
        return self._name
