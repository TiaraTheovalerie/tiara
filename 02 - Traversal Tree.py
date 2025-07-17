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
    
    def preOrderTrav(self, trav):
        if trav is not None:
            # V
            print(trav.data, end=" | ") # Visit root first (pre-order)
            # L
            self.preOrderTrav(trav.left)
            # R
            self.preOrderTrav(trav.right)
    
    def postOrderTrav(self,trav):
        if trav is not None:
            # L
            self.postOrderTrav(trav.left)
            # R
            self.postOrderTrav(trav.right)
            # V
            print(trav.data, end=" | ") # Visit root last (post-order)
    
    def inOrderTrav(self,trav):
        if trav is not None:
            # L
            self.inOrderTrav(trav.left)
            # V
            print(trav.data, end=" | ")
            # R
            self.inOrderTrav(trav.right)
            
btree = BinaryTree()
btree.insert("T")
btree.insert("E")
btree.insert("Y")
btree.insert("A")
btree.insert("M")
btree.insert("U")
btree.insert("D")
btree.insert("I")
btree.insert("S")

# btree.insert(35)
# btree.insert(25)
# btree.insert(40)
# btree.insert(15)
# btree.insert(30)
# btree.insert(36)
# btree.insert(45)
# btree.insert(10)
# btree.insert(20)
# btree.insert(27)
# btree.insert(32)
# btree.insert(42)
# btree.insert(18)
# btree.insert(29)

print("Pre-order-Traversal:")
btree.preOrderTrav(btree.root)
print()
print("Post-order-Traversal:")
btree.postOrderTrav(btree.root)
print()
print("In-order-Traversal:")
btree.inOrderTrav(btree.root)

search = "s"
if btree.binarySearch(btree.root, search):
    print(f"Data {search} ditemukan.")
else:
    print(f"Data {search} tidak ditemukan")