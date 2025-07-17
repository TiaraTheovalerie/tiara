class Node:
    def __init__(self, data):
        self.data   = data
        self.left   = None  # Left child node
        self.right  = None  # Right child node

class BinaryTree:
    def __init__(self):
        self.root = None  # Root node of the tree

    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            print(f"{new_node.data}: ditempatkan sebagai ROOT")
            return
        else:
            currentNode = self.root
            while True:
                # Left-to-Right
                if data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = new_node
                        print(f"{new_node.data}: ditempatkan sebagai LEFT {currentNode.data}")
                        return
                    currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = new_node
                        print(f"{new_node.data}: ditempatkan sebagai RIGHT {currentNode.data}")
                        return
                    currentNode = currentNode.right
                    
btree = BinaryTree()

btree.insert(50)
btree.insert(30)
btree.insert(20)
btree.insert(40)
btree.insert(70)
btree.insert(60)
btree.insert(80)

# btree.insert("T")
# btree.insert("E")
# btree.insert("Y")
# btree.insert("A")
# btree.insert("M")
# btree.insert("U")
# btree.insert("D")
# btree.insert("I")
# btree.insert("S")