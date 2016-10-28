#big O = NlogN
def find_max_crossing(seq, low, mid, high):
	sum_left = float("-inf")
	sum = 0
	cross_low = cross_high = 0
	for i in range(mid,low-1,-1):
		sum += seq[i]
		if sum > sum_left:
			cross_low = i
			sum_left = sum
	sum_right = float("-inf")
	sum = 0
	for i in range(mid+1,high+1):
		sum += seq[i]
		if sum > sum_right:
			cross_high = i
			sum_right = sum
	combined_sum = sum_left + sum_right
	return (cross_low,cross_high,combined_sum)
	
def find_max_subarray(seq,low,high):
	if low == high:
		#base case
		return (low, high, seq[low])
	else:
		#recursive case
		mid = (high+low)/2
		sum_list = []
		sum_list.append(find_max_subarray(seq,low,mid))
		sum_list.append(find_max_subarray(seq,mid+1,high))
		sum_list.append(find_max_crossing(seq, low, mid, high))
		sum_list = sorted(sum_list,key=lambda sum: sum[2])
		return sum_list.pop()
	
seq = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
mid = (len(seq)-1)/2
print(find_max_subarray(seq,0,len(seq)-1))
	