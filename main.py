import os
import sys

from commands.execute import execute
from commands.find_fey import find_fey
from commands.list_commands import list_commands
from commands.tools import check_if_added_command

import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='DEBUG: %(message)s')
#  logging.getLogger().disabled = True


# Message for the <commands>.sh files in .fey
command_template_line1 = "#!/bin/bash"
command_template_line2 = """#Type in the commands you wish to bind to "%s" below: """





#  Receiving arguments
n_arguments = len(sys.argv)
if n_arguments == 1: 
    print("No command specified. Exiting Fey")
    exit()

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
    fey_command = sys.argv[2]
    command_location = fey_location+fey_command+".sh"
    if os.path.isfile(command_location): 
        print("Command already exists. Please add -f to override")
        exit()

    if sys.argv[2] != "-f": 
        print("Adding new command")
        logging.debug(command_location)
        fout = open(command_location, "w")
        fout.write(command_template_line1 + "\n" + command_template_line2 % fey_command + "\n")
        if n_arguments == 3: 
            fout.write("\n"*3)
            fout.close()
            os.system("nvim "+command_location)
            check_if_added_command(command_location)
        elif n_arguments == 4: 
            fey_command = sys.argv[3]
            fout.write(fey_command)
            fout.close()
        else: 
            print("Too many arguments")
            
    elif n_arguments > 2 and sys.argv[2] == "-f": 
        fey_command = sys.argv[3]
        print("Overriding old command")
    exit()
else: 
    fey_command = sys.argv[1]+".sh"
    execute(original_directory, fey_location, fey_command)



