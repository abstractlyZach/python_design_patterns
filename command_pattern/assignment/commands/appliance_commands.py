from . import command_abc


class OnCommand(command_abc.AbsCommand):
    def __init__(self, appliance):
        self._appliance = appliance

    def execute(self):
        self._appliance.on()


class OffCommand(command_abc.AbsCommand):
    def __init__(self, appliance):
        self._appliance = appliance

    def execute(self):
        self._appliance.off()
