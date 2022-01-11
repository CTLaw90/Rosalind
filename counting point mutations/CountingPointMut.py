#Counting Point Mutations

data_set = open('data.txt')
output_data = open('out_data.txt', 'w')

DNA_string = data_set.read()
DNA_string = DNA_string.replace('\n', '')

DNA_chars = ["A", "C", "G", "T"]

string_s = DNA_string[0:((len(DNA_string))//2)]
string_t = DNA_string[((len(DNA_string))//2):]

mutations = 0


for i in xrange(len(string_s)):
	if string_s[i] != string_t[i]:
		mutations += 1

		
print mutations		
output_data.write((str(mutations)));

data_set.close()
output_data.close()