# Link Identification

port_A = int

port_B = int

link_1 = [port_A,port_B]

#if link_2 is link_1:
#	pass

list1 ="Ethernet44 Et31" 
new_list = list1.split()


#port_A = (new_list[1])
#port_B = (new_list[-1])

print(new_list)

#print(port_list)
print port_B
print port_A

list3 = [
"spn-500-paula-sw -->|xe-1/2/3 <br><br>xe-1/3/0|spn-500-paula",
"spn-500-paula-sw -->|ge-0/0/18 <br><br>dc:4a:3e:70:30:1f|dc:4a:3e:70:30:1f",
"spn-500-paula-prod-a-sw -->|Et2 <br><br>510|spn-lab-srx210-1",
"spn-500-paula-prod-a-sw -->|Et27 <br><br>Ethernet43|spn-500-paula-dtg01-sw",
"spn-500-paula-prod-a-sw -->|Et28 <br><br>Ethernet44|spn-500-paula-dtg01-sw"
]


#print("Sammy has {} balloons.".format(5))
#
#open_string = "Sammy loves {}."
#print(open_string.format("open source"))

no_pipes = ("spn-500-paula-sw -->|xe-1/2/3 <br><br>xe-1/3/0|spn-500-paula".split("|").split("<vr>"))
print(no_pipes)