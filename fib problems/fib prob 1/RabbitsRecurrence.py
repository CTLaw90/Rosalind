#Rabbits and Recurrence Relations

#k = rabbit pairs produced by each pair
#n = number of months

k = 4
n = 29

fib = [1] * (n+1)
fib[0] = 0

for x in xrange(2,n+1):
	fib[x] = fib[x-1] + (fib[x-2]*k)

	
print "Rabbits after", n, "months: ", fib[n]