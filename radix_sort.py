import math
def radix_sort(seq,d):
	m , n = 10, 1
	sort_machine = [list([]) for p in range(11)]
	for i in range(d):
		#use a stable sort to sort Array seq on digit i
		for j in range(len(seq)):
			num = seq[j]%m
			num = num/n
			sort_machine[num].append(seq[j])
		seq_i = 0	
		for k in range(len(sort_machine)):
			for l in range(len(sort_machine[k])):
				seq[seq_i] = sort_machine[k].pop(0)
				seq_i+=1
		m*=10
		n*=10	
	return seq
	
input = [1,41,52,13,156,23,276,3,6,18,29,90,503,702,257] 
		
print(radix_sort(input,3))
			