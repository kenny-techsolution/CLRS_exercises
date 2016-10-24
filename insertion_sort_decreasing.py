def insertion_sort_dec(seq):
	n = len(seq)
	for i in range(1,n):
		val = seq[i]
		j = i-1
		while j>=0 and val>seq[j]:
			seq[j+1]=seq[j]
			j-=1
		seq[j+1]= val
	return seq
	
input = list([4,1,3,6,3,7,8,9,10])

print(insertion_sort_dec(input))