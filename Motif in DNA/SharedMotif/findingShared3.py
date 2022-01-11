#rosalind finding a shared motif

#instead of creating a dict keeping track of all snips of code in which strings, 
#this will create a list of all snips from the first string and delete them as they are not found in the next strings
#accidently overrode the original v3 file which started with sets k = 2 and worked its way up. way too slow...
#this version works top down

from trimmer import trim
import time

start_time  = time.time()

raw_data = open('data.txt')
out_data = open('output.txt', 'w')
strings = trim(raw_data)

def find(strings):
	substrings = []

	n = len(strings)

	for j in range(len(strings[0]), 1, -1):			
		for k in range(len(strings[0]) - j + 1):	
			sub = strings[0][k:k+j]
			if (sub not in substrings):
				substrings.append(sub)

				
		for i in range(1, n):
			removeThese = []
			for sub in substrings:
				if sub not in strings[i]:
					removeThese.append(sub)
			for x in removeThese:
				substrings.remove(x)
				
		if substrings:
			return substrings
	
end = str(find(strings))
out_data.write(end)

raw_data.close()
out_data.close()

print (start_time - time.time())