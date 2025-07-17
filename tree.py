class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = input("Masukkan data: ")


class Tree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def create_root(self):
        simpul = Node(1)
        self.root = simpul

    def insert(self):
        if self.is_empty():
            return self.create_root()
        else:
            ptr = self.root
            simpul = Node(1)
            while True:
                if simpul.data < ptr.data:
                    if ptr.left is not None:
                        ptr = ptr.left
                    else:
                        ptr.left = simpul
                        break
                # kanan
                else:
                    if ptr.right is not None:
                        ptr = ptr.right
                    else:
                        ptr.right = simpul
                        break
    
    

    def display(self, ptr, level=0):
        if ptr:
            print(f"Node: {ptr.data}, Level: {level}")
            self.display(ptr.left, level + 1)
            self.display(ptr.right, level + 1)


tr = Tree()
for i in range(5):
    tr.insert()
tr.display(tr.root)