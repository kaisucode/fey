import os

def list_commands(fey_location): 
    all_commands = os.listdir(fey_location)
    print(fey_location)
    if not all_commands: 
        print("└── "+"(empty)")
    else: 
        for command in all_commands[:-1]: 
            print("├── "+command[:-3])
        print("└── "+all_commands[-1][:-3])
