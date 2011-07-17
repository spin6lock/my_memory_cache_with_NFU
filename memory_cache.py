#-*- coding=utf-8 -*-
from binary_search_tree import BinarySearchTree
import random

class MemoryCache(object):
	def __init__(self, size=100, capacity=120):
		self.size = size
		self.capacity = capacity
		self.current_size = 0
		self.stats_init()
		self.tree = BinarySearchTree()

	def stats_init(self):
		self.hit = 0
		self.miss = 0

	def set(self, key, value):
		self.tree.insert_node(key, value)
		self.current_size += 1
		if self.current_size > self.capacity:
			self.shrink()

	def get(self, key):
		val = self.tree.find(key)
		if val:
			self.hit += 1
		else:
			self.miss += 1
			return None
		return val

	def stats(self):
		return "\nhit: %s\nmiss: %s\nhit_ratio: %s\n" %(self.hit, self.miss, \
			float(self.hit) / (self.miss+self.hit))

	def shrink(self):
		for i in range(1,self.current_size - self.size):
			result = self.tree.shrink()
			while not result:
				result = self.tree.shrink()

if __name__ == "__main__":
	mc = MemoryCache(90,95)
	mc.set(1, 1)
	print	mc.get(1)

	sequence = [i for i in range(1, 100)]
	random.shuffle(sequence)
	for i in range(len(sequence)):
		mc.set(sequence[i], sequence[i])
		for j in range(0, i):
			mc.get(i)
	print mc.tree.print_tree()
