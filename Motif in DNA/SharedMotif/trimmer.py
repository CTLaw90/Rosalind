#script for trimming '>Rosalind_XXXX' string header & string breaking '\n' from data files

def trim(raw_data):
	strings = raw_data.read()
	strings = strings.split('>')

	strings.remove('')

	final = []
	
	for s in strings:
		s = s.split('\n')
		s.remove(s[0])
		if '' in s:
			s.remove('')
		s = ''.join(s)
		final.append(s)
		
	return final
