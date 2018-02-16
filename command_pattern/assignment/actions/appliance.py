import logging


class Appliance(object):
    def __init__(self, name):
        self._name = name

    def on(self):
        logging.info('%s has been turned on.' % self._name)

    def off(self):
        logging.info('%s has been turned off.' % self._name)