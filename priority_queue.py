class Priority_Queue:
	def __init__(self):
		self.heap_size = 0
		self.seq = []
	def left(self,n):
		n+=1
		return 2*n
	def right(self,n):
		n+1
		return 2*n-1
	def parent(self,n):
		n+1
		return (n/2)-1
		
	def max_heapify(self, i): 
		l = self.left(i)
		r = self.right(i)
		largest=0
		if l<self.heap_size and self.seq[l]>self.seq[i]:
			largest=l
		else:
			largest=i
		if r<self.heap_size and self.seq[r]>self.seq[largest]:
			largest = r
		if largest != i:
			self.seq[i],self.seq[largest]=self.seq[largest],self.seq[i]
			self.max_heapify(largest)
		
	def heap_max(self):
		return self.seq[0]

	def heap_extract_max(self):
		#check if there is any more element to be extracted
		if self.heap_size < 1:
			return None
		max = self.seq[0]
		self.seq[0]=self.seq[-1]
		self.heap_size -= 1
		max_heapify(0)
		
	def heap_increase_key(self,i,key):
		if key < i:
			print("A very specific bad thing happened, key",key,"i",i)
		self.seq[i]=key
		print(i,self.seq,key)
		while i>0 and self.seq[self.parent(i)]<self.seq[i]:
			self.seq[self.parent(i)], self.seq[i] = self.seq[i], self.seq[self.parent(i)]
			i =  self.parent(i)

	def max_heap_insert(self,key):
		print(self.heap_size)
		if self.heap_size>1:
			print("max_heapify")
			self.max_heapify(0)
			print(self.seq)
		neg_inf = float("-inf")
		if len(self.seq) == self.heap_size:
			self.seq.append(neg_inf)
			self.heap_size+=1
		else:
			self.heap_size+=1
		self.seq[self.heap_size-1]= neg_inf
		self.heap_increase_key(self.heap_size-1,key)

pq = Priority_Queue()


pq.max_heap_insert(3)
print(pq.seq)
pq.max_heap_insert(4)
print(pq.seq)
pq.max_heap_insert(8)
pq.max_heap_insert(10)
pq.max_heap_insert(2)

print(pq.seq)

#can't creat a pq from zero. There are some errors.		
		
		
		
		
		
		
		
		
		
		
		
