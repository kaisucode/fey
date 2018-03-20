import os
import sys

from commands.execute import execute
from commands.find_fey import find_fey
from commands.list_commands import list_commands
from commands.add import add

import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='DEBUG: %(message)s')
#  logging.getLogger().disabled = True


#  Receiving arguments
n_arguments = len(sys.argv)
if n_arguments == 1: 
    print("No command specified. Exiting Fey")
    exit()

# Initializing directory
fey_argument = sys.argv[1]
if fey_argument == "init": 
    fey_location = os.getcwd()+"/.fey/"
    print("Initializing empty Fey directory in"+fey_location)
    os.makedirs(fey_location)
    exit()

original_directory = os.getcwd()
fey_location = find_fey(original_directory)     # Find where .fey is

if fey_argument == "ls": 
    list_commands(fey_location)
elif fey_argument == "add": 
    if n_arguments > 2 and sys.argv[2] == "-f": 
        print("Overriding old command")
        add(n_arguments, fey_location, sys.argv[3], 1)
    elif os.path.isfile(fey_location+sys.argv[2]+".sh"): 
        print("Command already exists. Please add -f to override")
    elif sys.argv[2] != "-f": 
        print("Adding new command")
        add(n_arguments, fey_location, sys.argv[2], 0)
    exit()
elif fey_argument == "rm": 
    fey_command = sys.argv[2]
    if not os.path.isfile(fey_location+fey_command+".sh"): 
        print("Command does not exist")
        exit()
    print("Are you sure you want to delete "+fey_command+"? (y/N)")
    if input().lower() != 'y': 
        print("Aborted")
        exit()
    command_location = fey_location+fey_command+".sh"
    logging.debug(command_location)
    os.system("rm %s" % command_location)
    print("Deleted command: %s" % fey_command)
else: 
    fey_command = sys.argv[1]+".sh"
    execute(original_directory, fey_location, fey_command)



