class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def remove(self, value):
        if not self.head:
            return
        
        current = self.head
        while True:
            if current.data == value:
                if current.next == current:
                    self.head = None
                    return
                
                current.prev.next = current.next
                current.next.prev = current.prev
                
                if current == self.head:
                    self.head = current.next
                return
            
            current = current.next
            if current == self.head:
                break

    def search(self, value):
        if not self.head:
            return None
        
        current = self.head
        while True:
            if current.data == value:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def display(self):
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print(f"({self.head.data})")

# Testing the implementation
dll = DoubleCircularLinkedList()
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.display()

dll.remove(20)
dll.display()

found = dll.search(30)
if found:
    print("Found:", found.data)
else:
    print("Not found")
