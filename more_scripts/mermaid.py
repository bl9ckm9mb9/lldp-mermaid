# Script to generate Mermdaid Diagram
'''
Formatting name of device for Mermaid diagram 
symbol.
'''
def dev_shape(item):

	fw = ["(", ")"]
	sw = ["[", "]"]
	rtr = ["((", "))"]

	if "sw" in item:
		sw.insert(1, item)
		formatted_dev = (''.join(sw))
	elif "pan" in item:
		fw.insert(1, item)
		formatted_dev = (''.join(fw))
	else:
		rtr.insert(1, item)
		formatted_dev = (''.join(rtr))

# Mermaid formatting:
graph_direction = "graph TD"

list_of_lldp_ports = []
# use list.append(elem) to add devices to your list
list_of_devices = []

''' File from previous run, containing the filtered
    output of the Ansible Playbook
''' 
play_lldp_file = open('play-lldp.txt', 'a+')
final_map = open('final_map.txt', 'a+')

with open("lldp-diagram.md","a+") as lldp_diagram:
    target_dev = ""
    local_port = ""
    lldp_neigh_port = ""
    lldp_neigh = ""
    #lldp_link = "%s ---|%s <br><br> %s| %s" % (target_dev, local_port, lldp_neigh_port, lldp_neigh)
    lldp_link = "%s -->|%s <br><br>|%s" % (formatted_target_dev, local_port, neighbor)
    noise = "TTL"
    # write type of file:
    lldp_diagram.write(graph_direction)
    # Check line by line, reformat and write to final_map
    for line in play_lldp_file:
        if noise in line:
            pass
        elif "SUCCESS" in line:
            split.line()
            target_dev = my_list[0]
            formatted_target_dev = dev_shape(target_dev)
            lldp_diagram.write(formatted_target_dev)
        else:
            my_list = split.line()
            local_port = my_list[0] 
            lldp_neigh = my_list[1]
            neighbor = dev_shape(lldp_neigh)
            play_lldp_file.write(lldp_link)

print "Code executed."  


play = ["ansible-playbook", "/Users/diegoavalos/myansible/lldp.yml", "i", "/Users/diegoavalos/myansible/hosts"]
