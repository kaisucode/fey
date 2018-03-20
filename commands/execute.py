import os
import sys
import logging

def execute(original_directory, fey_location, fey_command): 
    os.chdir(original_directory)    # Go back to original directory and execute command
    logging.debug("Executing "+fey_location+fey_command)
    #  os.system(fey_location+fey_command)
    exit()
