#Complementing a Strand of DNA

data_set = open('data.txt')
output_data = open('out_data.txt', 'w')

DNA_string = data_set.read()
DNA_string = DNA_string.replace('\n', '')

DNA_chars = ["A", "C", "G", "T"]
DNAc_chars = ["T", "G", "C", "A"]

DNAc_list = []
DNAc_string = ""

string_len = len(DNA_string)

for i in xrange(string_len-1,-1,-1):
	DNAc_list.append(DNAc_chars[DNA_chars.index(DNA_string[i])])
	
DNAc_string = ''.join(map(str, DNAc_list))

output_data.write(DNAc_string);

data_set.close()
output_data.close()