class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

	def show(self):
		return self.items


q = Queue()
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
print(q.dequeue())
print(q.show())



