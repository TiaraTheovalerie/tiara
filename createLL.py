class Node:
    def __init__(self):
        self.data = input("Data node: ")
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addFirst(self):
        simpul = Node()
        if self.isEmpty():
            self.head = simpul
        else:
            simpul.next = self.head
            self.head = simpul
    
    def addLast(self):
        simpul = Node()
        if self.isEmpty():
            self.head = simpul
        else:
            pointer = self.head
            while pointer.next :
                pointer = pointer.next
            pointer.next = simpul
    
    def removeFirst(self):
        if self.isEmpty():
            print ("Linked list is empty")
        elif self.head.next == None:
            print (f"Data {self.head.data} has been removed")
            self.head = None
        else:
            pointer = self.head
            self.head = self.head.next
            pointer.next = None
            print (f"Data {pointer.data} has been removed")


    def removeLast(self):
        if self.isEmpty():
            print ("Linked list is empty")
        elif self.head.next == None:
            print (f"Data {self.head.data} has been removed")
            self.head = None
        else:
            pointer = self.head
            while pointer.next.next:
                pointer = pointer.next
            print (f"Data {pointer.next.data} has been removed")
            pointer.next = None

    def addMid(self, index):
        pointer = self.head
        position = 0 
        if index == 0 :
            self.addFirst()
        else: 
            simpul = Node()        
            while pointer != None and position + 1 != index:
                pointer = pointer.next
                position += 1
            if pointer :
                if pointer.next:
                    simpul.next = pointer.next
                    pointer.next = simpul
                else:
                    pointer.next = simpul
            else: 
                print ("Data cannot be inserted")
                   
    def removeMid(self, index):
        pointer = self.head
        position = 0
        if index == 0:
            if pointer.next :
                self.head = pointer.next
            else:
                self.head = None
        else:
            while pointer != None and position + 1 != index:
                pointer = pointer.next
                position += 1
            if pointer:
                if pointer.next.next == None:
                    pointer.next = None
                else:
                    pointer.next = pointer.next.next
            else : 
                print ("Cannot remove, data isn't available")

    def display(self):
        if self.isEmpty():
            print ("Linked list is empty")
        else:
            pointer = self.head
            while True:
                print(pointer.data, end=" >> ")
                if pointer.next is None:
                    print ("None")
                    break
                else:
                    pointer = pointer.next

ll = linkedList()
ll.addMid(0)
ll.display()
print (f"Head : {ll.head.data}")
ll.addMid(1)
ll.display()
print (f"Head : {ll.head.data}")
ll.addMid(1)
ll.display()
print (f"Head : {ll.head.data}")
ll.addMid(3)
ll.display()
print (f"Head : {ll.head.data}")
ll.addMid(8)
ll.display()
print (f"Head : {ll.head.data}")