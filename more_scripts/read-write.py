######################################################################################################

# Variables
hyphen = "-"
colon = ":"
unwanted = "msg"
new_file = open('play-lldp.txt', 'a+')
ans_output_file = open('raw-output.txt', 'a+')

######################################################################################################
ans_output = "This is more string. Testing"
#with open('some-file.txt','a+') as ans_output:
#	ans_output.write("This is a test")


# Write Ansible Playbook output to a txt file
# str(ans_output)


with open('raw-output.txt', 'a+') as ans_output_file:
	ans_output_file.write(ans_output)
	# contents = ans_output_file.read()
	# print "This is your ans_output_file:",contents


	#print(ans_output_file.read())
	# Open file that contains Ansible Playbook output as the variable: 'f'
	with open('raw-output.txt', 'a+') as list_of_lines:
		# readlines(): format lines, as lists full of strings, to search for wanted text,
		# line by line.
		list_of_lines.readlines()
		read_list =  list_of_lines.read()
		print "This is your read_list:",read_list

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
			# This adds line to new_file
			elif hyphen in line or colon in line:
				print(line[:-33]) # added for debugging and can be commented out when no longer needed
				new_file.write(line)
print(ans_output_file.closed)

contents = open('raw-output.txt','r+')
print "This is your ans_output_file:",contents.read()

# Close new file:
ans_output_file.close()
new_file.close()

######################################################################################################

print(ans_output)