
line_tuple =        "xe-0/2/2           -                   00:1c:73:0b:d9:43   Ethernet41         spn-500-paula-dtg01-sw.spn.disney.com",

hyphen = "xe-0/2/2           -                   00:1c:73:0b:d9:43   Ethernet41         spn-500-paula-dtg01-sw.spn.disney.com"

def search_for_dev(tuple_x):
	if hyphen in tuple_x:
		print "Found the hyphen."
	else:
		print "Nothing."


search_for_dev(line_tuple)