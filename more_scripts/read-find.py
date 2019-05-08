# Script to run on Ansible-playbook Output and create new file for 
# mermaid flow chart/diagram

hyphen = "-"
colon = ":"
unwanted = "msg"
new_file = open('play-lldp.txt', 'w+')


# Open file that contains Ansible Playbook output as the variable: 'f'
with open('raw-lldp.txt', 'r+') as f:
	# readlines(): format lines, as lists full of strings, to search for wanted text,
	# line by line.
	list_of_lines = f.readlines()

	# Iterate through content to filter out unwatend text
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
		# Add line to new file
		elif hyphen in line or colon in line:
			print line[:-33] # added for debugging and can be commented out when no longer needed
			new_file.write(line)

# Close new file:
new_file.close()