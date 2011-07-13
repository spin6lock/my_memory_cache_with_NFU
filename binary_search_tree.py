#encoding=utf8

LEFT = 0
RIGHT = 1

class Node(object):
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.flag = None
		self.count = 0
		self.left = None
		self.right = None

	def __repr__(self):
		return "key:%s" %self.key

class BinarySearchTree(object):
	def __init__(self):
		self.root = None	

	def insert_node(self, key, value):
		node = Node(key, value)
		if self.root is None:
			self.root = node
			return
		insert_point = self.find_place(self.root, key)
		if insert_point is None:
			insert_point = node
		else:
			if key > insert_point.key:
				insert_point.right = node
			else:
				insert_point.left = node

	def remove_node(self, key):
		pass

	def find(self, key):
		pass

	def find_place(self, root, key):
		if root is None:
			return root
		else:
			if key > root.key:
				if root.right is None:
					return root
				else:
					return self.find_place(root.right, key)
			else:
				if root.left is None:
					return root
				else:
					return self.find_place(root.left, key)
			
	def print_tree(self):
		def print_node(node):
			if node is None:
				return
			print_node(node.left)
			print node.key
			print_node(node.right)
		print_node(self.root)
		

	def find_least_freq_used(self):
		pass
