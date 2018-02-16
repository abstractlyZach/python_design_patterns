from actions.door import Door
from commands import door_commands
from commands import invoker

def test_door():
    door = Door()
    open_command = door_commands.OpenCommand(door)
    close_command = door_commands.CloseCommand(door)
    command_invoker = invoker.Invoker()
    command_invoker.set_object_commands(door, (open_command, close_command))
    command_invoker.activate(door)


