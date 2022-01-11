#rosalind finding a shared motif

from trimmer import trim

raw_data = open('data.txt')
strings = trim(raw_data)

substrings = {}

n = len(strings)

for i in range(n):									#iterate through each string in our file
	for j in range(2, len(strings[i]) + 1):			#iteration size, staritng with duples and up to n-tuples
		for k in range(len(strings[i]) - j + 1):	#iteration starting index
			sub = strings[i][k:k+j]
			if (sub not in substrings.keys()):
				substrings[sub] = [i]
			elif (i not in substrings[sub]):
				substrings[sub].append(i)
				
for x in substrings.keys():
	if len(substrings[x]) == n:
		print x