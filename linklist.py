
class Node(object):
    def __init__(self, value, point=0):
        self.value = value
        self.next = point

class Linklist(object):
    def __init__(self):
        self.head = 0

    def initlist(self, value):
        self.head = Node(value[0])
        point = self.head
        for i in value[1:]:
            node = Node(i)
            point.next = node
            point = point.next

    def insert(self, index, data):
        point = self.head
        j = 1
        while j < index:
            point = point.next
            j = j + 1
        if j == index:
            node = Node(data)
            node.next = point.next
            point.next = node
            return 'successful'

    def delete(self, index):
        point = self.head
        j = 1
        while j < index:
            point = point.next
            j = j + 1
        if j == index:
            point.next = point.next.next
            return 'successful'

    def show(self):
        point = self.head
        while point != 0:
            if point.next != 0:
                print(point.value,end=',')
                point = point.next
            if point.next ==0:
                print(point.value,end=',')
                return 'successful'

if __name__ == "__main__":
    l = Linklist()
    # l.createlist(4)
    # print(l.show())
    print(l.head)
    l.initlist([6,2,3,4])
    print(l.head.value)
    print(l.show())
    l.insert(1,5)
    print(l.show())
    l.delete(3)
    print(l.show())            







