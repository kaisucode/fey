import os
import sys

from commands.execute import execute
from commands.find_fey import find_fey
from commands.list_commands import list_commands
from commands.add import add
from commands.remove import remove

import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='DEBUG: %(message)s')
logging.getLogger().disabled = True


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
    exit()
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
    remove(fey_location, sys.argv[2])
    exit()
else: 
    fey_command = sys.argv[1]+".sh"
    execute(original_directory, fey_location, fey_command)
    exit()



