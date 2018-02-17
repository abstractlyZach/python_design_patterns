import logging


class Security(object):
    def __init__(self, name):
        self._name = name
        self._armed = False

    def arm(self):
        if self._armed:
            raise Exception('{} are already armed.'.format(self._name))
        else:
            logging.info('{} armed'.format(self._name))
            self._armed = True

    def disarm(self):
        if self._armed:
            logging.info('{} disarmed'.format(self._name))
            self._armed = False
        else:
            raise Exception('{} are already disarmed.'.format(self._name))

    @property
    def armed(self):
        return self._armed
