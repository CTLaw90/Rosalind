#ROSALIND
#INDEPENDENT ALLELES

#given k and N find the probability that N Aa Bb exist after k generations

k = 2			#k is the number of generations
N = 0			#N is the target number of Aa Bb that exist after k generations

probs = {	0 : [0.75,0.25,0.00],
			1 : [0.25,0.50,0.25],
			2 : [0.00,0.25,0.75]		}
			
total = {	0 : [1.00,1.00,1.00],
			1 : [1.00,1.00,1.00],
			2 : [1.00,1.00,1.00]		}
			
for i in xrange(k):
	for j in probs:
		for k in xrange(len(probs[j])):
			print j,k
			total[j][k] = total[j][k]*probs[j][k]
			
for key in total.keys():
	print total[key]