def randomized_select(seq,p,r,i):
	q = randomized_partition(seq,p,r)
	if q == i:
		return seq[q]
	elif q > i:
		return randomized_select(seq,p,q-1,i)
	else:
		return randomized_select(seq,q+1,r,i)

def randomized_partition(seq,p,r):
	pivot = seq[r]
	i = p-1
	for j in range(p,r):
		if seq[j]<pivot:
			i+=1
			seq[j], seq[i]=seq[i],seq[j]
	seq[i+1], seq[r]= seq[r], seq[i+1]
	return i+1

#sorted= [1, 2, 3, 6, 7, 8, 9, 12]
input = [1,3,12,2,9,7,6,8]

#print(randomized_partition(input,0,len(input)-1))
		
print(randomized_select(input,0,len(input)-1,4))