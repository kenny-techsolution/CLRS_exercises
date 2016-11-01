def find_minmax_simul(seq):
	n= len(seq)
	min = float("inf")
	max = float("-inf")
	start_pos = 0
	if 0 != n%2:
		min = seq[0]
		max = seq[0]
		start_pos = 1
	for i in range(start_pos,n,2):
		current_min = seq[i+1]
		current_max = seq[i]
		if seq[i]<seq[i+1]:
			current_min = seq[i]
			current_max = seq[i+1]
		if max < current_max: max = current_max
		if min > current_min: min = current_min
			
	return (min, max)
	
input = [100,1,-34,2,6,2,4,68,2,8,92,57,25,71,0,34]

print(find_minmax_simul(input))
		
				