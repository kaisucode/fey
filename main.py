import os
import sys

global debug
debug = 1
def debugger(message): 
    if debug: 
        print("Debugger:", message)


#  Receiving arguments
#  sys.argv is an list of all the arguments, including the command
if len(sys.argv) == 1: 
    print("No command specified. Exiting Fey")
    exit()
fey_command = sys.argv[1]
if len(sys.argv) > 2:
    for argument in sys.argv[2:]: 
        fey_command += "\ "+argument
fey_command += ".sh"
debugger("Command file is "+fey_command)

#  Find where .fey is
original_directory = os.getcwd()
while not os.path.isdir(".fey/"): 
    os.chdir("..")
    if os.getcwd() == "/": 
        print("No .fey file found")
        exit()
fey_location = os.getcwd()+"/.fey/"
debugger("Found .fey: "+fey_location)

# Go back to original directory and execute command
os.chdir(original_directory)
debugger(fey_location+fey_command)
#  os.system(fey_location+fey_command)



