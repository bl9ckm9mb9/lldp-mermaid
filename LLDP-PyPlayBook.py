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
ans_output = p.check_output(["ansible", "srx210", "-m", "ping"])

######################################################################################################

# Variables
hyphen = "-"
colon = ":"
play_lldp_file = open('play-lldp.txt', 'a+')

######################################################################################################

# Write Ansible Playbook output to a txt file
str(ans_output)


with open('ans-output-file.txt', 'a+') as ans_output_file:
	ans_output_file.write(ans_output)

	#print(ans_output_file.read())
	# Open file that contains Ansible Playbook output as the variable: 'f'
	with open('ans-output-file.txt', 'a+') as list_of_lines:
		# readlines(): format lines, as lists full of strings, to search for wanted text,
		# line by line.
		test = ans_output_file.readlines()
		print "Read line: %s" % test
		print "Hello... You are here, right at the doorstep of your loop."


		# Iterate through content to filter out unwantend text
		for line in list_of_lines:
			print "LOGIC KICKING IN!"
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
			# This adds line to play_lldp_file
			elif hyphen in line or colon in line:
				print "Entered your loop."
				print(line[:-33]) # added for debugging and can be commented out when no longer needed
				play_lldp_file.write(line)

# Checking if file is closed:
print(ans_output_file.closed), "ans_output_file is closed."

# Checking if 

contents = open('ans-output-file.txt','r+')
#contents = ans_output_file.open()
print "This is your ans_output_file:",contents.read()


# Close new file:
ans_output_file.close()
play_lldp_file.close()

