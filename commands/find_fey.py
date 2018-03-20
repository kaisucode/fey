import os
import sys
import logging

def find_fey(original_directory): 
    while not os.path.isdir(".fey/"): 
        os.chdir("..")
        if os.getcwd() == "/": 
            print("No .fey file found")
            exit()
    fey_location = os.getcwd()+"/.fey/"
    logging.debug("Found .fey: "+fey_location)
    return fey_location

