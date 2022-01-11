#Consensus and Profile

data_set = open('data.txt')
output_data = open('out_data.txt', 'w')

DNA_strings = data_set.read()

list_of_strings = DNA_strings.split('>Rosalind_')
list_of_strings.pop(0)	#gets rid of a single '' left from split


for i in xrange(len(list_of_strings)):
	list_of_strings[i] = list_of_strings[i].replace('\n', '')
	list_of_strings[i] = list_of_strings[i][4:]
	
	
list_of_counts = [["A:" ], ["C:" ], ["G:" ], ["T:" ]]
alphabet = ["A", "C", "G", "T"]

consensus_list = []
consensus_string = ""
A_str = ""
C_str = ""
G_str = ""
T_str = ""

for col in xrange(len(list_of_strings[0])):
	counts = [0, 0, 0, 0]
	for row in xrange(len(list_of_strings)):
		counts[(alphabet.index(list_of_strings[row][col]))] += 1
		
	for i in xrange(4):
		list_of_counts[i].append(counts[i])
		
#get consensus	
for char in xrange(1, len(list_of_strings[0]) + 1):
	if list_of_counts[0][char] >= list_of_counts[1][char] and list_of_counts[0][char] >= list_of_counts[2][char] and list_of_counts[0][char] >= list_of_counts[3][char]:
		consensus_list.append("A")
	elif list_of_counts[1][char] >= list_of_counts[0][char] and list_of_counts[1][char] >= list_of_counts[2][char] and list_of_counts[1][char] >= list_of_counts[3][char]:
		consensus_list.append("C")
	elif list_of_counts[2][char] >= list_of_counts[0][char] and list_of_counts[2][char] >= list_of_counts[1][char] and list_of_counts[2][char] >= list_of_counts[3][char]:
		consensus_list.append("G")
	elif list_of_counts[3][char] >= list_of_counts[0][char] and list_of_counts[3][char] >= list_of_counts[2][char] and list_of_counts[3][char] >= list_of_counts[2][char]:
		consensus_list.append("T")

	
consensus_string = ''.join(consensus_list) + '\n'
A_str = ''.join(str(list_of_counts[0])) + '\n'
C_str = ''.join(str(list_of_counts[1])) + '\n'
G_str = ''.join(str(list_of_counts[2])) + '\n'
T_str = ''.join(str(list_of_counts[3]))

A_str =  A_str.replace('[', '')
A_str =  A_str.replace(']', '')
A_str =  A_str.replace(',', '')
A_str =  A_str.replace("'", '')

C_str =  C_str.replace('[', '')
C_str =  C_str.replace(']', '')
C_str =  C_str.replace(',', '')
C_str =  C_str.replace("'", '')

G_str =  G_str.replace('[', '')
G_str =  G_str.replace(']', '')
G_str =  G_str.replace(',', '')
G_str =  G_str.replace("'", '')

T_str =  T_str.replace('[', '')
T_str =  T_str.replace(']', '')
T_str =  T_str.replace(',', '')
T_str =  T_str.replace("'", '')
	
print consensus_string, A_str, C_str, G_str, T_str, len(consensus_string), len(A_str)
output_data.write(consensus_string);
output_data.write(A_str);
output_data.write(C_str);
output_data.write(G_str);
output_data.write(T_str);

data_set.close()
output_data.close()
