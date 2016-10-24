def linear_search(seq, v):
	for i in range(len(seq)):
		if seq[i]== v:
			return i
	return None

input1 = list([4,1,3,6,3,7,8,9,10])
input2 = 6

print(linear_search(input1,input2))

#initialzation
#if seq[0]-seq[i-1] has been searched found no match and if seq[i] matches v, then the answer is found.

#maintenance

#termination
#if i is the last element and still not matches v, then we conclude that the array contains no such element as v.
 