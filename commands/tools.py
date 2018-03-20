
#  Check if things are actually added
def check_if_added_command(command_location): 
    command_file = open(command_location).read().split('\n')
    command_file = command_file[2:]
    minimized_command_file = [line for line in command_file if line.strip()]
    return minimized_command_file

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print(ch)
        return ch
getch = _GetchUnix()


