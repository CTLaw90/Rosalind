#Enumerating k-mers lexicographically

data_set = open('data.txt', 'r')
output_data = open('output.txt', 'w')

alphabet = data_set.readline()
max_depth = data_set.readline()

alphabet = alphabet.replace('\n', '')
alphabet_arr = alphabet.split(' ')

strings = []

def Next_Depth(buffy, depth):
	# print "Entering Depth: ", depth, "Buffy: ", buffy
	if depth == int(max_depth):
		strings.append(str(buffy))
		return
		
	for letter in alphabet_arr:
		buffy[depth] = letter
		Next_Depth(buffy, depth + 1)
		buffy[depth] = ''
		
base = []

for x in range(int(max_depth)):
	base.append('')

Next_Depth(base, 0)
		
for perm in strings:
	perm = perm.replace("'" , '')
	perm = perm.replace(' ' , '')
	perm = perm.replace('[' , '')
	perm = perm.replace(']' , '')
	perm = perm.replace(',' , '')
	# print perm
	output_data.write(perm + '\n')


data_set.close()
output_data.close()
