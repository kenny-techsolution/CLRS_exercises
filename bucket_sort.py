def bucket_sort(seq):
	#create bucket
	n=len(seq)
	b = [list() for i in range(n)]
	#put in the right bucket
	for i in range(n):
		val = n*seq[i]
		val = int(val)
		b[val].append(seq[i])
		
	#sort each list in the bucket.
	output = list([])
	for i in range(len(b)):
		insertion_sort(b[i])
		output = output + b[i]
	return output
		
	
def insertion_sort(seq):
	n = len(seq)
	if n<2:
		return seq
	for j in range(1,n):
		current = seq[j]
		current_pos = 0
		for k in range(j-1,-1,-1):
			if seq[k] > current:
				seq[k+1] = seq[k]
			else:
				current_pos = k+1
				break;
		seq[current_pos] = current
	return seq
	
input1 = [4,2,1,6,1,6,9,3,9,29]	

print(insertion_sort(input1))

input2 = list([4,1,3,6,3,7,8,9,10])

print(insertion_sort(input2))

input = [0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]	
print(bucket_sort(input))
