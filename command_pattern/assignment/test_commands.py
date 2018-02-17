import pytest
import testfixtures

from actions.appliance import Appliance
from actions.door import Door
from actions.security import Security
from commands import appliance_commands
from commands import door_commands
from commands import invoker
from commands import security_commands


@pytest.fixture
def door_and_invoker():
    test_door = Door('test door')
    activation_command = door_commands.LockCommand(test_door)
    deactivation_command = door_commands.UnlockCommand(test_door)
    command_invoker = invoker.Invoker()
    command_invoker.set_object_commands(test_door, (activation_command,
                                                   deactivation_command))
    return test_door, command_invoker


@pytest.fixture
def toaster_and_invoker():
    toaster = Appliance('toaster')
    activation_command = appliance_commands.OnCommand(toaster)
    deactivation_command = appliance_commands.OffCommand(toaster)
    command_invoker = invoker.Invoker()
    command_invoker.set_object_commands(toaster, (activation_command,
                                                    deactivation_command))
    return toaster, command_invoker


@pytest.fixture
def ninjas_and_invoker():
    ninjas = Security('ninjas')
    activation_command = security_commands.ArmCommand(ninjas)
    deactivation_command = security_commands.DisarmCommand(ninjas)
    command_invoker = invoker.Invoker()
    command_invoker.set_object_commands(ninjas, (activation_command,
                                                  deactivation_command))
    return ninjas, command_invoker


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

def test_cant_unlock_unlocked_door(door_and_invoker):
    door, invoker = door_and_invoker
    with pytest.raises(Exception):
        door.unlock()

def test_cant_lock_locked_door(door_and_invoker):
    door, invoker = door_and_invoker
    door.lock()
    with pytest.raises(Exception):
        door.lock()

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

def test_basic_appliance_on(toaster_and_invoker):
    toaster, invoker = toaster_and_invoker
    invoker.activate(toaster)
    assert toaster.is_on

def test_basic_appliance_off(toaster_and_invoker):
    toaster, invoker = toaster_and_invoker
    toaster.on()
    invoker.deactivate(toaster)
    assert not toaster.is_on

def test_appliance_already_on(toaster_and_invoker):
    toaster, invoker = toaster_and_invoker
    toaster.on()
    with pytest.raises(Exception):
        toaster.on()

def test_appliance_already_off(toaster_and_invoker):
    toaster, invoker = toaster_and_invoker
    with pytest.raises(Exception):
        toaster.off()

def test_basic_security_arm(ninjas_and_invoker):
    ninjas, invoker = ninjas_and_invoker
    invoker.activate(ninjas)
    assert ninjas.armed

def test_basic_security_disarm(ninjas_and_invoker):
    ninjas, invoker = ninjas_and_invoker
    ninjas.arm()
    invoker.deactivate(ninjas)
    assert not ninjas.armed

def test_security_already_armed(ninjas_and_invoker):
    ninjas, invoker = ninjas_and_invoker
    ninjas.arm()
    with pytest.raises(Exception):
        ninjas.arm()

def test_security_already_disarmed(ninjas_and_invoker):
    ninjas, invoker = ninjas_and_invoker
    with pytest.raises(Exception):
        ninjas.disarm()

class TestUndo(object):
    def test_on_undo(self, toaster_and_invoker):
        toaster, invoker = toaster_and_invoker
        invoker.activate(toaster)
        invoker.undo()
        assert not toaster.is_on

    def test_off_undo(self, toaster_and_invoker):
        toaster, invoker = toaster_and_invoker
        toaster.on()
        invoker.deactivate(toaster)
        invoker.undo()
        assert toaster.is_on

    def test_two_undos(self, door_and_invoker):
        door, invoker = door_and_invoker
        invoker.activate(door)
        invoker.deactivate(door)
        for i in range(2):
            invoker.undo()
        assert not door.locked

    def test_lots_of_undos(self, ninjas_and_invoker):
        ninjas, invoker = ninjas_and_invoker
        for i in range(30):
            invoker.activate(ninjas)
            invoker.deactivate(ninjas)
        for i in range(40):
            invoker.undo()
        assert not ninjas.armed

    def test_undo_too_many_times(self, ninjas_and_invoker):
        ninjas, invoker = ninjas_and_invoker
        with pytest.raises(Exception):
            invoker.undo()
