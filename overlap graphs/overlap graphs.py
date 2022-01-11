#Overlap Graphs

'''
if using this to solve Rosalinds Overlaping Graphs problem make sure the input data does not have any newline characters in the input string.
for some reason i was getting a \n in ever data string. this will mess with the way my code reads the input data. i just manually removed the 
newline characters.
'''


class Vertex():
	def __init__(self, name, string, k):
		self.id = name
		self.contents = string
		self.k = k
		self.prefix = self.contents[:self.k]
		self.suffix = self.contents[-self.k:]
		
class Graph():
	def __init__(self):
		self.edges = {}
		
	def addEdge(self, vertA, vertB):
		if vertA.id not in self.edges.keys():	
			if vertB.id in self.edges.keys():
				if vertA.id in self.edges[vertB.id]:
					return			
			self.edges[vertA.id] = [vertB.id]
			return
		if (vertB.id not in self.edges[vertA.id]) and (vertA.contents != vertB.contents):
			self.edges[vertA.id] += [vertB.id]
				
	
raw_data = open('data.txt', 'r')					#open data file
data_text = raw_data.read()
data_text = data_text.replace(">", "")		#remove the > character from names of strings
data_text = data_text.split("\n")
	
k = 3										#the length of the prefix / suffix

G = Graph()

myVerts = []

for i in xrange(len(data_text) / 2):
	myVerts.append(Vertex(data_text[i*2],data_text[i*2 + 1], k))
	
for i in myVerts:
	for j in myVerts:
		if i == j:
			continue
		else:
			if i.suffix == j.prefix:
				G.addEdge(i, j)

output_data = open('out_data.txt', 'w')
			
for key in G.edges.keys():
	for item in G.edges[key]:
		output_data.write(key + " " + item + "\n")
		
raw_data.close()
output_data.close()

