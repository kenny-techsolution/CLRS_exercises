def insertion_sort_recursive(seq,r):
	if r>=0:
		last = seq[r]
		print("last",last)
		r-=1
		# it's important that i = r-1. 
		i = r
		insertion_sort_recursive(seq,r)
		while i>=0 and last<seq[i]:
			seq[i+1]=seq[i]
			i-=1
		print(seq)
		seq[i+1]=last
	
input = [1,4,3,6,7,8,2,9]
print(insertion_sort_recursive(input,len(input)-1))