#-*- coding=utf-8 -*-

class LinkedNode(object):
	def __init__(self, payload = None):
		self.prev = None
		self.next = None
		self.payload = payload

class LinkedList(object):
	def __init__(self):
		self.head = LinkedNode()

	def next(self, curr):
		return curr.next

	def insert(self, curr, new_node):
		temp = curr.next
		curr.next = new_node
		new_node.prev = curr
		new_node.next = temp
		if temp != None:
			temp.prev = new_node

	def delete(self, curr):
		if self.head == curr:
			self.head = None
			del curr
		temp = curr
		prev_node = curr.prev
		next_node = curr.next
		prev_node.next = next_node
		next_node.prev = prev_node
		del temp

	def move_forward(self, curr):
		if self.head == curr:
			return
		temp = curr.prev
		prev_node = temp.prev
		prev_node.next = curr
		curr.prev = prev_node
		next_node = curr.next
		next_node.prev = temp
		curr.next = temp
		temp.prev = curr
		temp.next = next_node

	def move_backward(self, curr):
		if curr.next == None:
			return
		next_node = curr.next
		prev_node = curr.prev
		prev_node.next = next_node
		next_node.prev = prev_node
		curr.next = next_node.next
		next_node.next = curr
		curr.prev = next_node
		if self.head == curr:
			self.head = prev_node

	def print_list(self):
		point = self.head
		while point.next is not None:
			point = point.next
			print point.payload

