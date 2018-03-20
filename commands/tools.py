
#  Check if things are actually added
def check_if_added_command(command_location): 
    command_file = open(command_location).read().split('\n')
    command_file = command_file[2:]
    minimized_command_file = [line for line in command_file if line.strip()]
    return minimized_command_file


