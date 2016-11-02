class Node(object):
	def __init__(self, val= None, next = None, previous = None):
		self.val = val
		self.next = next
		self.pre = previous

class Linkedlist(object):
	def __init__(self, head,sentinal):
		self.head = head
		self.nil = sentinal

N1 = Node(1)
N2 = Node(4,N1)
N3 = Node(16,N2)
N4 = Node(9,N3)
N3.pre = N4
N2.pre = N3
N1.pre = N2
sentinal = Node(None,N4,N1)
N1.next = sentinal
l = Linkedlist(N4,sentinal)

def list_search(l, key):
	x = l.head
	while x != None and x.val != key:
		x = x.next
	if x.val == key:
		return x
	else:
		return None
def list_search_sentinal(l,key):
	x = l.nil.next
	while x != l.nil and x.val != key:
		x = x.next
	if x.val == key:
		return x
	else:
		return None	
			
def list_insert(l,x):
	x.next = l.head
	if l.head.pre != None:
		l.head.pre = x
	l.head = x

def list_insert_sentinal(l,x):
	x.next = l.nil.next
	x.next.pre = x
	l.nil.next = x
	x.pre = l.nil

def list_delete(l,x):
	#adjust its pre
	if x.pre != None:
		x.pre.next = x.next
	else:
		l.head = x.next
	print(l.head)
	#adjust its next
	if x.next != None:
		x.next.pre = x.pre

def list_delete_sentinal(l,x):
	#adjust its pre
	if x.pre != None:
		x.pre.next = x.next
	else:
		l.lil.next = x.next
	print(l.head)
	#adjust its next
	if x.next != None:
		x.next.pre = x.pre

def print_node(node):
	if node == None:
		print(None)
	else:
		print(node.val)

def print_linkedlist(l):
	x = l.nil.next
	output = []
	while x != l.nil:
		output.append(x.val)
		x = x.next
	print(output)

print_node(list_search(l,4))
print_node(list_search_sentinal(l,4))
list_insert_sentinal(l, Node(12))
print_linkedlist(l)
list_insert_sentinal(l,Node(45))
list_delete_sentinal(l,N3)
print_linkedlist(l)