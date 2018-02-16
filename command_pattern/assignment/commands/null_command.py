from . import command_abc

import logging


class NullCommand(command_abc.AbsCommand):
    def execute(self):
        logging.info('null command.')