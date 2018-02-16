from . import command_abc


class LockCommand(command_abc.AbsCommand):
    def __init__(self, door):
        self._door = door

    def execute(self):
        self._door.lock()


class UnlockCommand(command_abc.AbsCommand):
    def __init__(self, door):
        self._door = door

    def execute(self):
        self._door.unlock()
