#Calculating Expected Offspring

prob = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
num_couple = [17852, 17126, 17666, 17487, 16679, 16704]

total_prob = 0

for i in xrange(len(prob)):
	total_prob += 2 * (prob[i] * num_couple[i])
	
print total_prob