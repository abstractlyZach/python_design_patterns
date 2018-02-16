import pytest
import testfixtures

from actions.door import Door
from commands import door_commands
from commands import invoker


@pytest.fixture
def door_and_invoker():
    test_door = Door('test door')
    activation_command = door_commands.LockCommand(test_door)
    deactivation_command = door_commands.UnlockCommand(test_door)
    command_invoker = invoker.Invoker()
    command_invoker.set_object_commands(test_door, (activation_command,
                                                   deactivation_command))
    return test_door, command_invoker


def test_basic_door_lock(door_and_invoker):
    door, invoker = door_and_invoker
    invoker.activate(door)
    assert door.locked


def test_basic_door_unlock(door_and_invoker):
    door, invoker = door_and_invoker
    door.lock()
    invoker.deactivate(door)
    assert not door.locked

def test_door_lock_and_unlock(door_and_invoker):
    door, invoker = door_and_invoker
    invoker.activate(door)
    invoker.deactivate(door)
    assert not door.locked

def test_door_unlock_and_lock(door_and_invoker):
    door, invoker = door_and_invoker
    door.lock()
    invoker.deactivate(door)
    invoker.activate(door)
    assert door.locked



def test_null_command_if_unrecognized_object_activated():
    with testfixtures.LogCapture() as l:
        command_invoker = invoker.Invoker()
        command_invoker.activate('abc')
    l.check(('root', 'INFO', 'null command.'))


def test_null_command_if_unrecognized_object_deactivated():
    with testfixtures.LogCapture() as l:
        command_invoker = invoker.Invoker()
        command_invoker.deactivate('abc')
    l.check(('root', 'INFO', 'null command.'))

