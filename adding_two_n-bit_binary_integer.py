def add_binary_int(int1, int2):
	res = [0]*(len(int1)+1)
	for i in range(len(int1)-1,-1,-1):
		print(i,int1[i])
		sum = int1[i]+int2[i]+res[i]
		print(sum)
		if sum >= 2:
			res[i] = 1
			res[i+1] += sum-2
		else:
			res[i+1] += sum
		print(res)
	return res
	
int1 = [1,0,0,1]
int2 = [1,1,0,1]

print(add_binary_int(int1,int2))