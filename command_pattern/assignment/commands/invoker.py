from collections import defaultdict

from . import null_command


def get_null_commands():
    """Get two null commands."""
    return (null_command.NullCommand(), null_command.NullCommand())

class Invoker(object):
    """The object that tells commands to execute."""
    def __init__(self):
        self._object_commands = defaultdict(get_null_commands)
        self._history = []

    def set_object_commands(self, object, commands):
        self._object_commands[object] = commands

    def activate(self, thing):
        """Activates the thing."""
        activation_command = self._object_commands[thing][0]
        activation_command.execute()
        self._history.insert(0, activation_command)

    def deactivate(self, thing):
        """Deactivate the thing."""
        deactivation_command = self._object_commands[thing][1]
        deactivation_command.execute()
        self._history.insert(0, deactivation_command)

    def undo(self):
        command_to_undo = self._pop_most_recent_command()
        command_to_undo.undo()

    def _pop_most_recent_command(self):
        try:
            return self._history.pop(0)
        except IndexError:
            raise Exception('Tried to undo, but there are no '
                            'actions left to undo.')

