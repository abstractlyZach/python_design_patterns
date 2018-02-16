import pytest

from actions.door import Door
from commands import door_commands
from commands import invoker


@pytest.fixture
def door_and_invoker():
    test_door = Door('test door')
    open_command = door_commands.LockCommand(test_door)
    close_command = door_commands.UnlockCommand(test_door)
    command_invoker = invoker.Invoker()
    command_invoker.set_object_commands(test_door, (open_command,
                                                   close_command))
    return test_door, command_invoker


def test_basic_door_lock(door_and_invoker):
    door, invoker = door_and_invoker
    invoker.activate(door)
    assert door.locked

def test_basic_door_unlock(door_and_invoker):
    door, invoker = door_and_invoker
    door.unlock()
    invoker.deactivate(door)
    assert not door.locked


