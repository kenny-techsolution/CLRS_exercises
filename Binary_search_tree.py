class Node:
	def __init__(self,key=None,left=None, right=None):
		self.key = key
		self.left = left
		self.right = right
class BST:
	def __init__(self, node=None):
		self.root = node		
	def insert(self,z):
		y = None
		x = self.root
		while x != None:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		#find the right parent
		z.parent = y
		
		#now handle the child
		if y == None:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z
	def delete(self,z):
		#3 cases
		#1. if z has no children. remove it , mod the parent to replace z to None.
		#2. if z has one child, then we elevate the child to take z pos.
		#3. if z has two children. find z's succossor, and let it take z's pos. 
		### implementation organized in the following 4 catagory
		#1. z has no left child. then replace z with right child. it has no right child. or it has right child. 
		#2. z has just left child. replace z with left child
		#3. z has two child. if y is z's right child. then replace z by y, leaving y's right child alone.
		#4. y lies within z's right subtree, but is not z's right child. replace y by its own right child. then replace z by y.
		print("z",z.key,z.right,z.left)
		if z.left == None:
			self.transplant(z,z.right)
		elif z.right == None:
			self.transplant(z,z.left)
		else:
			y = self.tree_minimum(z.right)
			if y.p != z:
				self.tranplant(y,y.right)
				y.right = z.right
				y.right.parent = y	
			self.transplant(z,y)
			y.left = z.left
			y.left.parent = y
			
	def transplant(self, u, v):
		#.if u is at the root
		if u.parent == None:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		# we allow v to be None
		if v != None:
			v.parent = u.parent
		
	def inorder_tree_walk(self,x):
		if x != None:
			self.inorder_tree_walk(x.left)
			print(x.key)
			self.inorder_tree_walk(x.right)

	def tree_search(self,x, k):
		if x !=None:
			if k == x.key:
				return x
			#if not matched, continue the search in the subtree
			if k<x.key:
				return self.tree_search(x.left,k)
			else:
				return self.tree_search(x.right,k)
		return None

	def iteractive_tree_search(self,x,k):
		while x!=None:
			if x.key == k:
				return x
			elif x.key > k:
				x = x.left
			else:
				x = x.right
		return None
	
	def tree_minimum(self,x):
		if x==None:
			return None
		while x.left!=None:
			x = x.left
		return x
	def tree_maximum(self,x):
		if x==None:
			return None
		while x.right!=None:
			x = x.right
		return x
	#if the right subtree of x is non empty, then the successor is the mininum of the right subtree.	
	def tree_successor(self,x):
		#case 1 has right subtree.
		if x.right != None:
			return tree_minimum(x)
		print("case 2")
		#case 2 has no right subtree.
		y = x.parent
		while y!= None and y.right == x:
			x = y
			y = x.parent
		return y
		
	def tree_predecessor(self,x):
		#case 1 has the left subtree
		if x.left != None:
			return tree_maximum(x)
		print("case 2")
		y = x.parent
		while y!= None and y.left == x:
			x = y
			y = x.parent
		return y
				
		
		
bst = BST()
bst.insert(Node(15))
bst.insert(Node(6))
bst.insert(Node(18))
bst.insert(Node(3))
n7 = Node(7)
bst.insert(Node(7))
n17 = Node(17)
bst.insert(n17)
bst.insert(Node(20))
bst.insert(Node(2))
bst.insert(Node(4))
n13 = Node(13)
bst.insert(n13)
bst.insert(Node(9))

bst.inorder_tree_walk(bst.root)
print(bst.tree_search(bst.root,2).key) 
print(bst.iteractive_tree_search(bst.root,2).key)
print(bst.tree_search(bst.root,10)) 
print("find minimum", bst.tree_minimum(bst.root).key)
print("find maximum", bst.tree_maximum(bst.root).key)
print("find successor", bst.tree_successor(n13).key)
print("find predecessor", bst.tree_predecessor(n17).key)
rn7 = bst.tree_search(bst.root, 7)
print("rn7",rn7.key,rn7.parent.key)
print("delete 7", bst.delete(rn7))
bst.inorder_tree_walk(bst.root)
