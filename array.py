
MAXSIZE = 40

class Array:
	def __init__(self):
		self.items = []
		self.length = MAXSIZE

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def insert(self, index, item):
		self.items.insert(index - 1, item)

	def remove(self, index):
		return self.items.remove(index - 1)

	def index(self, index):
		return self.items[index - 1]

	def search(self, item):
		for i in range(len(self.items)):
			if self.items[i] == item:
				return i + 1
		return None

	def show(self):
		return self.items

array = Array()
array.insert(1, 2)
print(array.show())
array.insert(1, 100)
print(array.show())
print(array.search(100))
print(array.index(1))






