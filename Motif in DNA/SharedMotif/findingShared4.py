#rosalind finding a shared motif

#instead of creating a dict keeping track of all snips of code in which strings, 
#this will create a list of all snips from the first string and delete them as they are not found in the next strings

from trimmer import trim

raw_data = open('data.txt')
strings = trim(raw_data)

substrings = []

n = len(strings)

for j in range(2, len(strings[0]) + 1):			
	for k in range(len(strings[0]) - j + 1):	
		sub = strings[0][k:k+j]
		if (sub not in substrings):
			substrings.append(sub)

print('hi')			
			
for i in range(1, n):
	removeThese = []
	for sub in substrings:
		if sub not in strings[i]:
			removeThese.append(sub)
	for x in removeThese:
		substrings.remove(x)
	
print substrings[-1]