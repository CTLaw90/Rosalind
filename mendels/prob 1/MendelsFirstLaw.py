#Mendel's First Law

#k - homo dom
#m - hetero
#n - homo rec

k = 27.0
m = 19.0
n = 28.0

tot = k + m + n

t = tot - 1

hh = 0.75
hr = 0.5

kprob = k / tot
mprob = (m / tot) * ((k/t) + (((m-1)/t)*hh) + (n/t)*hr)
nprob = (n / tot) * ((k/t) + (m/t)*hr)

tot_prob = kprob + mprob + nprob

print tot_prob
