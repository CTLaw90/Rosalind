#Computing GC Content
data_set = open('data.txt')
output_data = open('out_data.txt', 'w')

DNA_string = data_set.read()
DNA_string = DNA_string.replace('\n', '')

DNA_sets = DNA_string.split('>Rosalind_')
DNA_sets.pop(0)

alphabet = ["A", "C", "G", "T"]

ratio = 0.0

results = []
results_string = ""

for j in DNA_sets:	
	counts = [0, 0, 0, 0]
	
	for i in xrange(len(j)):
		if j[i] in alphabet:
			counts[(alphabet.index(j[i]))] += 1	
		
	if counts[0] + counts[3] > 0:
		ratio =  100 * (float(counts[1]) + float(counts[2])) /  (float(counts[0]) + float(counts[1]) +float(counts[2]) + float(counts[3]))
		results.append('Rosalind_' + str(j)[0:4] + ' - ' + str(ratio))
	else:
		print "error"

results_string = '\n'.join(results)
print results_string

output_data.write(results_string);

data_set.close()
output_data.close()