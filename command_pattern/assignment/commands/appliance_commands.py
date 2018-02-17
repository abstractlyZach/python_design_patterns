from . import command_abc


class OnCommand(command_abc.AbsCommand):
    def __init__(self, appliance):
        self._appliance = appliance

    def execute(self):
        self._appliance.on()

    def undo(self):
        self._appliance.off()


class OffCommand(command_abc.AbsCommand):
    def __init__(self, appliance):
        self._appliance = appliance

    def execute(self):
        self._appliance.off()

    def undo(self):
        self._appliance.on()
