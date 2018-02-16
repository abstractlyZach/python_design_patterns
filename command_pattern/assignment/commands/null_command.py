from . import command_abc

class NullCommand(command_abc.AbsCommand):
    def execute(self):
        print('null command.')