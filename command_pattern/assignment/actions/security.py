import logging


class Security(object):
    def __init__(self):
        self._armed = False

    def arm(self):
        logging.info('Security system armed')
        self._armed = True

    def disarm(self):
        logging.info('Security disarmed')
        self._armed = False

    @property
    def armed(self):
        return self._armed
