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
def dog_and_invoker():
    doggo = Security()
    activation_command = security_commands.ArmCommand(doggo)
    deactivation_command = security_commands.DisarmCommand(doggo)
    command_invoker = invoker.Invoker()
    command_invoker.set_object_commands(doggo, (activation_command,
                                                  deactivation_command))
    return doggo, command_invoker


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

def test_basic_security_arm(dog_and_invoker):
    dog, invoker = dog_and_invoker
    invoker.activate(dog)
    assert dog.armed

def test_basic_security_disarm(dog_and_invoker):
    dog, invoker = dog_and_invoker
    dog.arm()
    invoker.deactivate(dog)
    assert not dog.armed

def test_security_already_armed(dog_and_invoker):
    dog, invoker = dog_and_invoker
    dog.arm()
    with pytest.raises(Exception):
        dog.arm()

def test_security_already_disarmed(dog_and_invoker):
    dog, invoker = dog_and_invoker
    with pytest.raises(Exception):
        dog.disarm()


