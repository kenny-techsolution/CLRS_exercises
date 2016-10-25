def insertion_sort_recursive(seq,p,q):
	if q>p:
		last = seq[q]
		#print("last",last)
		q-=1
		# it's important that i = r-1. 
		i = q
		insertion_sort_recursive(seq,p,q)
		while i>=p and last<seq[i]:
			seq[i+1]=seq[i]
			i-=1
		#print(seq)
		seq[i+1]=last
	return seq
	
def merge(seq,p,q,r):
	#create two sub seq left and right
	#print(seq)
	left_seq = [seq[i] for i in range(p,q+1)]
	right_seq = [seq[i] for i in range(q+1,r+1)]
	#print(left_seq, right_seq)
	for i in range(p,r+1):
		if len(left_seq)==0:
			seq[i]=right_seq.pop(0)
		elif len(right_seq)==0:
			seq[i]=left_seq.pop(0)
		else:
			if left_seq[0]<right_seq[0]:
				seq[i]=left_seq.pop(0)
			else:
				seq[i]=right_seq.pop(0)
	return seq

def insertion_merge_hybrid_sort(seq,p,q):
	threshold = 10
	#print(seq,p,q)
	#print(q-p+1<=threshold)
	if q-p+1<=threshold:
		insertion_sort_recursive(seq,p,q)
	else:
		mid = (p+q)/2
		insertion_merge_hybrid_sort(seq,p,mid)
		insertion_merge_hybrid_sort(seq,mid+1,q)
		merge(seq,p,mid,q)
	return seq

input = [8,7,6,3,10,3,4,7,20,31,64,42,32,13,29]
input2 = [3, 3, 4, 6, 7, 7, 8, 10, 20, 31, 42, 64, 13, 29, 32]
#print(insertion_sort_recursive(input,0,3))
#print(merge(input2,8,11,14))
print(insertion_merge_hybrid_sort(input,0,len(input)-1))