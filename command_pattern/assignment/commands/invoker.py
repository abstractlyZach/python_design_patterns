from collections import defaultdict

from . import null_command


class Invoker(object):
    """The object that tells commands to execute."""
    def __init__(self):
        self._object_commands = defaultdict(null_command.NullCommand)

    def set_object_commands(self, object, commands):
        self._object_commands[object] = commands

    def activate(self, thing):
        """Activates the thing."""
        activation_command = self._object_commands[thing][0]
        activation_command.execute()