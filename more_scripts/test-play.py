#!/bin/bash/env Python3
''' Python Script to run Ansible Playbook, providing a key word to
execute the Playbook on - Project LLDP Mermaid App '''

# Import argv to provide an argument in python script
from sys import argv
# Using "subprocess" to run commands (i.e. "ansible-playbook nameofplay.yml")
import subprocess

# Variable to use throughout script
net_grp = argv
p = subprocess

# Testing via Ansible ad-hoc command:
ans_output = p.check_output(["ansible", "td-juniper", "-m", "ping"])

######################################################################################################

# Variables
hyphen = "-"
colon = ":"
unwanted = "msg"
new_file = open('play-lldp.txt', 'w+')
ans_output_file = open('raw-output.txt', 'w+')

######################################################################################################

# Write Ansible Playbook output to a txt file
ans_output_file.write(str(ans_output))


# Open file that contains Ansible Playbook output as the variable: 'f'
with open('ans_output_file.txt', 'w+') as f:
	# readlines(): format lines, as lists full of strings, to search for wanted text,
	# line by line.
	list_of_lines = f.readlines()

	# Iterate through content to filter out unwantend text
	for line in list_of_lines:
		if "msg" in line:
			pass
		elif "changed" in line:
			pass
		elif "stdout" in line:
			pass
		elif "table" in line:
			pass
		elif "SUCCESS" in line:
			pass
		# This adds line to new_file
		elif hyphen in line or colon in line:
			print(line[:-33]) # added for debugging and can be commented out when no longer needed
			new_file.write(line)

# Close new file:
ans_output_file.close()
new_file.close()

######################################################################################################

print(ans_output)
print(len(ans_output))
