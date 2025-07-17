class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            print(f"{new_node.data}: ditempatkan sebagai ROOT")
            return
        else:
            currentNode = self.root
            while True:
                if data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = new_node
                        new_node.parent = currentNode  # 👈 Tambahkan ini
                        print(f"{new_node.data}: ditempatkan sebagai LEFT {currentNode.data}")
                        return
                    currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = new_node
                        new_node.parent = currentNode  # 👈 Tambahkan ini
                        print(f"{new_node.data}: ditempatkan sebagai RIGHT {currentNode.data}")
                        return
                    currentNode = currentNode.right

    def inOrderTrav(self,trav):
        if trav is not None:
            # L
            self.inOrderTrav(trav.left)
            # V
            print(trav.data, end=" | ")
            # R
            self.inOrderTrav(trav.right)
    
    def rightMost(self,node):
        while node.right:
            node = node.right
        return node
    
    def leftMost(self, node):
        while node.left:
            node = node.left
        return node

    def deleteNode(self,travcell,hapus,deletecell):
        if deletecell == None:
            if travcell is not None:
                if travcell.data == hapus:
                    self.deleteNode(travcell,hapus,travcell)
                    return True
                if self.deleteNode(travcell.left, hapus, None):
                    return True
                if self.deleteNode(travcell.right,hapus,None):
                    return True
                else:
                    return False
            else:
                if deletecell.right == None:
                    if deletecell.parent == None:
                        self.root = deletecell.left
                    else:
                        if deletecell.parent.left == deletecell:
                            deletecell.parent.left = deletecell.parent
                        elif deletecell.parent.right == deletecell:
                            deletecell.left
                elif deletecell.left == None:
                    if deletecell.parent == None:
                        self.root = deletecell.right
                    else:
                        if deletecell.parent.left == deletecell:
                            deletecell.parent.left = deletecell.right
                        elif deletecell.parent.right == deletecell:
                            deletecell.right
                else:
                    if deletecell.parent.left == deletecell:
                        deletecell.parent.left = deletecell.left
                    else:
                        deletecell.parent.right = deletecell.left
                    
                    travcell = deletecell.left
                    travcell.parent = deletecell.parent

                    while travcell.right != None:  
                        travcell = travcell.right
                    travcell.right = deletecell.right
                    travcell.right.parent = travcell
    
    def deleteNode(self,travCell,hapus):
        if travCell is not None:
            if hapus < travCell.data:
                travCell.left = self.deleteNode(travCell.left, hapus)
            elif hapus > travCell.data:
                travCell.right = self.deleteNode(travCell.right,hapus)
            else:
                #penghapusan Node
                if travCell.left is None:
                    temp = travCell.right
                    travCell = None
                    return temp
                elif travCell.right is None:
                    temp = travCell.left
                    travCell = None
                    return temp
                
                temp = self.leftMost(travCell.right)
                #copy Node
                travCell.daata = temp.data
                travCell.right = self.deleteNode(travCell.right,temp.data)
        return travCell

btree = BinaryTree()
btree.insert(5)
btree.insert(2)
btree.insert(12)
btree.insert(-4)
btree.insert(3)
btree.insert(9)
btree.insert(21)
btree.insert(10)
btree.insert(25)
btree.insert(27)
btree.insert(32)
btree.insert(42)
btree.insert(18)
btree.insert(29)

print("In-order-Travesal:")
btree.inOrderTrav(btree.root)

btree.deleteNode(btree.root,2)

print("\nin-order-Travesal")
btree.inOrderTrav(btree.root)

print()
print("In-order Traversal before Delete:")
btree.inOrderTrav(btree.root)
print()
if btree.deleteNode(btree.root,25):
    print()
    print("In-order-Traversal After Delete:")
    btree.inOrderTrav(btree.root)
else:
    print("Node tidak ditmukan")
