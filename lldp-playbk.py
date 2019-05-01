''' 
LLDP Mermaid App

	Python Script to run Ansible Playbook, providing a key word to target the site
	- generating a LLDP-based Mermaid Network Diagram 
 
'''

# Import argv to provide an argument in python script
# Using "subprocess" to run commands (i.e. "ansible-playbook nameofplay.yml")
from sys import argv
import subprocess
import os

''' 
My function for formatting
'''
def dev_shape(item):

	fw = ["(", ")"]
	sw = ["[","]"]
	rtr = ["((","))"]

	if "sw" in item:
		sw.insert(1,item)
		formatted_dev = (''.join(sw))
		str(formatted_dev)
	elif "pan" in item:
		fw.insert(1,item)
		formatted_dev = (''.join(fw))
		str(formatted_dev)
	else:
		rtr.insert(1,item)
		formatted_dev = (''.join(rtr))
		str(formatted_dev)


# Variable to use throughout script
user_input = argv
p = subprocess
hyphen = "-"
colon = ":"

'''
Testing via Ansible ad-hoc command:
Example of ansible command: 
ansible-playbook ~/myansible/lldp.yml --limit "spn-500-paula-dtg01-sw"
'''

# This one works:
site = user_input[1]
myCmd = "ansible-playbook /Users/diegoavalos/myansible/lldp.yml --limit %s >> raw.txt" % (site)

# Used for testing ; bypassing sysargv variables
# myCmd = "ansible-playbook /Users/diegoavalos/myansible/lldp.yml --limit spn-500-paula-prod-a-sw >> raw.txt"

# Telling user to wait while command runs. 
print "... stay funky for about 5 seconds."

# Run ansible command, and set output to string format
ans_output = p.call(myCmd,shell=True)
ans_output = str(ans_output)

# Create cleaned up text file for writing:
cleanedup_txt = open('cleanedup.txt','a+') 

# Clean up raw output and write to cleanedup.txt file
with open('raw.txt', 'a+') as raw_txt:
	raw_txt.write(ans_output)

with open('raw.txt', 'r+') as file:
	list_of_lines = file.readlines()
	for line in list_of_lines:
		if "msg" in line:
			pass
		elif "changed" in line:
			pass
		elif "stdout" in line:
			pass
		elif "table" in line:
			pass
		elif "master:0" in line:
			pass
		elif hyphen in line or colon in line:
			cleanedup_txt.write(line)		

# Mermaid formatting:
graph_direction = "```mermaid\n \ngraph LR \n"

''' 
File from previous run, containing the filtered
    output of the Ansible Playbook
''' 
cleanedup_txt = open('cleanedup.txt', 'a+')
diagram_txt= open('diagram.txt', 'a+')

with open("lldp-diagram.md","a+") as lldp_diagram:
    target_dev = ""
    local_port = ""
    #lldp_neigh_port = ""
    lldp_neigh = ""
    target_dev = ""
    neighbor = ""
    noise = "TTL"

    # write type of file:
    lldp_diagram.write(graph_direction)

    # Check line by line, reformat and write to final file: lldp-diagram.md
    for line in cleanedup_txt:
        if noise in line:
            pass
        elif "SUCCESS" in line:
        	# The split() func. will create a list of your string of text, 
        	# splitting on empty spaces
            my_list = line.split()
            target_dev = my_list[0]
            dev_shape(target_dev)
            lldp_diagram.write(target_dev)
        else:
            my_list = line.split()
            del my_list[-1]
            local_port = my_list[0] 
            lldp_neigh = my_list[-1]
            lldp_link = "%s -->|%s <br><br>|%s\n" % (target_dev, local_port, lldp_neigh)
            lldp_diagram.write(lldp_link)

    lldp_diagram.write("```\n \n")

# Close all files.
raw_txt.close()
cleanedup_txt.close()
lldp_diagram.close()


# Command to open file with default Markdown reader
open_typora = p.Popen(["open", "lldp-diagram.md"], stdout=subprocess.PIPE)


