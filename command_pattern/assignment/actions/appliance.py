import logging


class Appliance(object):
    def __init__(self, name):
        self._name = name
        self._is_on = False

    def on(self):
        logging.info('%s has been turned on.' % self._name)
        self._is_on = True

    def off(self):
        logging.info('%s has been turned off.' % self._name)
        self._is_on = False

    @property
    def is_on(self):
        return self._is_on