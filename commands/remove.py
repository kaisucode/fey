import os
from .tools import getch

def remove(fey_location, fey_command): 
    if not os.path.isfile(fey_location+fey_command+".sh"): 
        print("Command does not exist")
        return
    print("Are you sure you want to delete "+fey_command+"? (y/N)")
    if getch().lower() != 'y': 
        print("Aborted")
    else: 
        command_location = fey_location+fey_command+".sh"
        os.system("rm %s" % command_location)
        print("Deleted command: %s" % fey_command)

