import logging


class Door(object):
    def __init__(self, name):
        self.name = name
        self._locked = False

    def lock(self):
        if self._locked:
            raise Exception('Door is already locked.')
        else:
            logging.info("%s is locked." % self.name)
            self._locked = True

    def unlock(self):
        if self._locked:
            logging.info("%s is unlocked." % self.name)
            self._locked = False
        else:
            raise Exception('Door is already unlocked.')

    @property
    def locked(self):
        return self._locked