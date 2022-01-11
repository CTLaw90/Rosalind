#Mortal Fibonacci Rabbits

import time
start_time = time.time()

maxAge = 18 #where n == age of rabbit... -1 cause we start at 0
maxMonth = 40 #where m == current month... same as above

totOne = 0

def MortalRab(n=0, m=0, maxM=maxMonth):
	total = 0
	timeLeft = maxM - m
		
	if m == maxM:
		return 1
	if n == maxAge:
		if totOne != 0 and (timeLeft - 1) == maxAge:
			total += totOne
			
		else:
			total += MortalRab(0,m+1,maxM)
		return total
		
	total += MortalRab(n+1,m+1,maxM)
	
	if n > 0:
		if totOne != 0 and (timeLeft - 1) == maxAge:
			total += totOne
		else:
			total += MortalRab(0,m+1,maxM)

	return total
	
def RabHelper():
	return MortalRab(0,0,maxAge)
	
totOne = RabHelper()

print MortalRab()
print "---", time.time() - start_time,"---"