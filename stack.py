class stack:
	def __init__(self):
		self.store = list([])
	def stack_empty(self):
		return len(self.store)==0
	def push(self,elem):
		self.store.append(elem)
	def pop(self):
		if len(self.store)>0:
			return self.store.pop()
		
stack = stack()

print(stack.stack_empty())

stack.push(2)

stack.push(7)

stack.push(9)

print(stack.stack_empty())

print(stack.store)

stack.pop()

print(stack.store)
