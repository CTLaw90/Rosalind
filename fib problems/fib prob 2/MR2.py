#mortal rabbits

max_age = 3			#the n
ticks = 6			#the m

current_rabbits = []

for x in range(max_age):
	current_rabbits.append([])

def rabbit(age):

	
	print current_rabbits, age
	
	global current_rabbits
	global max_age
	global offspring

	if age == max_age:
		rabbit(0)
		return
	
		
	return
	
	
rabbit(0)

print current_rabbits