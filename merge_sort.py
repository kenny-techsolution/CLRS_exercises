def merge(seq, p, q, r):
	#create two sub seq based on p i q indices
	left_seq = [seq[i] for i in range(p,q+1)]
	right_seq = [seq[i] for i in range(q+1,r+1)]
	sentinal = float("inf")
	left_seq.append(sentinal)
	right_seq.append(sentinal)
	#print(left_seq)
	#print(right_seq)
	l_index = r_index = 0
	for i in range(p,r+1):
		if left_seq[l_index]<right_seq[r_index]:
			seq[i]=left_seq[l_index]
			l_index +=1 
		else:
			seq[i]=right_seq[r_index]
			r_index +=1
	#return seq
		
def merge_sort(seq,p,r):
	# if p>=r, that means the seq only has one element, no need to do anymore merge_sort
	if p<r:
		print(p,r)
		mid = (p+r)/2
		merge_sort(seq,p,mid)
		merge_sort(seq,mid+1,r)
		merge(seq,p,mid,r)
		print("changed",seq)
	return seq

input = [5,2,4,7,1,3,2,6]
print(merge_sort(input,0,len(input)-1))