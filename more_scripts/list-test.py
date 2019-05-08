word = 'spn-td-2k-sw | SUCCESS'

print type(word)

with open("test.txt", "w+") as file:
	file.write(word)

content = file.open()

print content
