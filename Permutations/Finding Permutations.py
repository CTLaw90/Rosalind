Perms = []
Sum = 0
N = 5


def Get_Next_Digit(n, ign, list):
	global Sum

	if len(n) == len(ign):
		# print "Appending", list
		Perms.append(str(list))
		Sum += 1
		return
    
	for char in n:
		if char not in ign:
			# print n, char, ign, list
			ign.append(char)
			list.append(char)
			# print "Enter", n, char, list
			Get_Next_Digit(n, ign, list)
			# print "Exit", n, char, list
			list.remove(char)
			ign.remove(char)
			
  
  
array = []

for x in range(N):
	array.append(x + 1)
 
 
Get_Next_Digit(array, [], [])
print Sum

for perm in Perms:
	perm = perm.replace('[' , '')
	perm = perm.replace(']' , '')
	perm = perm.replace(',' , '')
	print perm
