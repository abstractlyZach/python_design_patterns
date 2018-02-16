import logging


class Door(object):
    def __init__(self, name):
        self.name = name
        self._locked = False

    def lock(self):
        logging.info("%s is locked." % self.name)
        self._locked = True

    def unlock(self):
        logging.info("%s is unlocked." % self.name)
        self._locked = False

    @property
    def locked(self):
        return self._locked