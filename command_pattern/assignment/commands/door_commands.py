from . import command_abc


class LockCommand(command_abc.AbsCommand):
    def __init__(self, door):
        self._door = door

    def execute(self):
        self._door.lock()

    def undo(self):
        self._door.unlock()


class UnlockCommand(command_abc.AbsCommand):
    def __init__(self, door):
        self._door = door

    def execute(self):
        self._door.unlock()

    def undo(self):
        self._door.lock()
