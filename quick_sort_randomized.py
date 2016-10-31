import random
def quicksort_rand(seq,p,r):
	if p<r:
		q = partition(seq,p,r)
		quicksort_rand(seq,p,q-1)
		quicksort_rand(seq,q+1,r)
	
def partition(seq,p,r):
	#randomize procedure
	rand = random.randrange(p,r)
	seq[rand],seq[r]= seq[r],seq[rand]
	i = p-1
	pivat = seq[r]
	for j in range(p,r):
		if seq[j]<=pivot:
			i+=1
			seq[i],seq[j]= seq[j],seq[i]
	seq[i+1],seq[r]= seq[r],seq[i+1]
	print(seq)
	return i+1
	
	
input = [2,8,7,1,3,5,6,4]
quicksort_rand(input, 0, len(input)-1)
#print(input)