#Rosalind Finding a Shared Motif
#Using the Apriori algorithm

from trimmer import trim

def FreqItem(T, A, sup):
	'''
	Where T is the array we wish to search, A is a list of the candidates, and sup is the support values
	'''
	
	canVals = {}
	
	for subArr in T:
		for candidate in A:
			if candidate in subArr:
				if candidate in canVals:
					canVals[candidate] += 1
				else:
					canVals[candidate] = 1
								
	# for key in canVals.keys():
		# print key, canVals[key]
		
	validCan = []
	for key in canVals.keys():
		if canVals[key] >= sup:
			validCan.append(key)

			
	return validCan
		
		
def GetCan(F):
	'''
	Where F is our candidates from Fk
	'''
	Cans = []
	for x in xrange(len(F)):
		for y in xrange(len(F)):
			newCan = []
			newCan.append(F[x])
			newCan.append(F[y])
			Cans.append(''.join(newCan))
	return Cans

def Apriori(T, sup):
	'''
	Where T is the array we wish to search and sup is the support
	'''
	k = 1
	freqItemsDict = {}
	freqItemsDict[1] = ['A', 'T', 'C', 'G']
	
	while freqItemsDict[k]:
		candidates = GetCan(freqItemsDict[k])
		freqItemsDict[k+1] = FreqItem(T, candidates, sup)
		k += 1
		
	# for key in freqItemsDict.keys():
		# print key, freqItemsDict[key]
		
	return freqItemsDict[k-1]
	
raw_data = open('data.txt', 'r')
list_data = trim(raw_data)

# string_name = []
# string_cont = []

# for i in xrange(0, len(list_data), 2):
	# string_cont.append(list_data[i+1])
	

print Apriori(list_data, len(list_data))