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

def indexOf(list1, piece): 
    return -1 if piece not in list1 else list1.index(piece)


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

force = indexOf(sys.argv, "-f")
force  = 1 if "-f" in sys.argv else 0



additional_message = 1
if force == 0 and n_arguments == 4: 
    fey_script = sys.argv[3]
elif force == 1 and n_arguments == 5: 
    fey_script = sys.argv[4]
else: 
    additional_message = 0




if fey_argument == "ls": 
    list_commands(fey_location)
    exit()
elif fey_argument == "add": 
    if n_arguments == 2: 
        print("No argument after \"add\"")
    elif n_arguments > 2 and force == 1: 
        print("Overriding old command")
        if additional_message == 0: 
            fey_script = sys.argv[3]
        add(n_arguments, fey_location, sys.argv[3], force, fey_script)
    elif os.path.isfile(fey_location+sys.argv[2]+".sh"): 
        print("Command already exists. Please add -f to override")
    else: 
        print("Adding new command")
        if additional_message == 0: 
            fey_script = sys.argv[2]
        add(n_arguments, fey_location, sys.argv[2], force, fey_script)
    exit()
elif fey_argument == "rm": 
    remove(fey_location, sys.argv[2])
    exit()
else: 
    fey_exe = sys.argv[1]+".sh"
    execute(original_directory, fey_location, fey_exe)
    exit()



