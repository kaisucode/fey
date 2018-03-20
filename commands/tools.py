import os

#  Check if things are actually added
def check_if_added_command(command_location): 
    command_file = open(command_location).read().split('\n')
    command_file = command_file[2:]
    minimized_command_file = [line for line in command_file if line.strip()]
    if not minimized_command_file: 
        print("No changes made, command not added")
        os.system("rm %s" % command_location)


