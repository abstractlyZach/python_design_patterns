import logging


class Appliance(object):
    def __init__(self, name):
        self._name = name
        self._is_on = False

    def on(self):
        if self._is_on:
            raise Exception('{} is already on.'.format(self._name))
        else:
            logging.info('%s has been turned on.' % self._name)
            self._is_on = True

    def off(self):
        if self._is_on:
            logging.info('%s has been turned off.' % self._name)
            self._is_on = False
        else:
            raise Exception('{} is already off.'.format(self._name))

    @property
    def is_on(self):
        return self._is_on