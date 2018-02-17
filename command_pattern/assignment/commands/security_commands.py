from . import command_abc


class ArmCommand(command_abc.AbsCommand):
    def __init__(self, security_system):
        self._system = security_system

    def execute(self):
        self._system.arm()

    def undo(self):
        self._system.disarm()


class DisarmCommand(command_abc.AbsCommand):
    def __init__(self, security_system):
        self._system = security_system

    def execute(self):
        self._system.disarm()

    def undo(self):
        self._system.arm()
