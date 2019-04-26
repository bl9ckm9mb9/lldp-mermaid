# Test opening and reading files


file = open("lldp_output.txt")

print file

result = file.find("spn")

print "Found %s in the file" % result

close(file)
