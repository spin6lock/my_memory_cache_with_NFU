#-*- coding=utf-8 -*-
from linked_list import LinkedList, LinkedNode

class MemoryCache(object):
	def __init__(self, size=100, capacity=120):
		self.size = size
		self.capacity = capacity
		self.cache = {}
		self.linked_list = LinkedList()
		self.stats_init()

	def stats_init(self):
		self.hit = 0
		self.miss = 0

	def set(self, key, value):
		new_node = LinkedNode([key, 0])
		self.cache[key] = [value, new_node]
		self.linked_list.insert(self.linked_list.head, new_node)
		if len(self.cache) > self.capacity:
			self.shrink()

	def get(self, key):
		try:
			val, node = self.cache[key]
			node.payload[1] += 1
			self.hit += 1
		except KeyError:
			self.miss += 1
			return None
		if self.isHitFreqBigger(node, node.prev):
			self.linked_list.move_backward(node)
		return val

	def stats(self):
		return "\nhit: %s\nmiss: %s\nhit_ratio: %s\n" %(self.hit, self.miss, \
			float(self.hit) / (self.miss+self.hit))

	def isHitFreqBigger(self, a, b):
		if b is None or a is None or a.payload is None or b.payload is None:
			return False
		return a.payload[1] > b.payload[1]

	def shrink(self):
		while len(self.cache) > self.size:
			key, count = self.linked_list.head.next.payload
			print self.linked_list.head.next
			self.linked_list.delete(self.linked_list.head.next)
			self.cache.pop(key)

if __name__ == "__main__":
	mc = MemoryCache()
	mc.set(1, 2)
	print	mc.get(1)
