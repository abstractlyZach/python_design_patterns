from collections import defaultdict

from . import null_command


def get_null_commands():
    """Get two null commands."""
    return (null_command.NullCommand(), null_command.NullCommand())

class Invoker(object):
    """The object that tells commands to execute."""
    def __init__(self):
        self._object_commands = defaultdict(get_null_commands)

    def set_object_commands(self, object, commands):
        self._object_commands[object] = commands

    def activate(self, thing):
        """Activates the thing."""
        activation_command = self._object_commands[thing][0]
        activation_command.execute()

    def deactivate(self, thing):
        """Deactivate the thing."""
        deactivation_command = self._object_commands[thing][1]
        deactivation_command.execute()