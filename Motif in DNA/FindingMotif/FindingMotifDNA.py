#Finding a Motif in DNA

data_set = open('data.txt')
output_data = open('out_data.txt', 'w')

DNA_strings = data_set.read()
DNA_strings = DNA_strings.replace('\n', '')

strands = DNA_strings.split('-')

string_s = strands[0]
string_t = strands[1]

print string_s
print string_t

locations = []

for i in xrange(len(string_s)):
	if string_s[i:(len(string_t)+i)] == string_t:
		locations.append(i+1)

string_loc = ''.join(str(locations))
		
print string_loc

output_data.write(string_loc);

data_set.close()
output_data.close()