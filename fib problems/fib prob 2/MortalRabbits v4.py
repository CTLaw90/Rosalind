#Mortal Rabbits
#List approach

n = 89			#month to check population
m = 16			#lifespan of rabbits

rabbits = [1]
for i in xrange(1,m):
	rabbits.append(0)
	
month = 0
while month < n-1:
	# print month, rabbits
	newRabbits = 0
	for i in xrange(m-1, 0, -1):
		newRabbits += rabbits[i]
		rabbits[i] = rabbits[i-1]
	rabbits[0] = newRabbits
	month += 1

total = 0
# print month, rabbits
for i in rabbits:
	total += i
	
print "Rabbits at month", n, "-", total