#encoding=utf8
from time import sleep

LEFT = "left"
RIGHT = "right"

class Node(object):
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.flag = None
		self.count = 0
		self.left = None
		self.right = None

	def __repr__(self):
		#return "key:%s, val:%s" %(self.key, self.value)
		#return str(vars(self)) + "\n"
		return "val:%s right:%s left:%s flag:%s" %(self.value, self.right.value if self.right else None, self.left.value if self.left else None, self.flag)

class BinarySearchTree(object):
	def __init__(self):
		self.root = None	

	def insert_node(self, key, value):
		node = Node(key, value)
		if self.root is None:
			self.root = node
			return
		insert_point = self.find_place(self.root, key, True)
		if insert_point is None:
			insert_point = node
		else:
			if key > insert_point.key:
				insert_point.right = node
				insert_point.flag = LEFT
			else:
				insert_point.left = node
				insert_point.flag = RIGHT

	def remove_node(self, key):
		pass

	def find(self, key):
		node = self.find_place(self.root, key, True)
		return node.value

	def find_place(self, root, key, change=None):
		if root is None:
			return root
		if key > root.key:
			root.flag = LEFT if change else root.flag
			if root.right is None:
				return root
			else:
				return self.find_place(root.right, key)
		else:
			root.flag = RIGHT if change else root.flag
			if root.left is None:
				return root
			else:
				return self.find_place(root.left, key)

	def shrink(self):
		return self.shrink_recursive(self.root)

	def shrink_recursive(self, root):
		def is_terminal_node(node):
			return node.left is None and node.right is None
		
		if root is None:
			return False
		if root.flag == LEFT:
			root.flag = RIGHT
			if root.left:
				if is_terminal_node(root.left):
					root.left = None
					return True
				else:
					return self.shrink_recursive(root.left)
		elif root.flag == RIGHT:
			root.flag = LEFT
			if root.right:
				if is_terminal_node(root.right):
					root.right = None
					return True
				else:
					return self.shrink_recursive(root.right)	
		return False
	
	def print_tree(self):
		def print_node(node, depth = 0):
			if node is None:
				return
			print_node(node.left, depth + 1)
			print "depth:", depth, node
			print_node(node.right, depth + 1)
		print_node(self.root)
		

	def find_least_freq_used(self):
		pass
