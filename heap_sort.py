class Heap:
	def __init__(self, seq):
		self.heap_size = len(seq)
	def left(self,n):
		n+=1
		return 2*n-1

	def right(self,n):
		n+=1
		return 2*n+1-1

	def parent(self,n):
		n+=1
		return (n/2)-1

	def heap_size(self,seq):
		return 0

	def max_heapify(self,seq,i):
		l = self.left(i)
		r = self.right(i)
		largest = 0
		if l<self.heap_size and seq[l]>seq[i]:
			largest = l
		else:
			largest = i
		if r<self.heap_size and seq[r]>seq[largest]:
			largest = r
		if largest != i:
			seq[i],seq[largest]=seq[largest],seq[i]
			self.max_heapify(seq,largest)
		#return seq
	
	def build_maxheap(self,seq):
		self.heap_size = len(seq)
		for i in range((len(seq)-1)/2,-1,-1):
			self.max_heapify(seq,i)
		#return seq

	def heap_sort(self,seq):
		self.build_maxheap(seq)
		#i will stop at index 1. 
		#because [2,1,3] will be come [1,2,3]. when i is 1
		for i in range(len(seq)-1,0,-1):
			#print(i,seq[i])
			seq[0],seq[i] = seq[i],seq[0]
			self.heap_size -= 1
			#print("before",seq)
			self.max_heapify(seq,0)
			#print("after",seq)
		return seq
		
	def heap_max(self,seq):
		return seq[-1]
		
		
input = [4,1,3,2,16,9,10,14,8,7]
input2 = [16,4,10,14,7,9,3,2,8,1]
heap = Heap(input2)
#print(heap.build_maxheap(input))
print(heap.heap_sort(input2))
print(heap.heap_max(input2))




	
		
	