import logging


class Security(object):
    def __init__(self):
        self._armed = False

    def arm(self):
        if self._armed:
            raise Exception('Security system is already armed.')
        else:
            logging.info('Security system armed')
            self._armed = True

    def disarm(self):
        if self._armed:
            logging.info('Security disarmed')
            self._armed = False
        else:
            raise Exception('Security system is already disarmed.')

    @property
    def armed(self):
        return self._armed
