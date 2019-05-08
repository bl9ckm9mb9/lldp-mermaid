'''
Formatting de
'''
device = ["(","spn-burbank-pan",")"]

#def dev_shape():
#	firewall = ["(", ")"]
#	switch = ["[","]"]
#	router = ["((","))"]
#
#
#	for item in dev_list:
#		if "sw" in item:
#			firewall.insert(1,item)
#		elif "pan" in item:
#			switch.insert(1,item)
#		else:
#			router.insert(1,item)
#
#
#	print (''.join(switch))
#	print (''.join(router))
#	print (''.join(firewall))

print (''.join(device))

test = "This is my string of text.\n And this should be the new line."

file1 = open("test.txt", "a+")

file1.write(test)

file1 = open("test.txt", "r")

print file1.read()
