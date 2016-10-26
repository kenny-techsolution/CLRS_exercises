#Interesting property
#1. each iteration, the largest num will be bubble up to the most right.
#2. if the iteration has no swap, then no need to iterate again. 
#3. the worst case of number of iterations is n-1
# proof:  
#	[2,1]=>1
#	[3,2,1] => 2
def bubble_sort(seq):
	swapped = False
	for j in range(len(seq),-1,-1):
		print(seq,j)
		for i in range(j-1):
			swapped = False
			if seq[i]>seq[i+1]:
				swapped = True
				temp = seq[i+1]
				seq[i+1] = seq[i]
				seq[i] = temp
		if swapped == False:
			break

input = list([43,34,11,6,3,7,8,9,10,34,51,2,36,91,20])
print(bubble_sort(input))