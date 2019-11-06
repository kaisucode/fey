import os
import sys
import logging

from .tools import check_if_added_command

def add(n_arguments, fey_location, fey_command, force, fey_script): 
    command_location = fey_location+fey_command+".sh"
    logging.debug(command_location)

    if (not (n_arguments == 4 and force == 1)) or not os.path.isfile(command_location): 
        fout = open(command_location, "w")
        command_template = ("#!/bin/bash\n"
                            "#Type in the commands you wish to bind to \"%s\" below: \n")
        fout.write(command_template % fey_command)
        print(fey_command)
    else: 
        fout = open(command_location, "a")

    if n_arguments == 3+force: 
        fout.write("\n"*3)
        fout.close()
        os.system("nvim +3 "+command_location)
        if not check_if_added_command(command_location): 
            print("No changes made, command not added")
            os.system("rm %s" % command_location)
            return
    elif n_arguments == 4+force: 
        fout.write(fey_script)
        fout.close()
    else: 
        print("Too many arguments")
        return
    
    os.chmod(command_location, 0o775)


