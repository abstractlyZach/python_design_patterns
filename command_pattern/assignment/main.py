import logging

from actions.door import Door
from commands import door_commands
from commands import invoker


def open_door(door):
    open_command = door_commands.LockCommand(door)
    close_command = door_commands.UnlockCommand(door)
    command_invoker = invoker.Invoker()
    command_invoker.set_object_commands(door, (open_command, close_command))
    command_invoker.activate(door)

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s - %(message)s',
                        level=logging.INFO)

    door = Door('airlock')
    print('Door is open: {}'.format(not door.locked))
    open_door(door)
    print('Door is open: {}'.format(not door.locked))

