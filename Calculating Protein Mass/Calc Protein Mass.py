#Calculating Protein Mass

#import table
protein_file = open('protein mass table.txt')

protein_table = protein_file.read()
protein_table = protein_table.replace('\n', ' ')
proteins = protein_table.split(' ')

#import dataset
data_set = open('data.txt')
data = data_set.read()

output_data = open('out_data.txt', 'w')


Mass_Sum_Total = 0
#print proteins

for char in data:
	#print char
	#print proteins[proteins.index(char) + 1]
	Mass_Sum_Total += float(proteins[int(proteins.index(char)) + 1])
	
print Mass_Sum_Total

protein_file.close()
data_set.close()
output_data.close()
