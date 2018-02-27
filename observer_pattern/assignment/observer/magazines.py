from . import abc_subject

class Magazine(abc_subject.AbsSubject):
    def __init__(self, name):
        super(Magazine, self).__init__()
        self._name = name

    def notify(self):
        for observer in self._observers:
            observer.update(self._name)

    def release_edition(self, release_name):
        self.notify()

    @property
    def name(self):
        return self._name