from collections import namedtuple
import logging

from actions.appliance import Appliance
from actions.door import Door
from actions.security import Security
from commands import appliance_commands
from commands import door_commands
from commands import security_commands
from commands.invoker import Invoker


NameToObject = namedtuple('NameToObject', 'appliances doors security_systems')

def set_up_logging():
    logging.basicConfig(format='%(levelname)s - %(message)s',
                        level=logging.INFO)

def get_appliances():
    appliance_names = ['toaster', 'smart fridge', 'George Foreman grill']
    return {name: Appliance(name) for name in appliance_names}

def get_doors():
    door_names = ['front door', 'back door', 'secret bookcase door',
                  'lab door', 'interdimensional portal']
    return {name: Door(name) for name in door_names}

def get_security_systems():
    system_names = ['ninjas', 'drones', 'doggos', 'stern disciplinarians',
                    'sharks', 'weaponized flu']
    return {name: Security(name) for name in system_names}

def get_appliance_commands(appliance_dict):
    return {appliance: appliance_commands.make_commands(appliance)
            for appliance in appliance_dict.values()}

def get_door_commands(door_dict):
    return {door: door_commands.make_commands(door)
            for door in door_dict.values()}

def get_security_commands(security_systems_dict):
    return {security_system: security_commands.make_commands(security_system)
            for security_system in security_systems_dict.values()}

def get_things_dict():
    appliances = get_appliances()
    doors = get_doors()
    security_systems = get_security_systems()
    return NameToObject(appliances, doors, security_systems)

def get_smushed_dict(names_to_object_dict):
    appliances, doors, security_systems = names_to_object_dict
    to_return = {}
    to_return.update(appliances)
    to_return.update(doors)
    to_return.update(security_systems)
    return to_return

def set_up_invoker(things_dict):
    invoker = Invoker()
    appliances, doors, security_systems = things_dict
    appliance_commands = get_appliance_commands(appliances)
    door_commands = get_door_commands(doors)
    security_commands = get_security_commands(security_systems)
    types_of_commands = [appliance_commands, door_commands, security_commands]
    for type_of_command in types_of_commands:
        for object, command in type_of_command.items():
            invoker.set_object_commands(object, command)
    return invoker






if __name__ == '__main__':
    set_up_logging()
    logging.info('Application initializing...')
    things = get_things_dict()
    invoker = set_up_invoker(things)
    things = get_smushed_dict(things)
    logging.info('Application started.')

    invoker.activate(things['ninjas'])





