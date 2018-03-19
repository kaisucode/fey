
import os
import subprocess

command = """
# Get into .fey and find the file with the .sh file
# Trying to find .fey directory, if not found, cd .. and keep on looping. 
# test -f .fey && echo "Found" || echo "Not found"
until test -d .fey
do
	cd ..
	if [[ "$PWD" == "/" ]] ; then
		echo ".fey file not initiated"
		exit
	fi
done
fey_location=$(pwd)
echo "$fey_location"
"""

output = os.popen(command).readlines()
print(output)



