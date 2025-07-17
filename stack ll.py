class Node:
    def __init__(self, data):
        self.data = data # menyimpan data
        self.next = None # menunjuk ke node berikutnya

class LinkedList:
    def __init__(self):
        self.head = None # node paling atas dalam stack

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)

        # jika list tidak kosong
        if self.head:
            new_node.next = self.head
        self.head = new_node
        print(f"{data} telah ditambahkan ke stack")

    def topEl(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data

    def pop(self):
        if self.isEmpty():
            return None
        else:
            top_data = self.head.data
            self.head = self.head.next
            return top_data

    def clear(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        else:
            ptr = self.head
            while ptr:
                self.head = self.head.next
                ptr = ptr.next

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        else:
            print("Isi stack: ")
            ptr = self.head
            while ptr:
                print(ptr.data, end=" -> ")
                ptr = ptr.next
            print("None")

stack = LinkedList()

# menambahkan data
stack.push(1)
stack.push(2)
stack.push(3)

# menampilkan stack
stack.display()

# menghapus elemen
print("Elemen yang di-pop: ", stack.pop())
stack.display()

# melihat elemen teratas
print("Elemen teratas pada stack: ", stack.topEl())