#Mortal Fibonacci Rabbits

import time

start = time.clock()

#n = number of months
#m = number of months rabbits live

n = 8
m = 3

fibs = [0] * (n+1)
fibs[1] = 1


for x in xrange(2,n+1):
	fibs[x] = fibs[x-1] + fibs[x-2]

def get_rab(x):
	if x < m:
		return fibs[m]
	else:
		return fibs[x] + get_rab(x-m)

# print "Rabbits after", n, "months: ", len(rabbits)

print fibs[n] - get_rab(n-m)

end = time.clock()
print "Time :" , end - start , "seconds"
