

class Node(object):
    def __init__(self, value):
        self.elem = value
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return 
        queue = []
        queue.append(self.root)


        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return 
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return 
            else:
                queue.append(cur_node.rchild)

    def pre_travel(self, node):
        if node is None:
            return 
        print(node.elem,end=" ")
        self.pre_travel(node.lchild)
        self.pre_travel(node.rchild)

    def mid_travel(self, node):
        if node is None:
            return 
        self.mid_travel(node.lchild)
        print(node.elem,end=" ")
        self.mid_travel(node.rchild)

    def post_travel(self, node):
        if node is None:
            return 
        self.post_travel(node.lchild)
        self.post_travel(node.rchild)
        print(node.elem,end=" ")

    def traverse(self, node):
        if node is None:
            return 
        queue = []
        queue.append(node)

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

            
if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.pre_travel(tree.root)
    print('\n')
    tree.mid_travel(tree.root)
    print('\n')
    tree.post_travel(tree.root)
    print('\n')
    tree.traverse(tree.root)


