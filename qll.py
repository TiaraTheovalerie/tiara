class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedlistQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        print(f"{data} telah ditambahkan ke queue")

    def firstel(self):
        if self.isEmpty():
            return None
        return self.head.data

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            first_data = self.head.data
            ptr = self.head
            if (ptr.next is None) and (ptr.prev is None):
                # jika cuma 1 data dalam list
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return first_data

    def display(self):
        print(f"Isi Double Linked List saat ini: ", end = " ")
        if self.head:
            ptr = self.head
            while ptr:
                print(ptr.data, end=" ")
                ptr = ptr.next
                if (ptr!=None):
                    print("<->", end=" ")
                else:
                    print("-> None")
        else:
            print("Kosong")

queue = LinkedlistQueue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

queue.display()

print("Elemen paling depan:", queue.firstel())

print("Dequeue:", queue.dequeue())
queue.display()

print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
queue.display()