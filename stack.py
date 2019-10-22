


class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def show(self):
		return self.items

if __name__ == "__main__":
	s = Stack()
	s.push(123456)
	s.push('fdslj')
	s.push('llx')
	print(s.peek())
	print("isEmpty:",s.isEmpty())
