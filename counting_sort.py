#remember the step by step diagram
#so neat. 
def counting_sort(seq,k):
	c = [0]*(k+1)
	b = [0]*len(seq)
	#store the number of occurance of the seq[i]
	for i in range(0,len(seq)):
		c[seq[i]]+=1
	print(c)
	#calculate the starting position of each number index.
	for i in range(1,len(c)):
		c[i]+=c[i-1]
	print(c)
	#now render the number in the corrected position by iterating seq
	for i in range(0,len(seq)):
		#IMPORTANT: remember to -1, because python array index from 0.
		b[c[seq[i]]-1] = seq[i]
		c[seq[i]] -= 1
	print()
	return b
	
input = [2,5,3,0,2,3,0,3]
k=5	
print(counting_sort(input,k))