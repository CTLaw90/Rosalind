#ROSALIND
#INDEPENDENT VARIABLES

k = 0
n = 0


'''
probability of n offspring of phenotype Aa Bb existing at gen k = 
(p(AA BB) + p(Aa Bb) + p(aa bb))X(Aa Bb)

	X Aa
AA [.5,.5,0]
Aa [.25,.5,.25]
aa [0,.5,.5]

'''

probGraph = [[[0.5],[0.5],[0]] , [[0.25],[0.5],[0.25]] , [[0],[0.5],[0.5]]]

curProb = [[0.25],[0.5],[0.25]] #after first gen
newProb = [[.25 x .5 + .5 x .25 + .25 x 0

for j in xrange(k):
	newProb[0] =  