#Translating RNA into Protein

codon_file = open('RNA codon table2.txt', 'r')
data_set = open('data.txt', 'r')
output_data = open('out_data.txt', 'w')

RNA_string = data_set.read()
RNA_string = RNA_string.replace('\n', '')

codon_data = codon_file.read()
codon_table = codon_data.split(' ')

num_codon = (len(RNA_string) / 3)
protein_list = []

temp_codon = ""
temp_protein = ""

protein_string = ""

for i in xrange(num_codon):
	temp_codon = RNA_string[(3*i):((i*3)+3)]
	temp_protein = codon_table[codon_table.index(temp_codon) + 1]
	if temp_protein == "Stop":
		protein_list.append('\n')
	else:
		protein_list.append(temp_protein)
	
protein_string = ''.join(protein_list)

print protein_string
	
output_data.write(protein_string);	
	
codon_file.close()
data_set.close()
output_data.close()