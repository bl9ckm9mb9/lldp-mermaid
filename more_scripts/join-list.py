
'''
Formatting name of device for Mermaid diagram 
symbol.
'''

def dev_shape(item):

	fw = ["(", ")"]
	sw = ["[","]"]
	rtr = ["((","))"]

	if "sw" in item:
		sw.insert(1,item)
		formatted_dev = (''.join(sw))
	elif "pan" in item:
		fw.insert(1,item)
		formatted_dev = (''.join(fw))
	else:
		rtr.insert(1,item)
		formatted_dev = (''.join(rtr))

#	print formatted_dev

'''
Use function by inserting variable in the function: dev_shape(switch)
'''
