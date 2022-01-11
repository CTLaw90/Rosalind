#Counting DNA Nucleotides
data_set = open('data.txt')

DNA_string = data_set.read()
DNA_string = DNA_string.replace('\n', '')

alphabet = ["A", "C", "G", "T"]
counts = [0, 0, 0, 0]

string_len = len(DNA_string)

print DNA_string

for i in xrange(string_len):
	counts[(alphabet.index(DNA_string[i]))] += 1
	
print counts
