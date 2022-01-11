#Transcribing DNA to RNA

data_set = open('data.txt')
output_data = open('out_data.txt', 'w')

DNA_string = data_set.read()
DNA_string = DNA_string.replace('\n', '')

DNA_chars = ["A", "C", "G", "T"]
RNA_chars = ["A", "C", "G", "U"]

RNA_list = []
RNA_string = ""

string_len = len(DNA_string)

for i in xrange(string_len):
	RNA_list.append(RNA_chars[DNA_chars.index(DNA_string[i])])
	
RNA_string = ''.join(map(str, RNA_list))

print RNA_string, type(RNA_string)

output_data.write(RNA_string);

data_set.close()
output_data.close()