#need to remember the graph. for important indices: i j p r.
def partition(seq,p,r):
	i = p-1
	pivat = seq[r]
	#pointer = [0]*len(seq)
	for j in range(p,r):
		if seq[j]<=seq[r]:
			i += 1
			seq[i],seq[j] = seq[j],seq[i]
		#pointer[j],pointer[i]=9,1
		#print(pointer,i, j)
		#print(seq)
		#pointer[j],pointer[i]=0,0
	seq[i+1],seq[r] = seq[r],seq[i+1]
	return i+1
	
def quicksort(seq,p,r):
	if p<r:
		q = partition(seq,p,r)
		#important that the bound value. q-1 and q+1. because q doesn't need to be included in the sorting. 
		quicksort(seq,p,q-1)
		quicksort(seq,q+1,r)

input = [2,8,7,1,3,5,6,4]
partition(input, 0, len(input)-1)
print(input)

input = [2,8,7,1,3,5,6,4]
quicksort(input, 0, len(input)-1)
print(input)