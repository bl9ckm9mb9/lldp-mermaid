''' 
LLDP Mermaid App

	Python Script to run Ansible Playbook, providing a key word to target the site
	- generating a LLDP-based Mermaid Network Diagram 
 
'''
# Import argv to provide an argument in python script
# Using "subprocess" to run commands (i.e. "ansible-playbook nameofplay.yml")
from sys import argv
import subprocess
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
        return formatted_dev
    elif "pan" in item:
        fw.insert(1,item)
        formatted_dev = (''.join(fw))
        return formatted_dev
    else:
        rtr.insert(1,item)
        formatted_dev = (''.join(rtr))
        return formatted_dev

def arista_dev(line):
    my_list = line.split()
    del my_list[-1]
    local_port = my_list[0]
    local_port = local_port.strip('"')
    neigh_port = my_list[2]
    neigh_port = neigh_port[0:2]+neigh_port[-2:]
    lldp_neigh = my_list[1]
    lldp_neigh = lldp_neigh.split(".")[0]
    #lldp_neigh = dev_shape(lldp_neigh)
    lldp_link = "%s -->|%s <br><br>%s|%s\n" % (target_dev, local_port, neigh_port, lldp_neigh)
    # Insert your function to check for duplicate links, here.
    A = local_port
    B = (neigh_port[0:2]+neigh_port[-2:])
    link_pair = A + B
    reverse_pair = B + A
    if link_pair in links or reverse_pair in links:
        #print("Found a link duplicate.")
        pass
    else:
        links.append(link_pair)
        links.append(reverse_pair)
        #print("Adding to MD file.")
        lldp_diagram.write(lldp_link)

    #Insert code to write to MD file here.
    #lldp_diagram.write(lldp_link)
def juniper_dev(line):
    my_list = line.split()
    if my_list[-1] == '",':
        del my_list[-1]
    local_port = my_list[0]
    local_port = local_port.strip('"')
    neigh_port = my_list[-2]
    #neigh_port = neigh_port[0:2]+neigh_port[-2:]
    lldp_neigh = my_list[-1]
    lldp_neigh = lldp_neigh.strip('",')
    lldp_neigh = lldp_neigh.split(".")[0]
    #lldp_neigh = dev_shape(lldp_neigh)
    lldp_link = "%s -->|%s <br><br>%s|%s\n" % (target_dev, local_port, neigh_port, lldp_neigh)
    # Beginning of test block:
    link_pair = local_port+neigh_port
    reverse_pair = neigh_port+local_port
    if link_pair in links or reverse_pair in links:
        #print("Found a link duplicate.")
        pass
    else:
        links.append(link_pair)
        links.append(reverse_pair)
        #print("Adding to MD file.")
        lldp_diagram.write(lldp_link)

    # End of Test Block

    #lldp_diagram.write(lldp_link)

# Variable to use throughout script
user_input = argv
p = subprocess
hyphen = "-"
colon = ":"
neigh_port = ""
pair_dev = ""
links = []
master_list = []
pair_dev_list = []

'''
Testing via Ansible ad-hoc command:
Example of ansible command: 
ansible-playbook ~/myansible/lldp.yml --limit "hostname-here-sw"
'''

# This one works:
site = user_input[1]
myCmd = "ansible-playbook /Users/diegoavalos/myansible/lldp.yml --limit %s >> raw.txt" % (site)

# Used for testing ; bypassing sysargv variables
#myCmd = "ansible-playbook /Users/diegoavalos/myansible/lldp.yml --limit 'device-hostname' >> raw.txt"

# Telling user to wait while command runs.
print("... do the funky chicken for about 10 seconds.")

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
'''
Master list of port pairs to avoid duplicate links. 
Port pair: local_port + neigh_port ("Et43Et12") 
'''

with open("lldp-diagram.md","a+") as lldp_diagram:
    target_dev = ""
    local_port = ""
    lldp_neigh = ""
    neighbor = ""
    noise = "TTL"

    # Check line by line, reformat and write to final file: lldp-diagram.md
    for line in cleanedup_txt:
        if noise in line:
            pass
        elif "SUCCESS" in line:
            '''
            The split() func. will create a list of your string of text,
            splitting on empty spaces.
            '''
            my_list = line.split()
            #master_list.append(my_list[0])
            master_list.insert(0,my_list[0])
            target_dev = my_list[0]
            #target_dev = dev_shape(target_dev)
        elif (line.index("-")) == 11:
            # Juniper
            juniper_dev(line)
        else:
            # Arista version
            arista_dev(line)
        formatted_dev = dev_shape(target_dev)
    '''
    Reformatting and adding devices to a new list called: 'pair_dev_list'
    to define the device shape in mermaid syntax.
    '''
    for item in master_list:
        rfm_item = dev_shape(item)
        pair_dev = item + rfm_item
        pair_dev_list.insert(0, pair_dev)

    lldp_diagram.write("```\n \n")
'''
Writing to a new file from 'lldp-diagram.md' file to insert the 
list of elements at a certain point, ordering, and placing
lines where needed. This is a great place to insert new text.

Final file used to create the lldp mermaid diagram: site-diagram.md
'''
with open("lldp-diagram.md","r") as f:
    with open("site-diagram.md", "w") as site_diagram:
        site_diagram.write(graph_direction)
        for item in pair_dev_list:
            site_diagram.write(item+"\n")
        for line in f:
            site_diagram.write(line)

# Close all files.
raw_txt.close()
cleanedup_txt.close()
lldp_diagram.close()
site_diagram.close()

# Command to open file with default Markdown reader
open_typora = p.Popen(["open", "site-diagram.md"], stdout=subprocess.PIPE)
