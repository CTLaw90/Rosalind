Perms = []


def rec(n, ign, list):

	if len(n) == len(ign):
		print "Appending", list
		Perms.append(str(list))
		return
    
	for char in n:
		if char not in ign:
			# print n, char, ign, list
			ign.append(char)
			list.append(char)
			print "Enter", n, char, list
			rec(n, ign, list)
			print "Exit", n, char, list
			list.remove(char)
			ign.remove(char)
			
    
    
rec([1,2,3], [], [])
print Perms