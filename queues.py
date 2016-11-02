#psuedo code -> http://clrs.skanev.com/10/01/04.html
class Queue:
	def __init__(self,n):
		self.size = n
		self.store = [None]*(n+1)
		self.head = 0
		self.tail = 1
		self.overflow = False
	def enqueue(self,elem):
		print("enqueue")
		if self.head == self.tail:
			print("queue overflow")
			return
		self.store[self.tail] = elem
		
		#key operation
		if self.head == 0:
			self.head = self.tail
		
		#print(self.tail,len(self.store))
		if self.tail == self.size:
			self.tail=1
		else:
			self.tail+=1
	def dequeue(self):
		print("dequeue")
		if self.head == 0:
			print("queue underflow")
			return
		x = self.store[self.head]
		if self.head == self.size:
			self.head = 1
		else:
			self.head+=1
			
		#key operation	
		if self.head == self.tail:
			self.head = 0
		return x
		
		
queue = Queue(3)
print(queue.store,queue.head,queue.tail)

queue.enqueue(3)
print(queue.store,queue.head,queue.tail)	

queue.enqueue(8)
print(queue.store,queue.head,queue.tail)

queue.enqueue(9)
print(queue.store,queue.head,queue.tail)

queue.enqueue(10)
print(queue.store,queue.head,queue.tail)

print(queue.dequeue())
print(queue.store,queue.head,queue.tail)

print(queue.dequeue())
print(queue.store,queue.head,queue.tail)

print(queue.dequeue())
print(queue.store,queue.head,queue.tail)

print(queue.dequeue())
print(queue.store,queue.head,queue.tail)

queue.enqueue(7)
print(queue.store,queue.head,queue.tail)

queue.enqueue(15)
print(queue.store,queue.head,queue.tail)