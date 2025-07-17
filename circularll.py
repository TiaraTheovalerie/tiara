class Node:
    def __init__(self):
        self.data = input("Input data: ")
        self.next = None
        self.prev = None

class CirLinkedList:
    def __init__(self):
        self.head = None

    def append(self):
        new_node = Node()
        posisi = int(input("Input posisi " + str(new_node.data) + ": "))

        if posisi == 0:  # Insert di awal
            if self.head is None:
                self.head = new_node
                self.head.next = self.head  # Circular link ke dirinya sendiri
                self.head.prev = self.head  # Circular link ke dirinya sendiri
            else:
                ptr = self.head
                while ptr.next != self.head:  # Mencari node terakhir
                    ptr = ptr.next
                new_node.next = self.head  # Sambungkan node baru ke head
                ptr.next = new_node  # Update node terakhir agar menunjuk ke head
                self.head = new_node  # Update head

        elif posisi > 0:  # Insert di posisi tertentu
            if self.head is None:
                print("Circular Linked List kosong, tidak bisa insert di posisi tersebut.")
                return
            else:
                ptr = self.head
                index = 1  # Flag menuju posisi sebelum insert
                
                # Iterasi hingga mencapai posisi sebelum titik penyisipan
                while (ptr.next != self.head) and (index < posisi):
                    ptr = ptr.next
                    index += 1

                # Jika posisi valid, lakukan penyisipan
                if index == posisi:
                    new_node.next = ptr.next
                    ptr.next = new_node
                else:
                    print("Posisi melebihi panjang Circular Linked List.")
    
    def search(self):
        if self.head is None:
            print("Circular Linked List Kosong")
        else:
            cari = input("Input data yang ingin dicari: ")
            ptr = self.head
            index = 0
            while (ptr.next != self.head) and (ptr.data != cari):
                ptr = ptr.next
                index += 1
                if ptr.data == cari:
                    print(f"Data {cari} ditemukan di dalam circular linked list pada posisi {index}")
                else:
                    print(f"Data {cari} tidak ditemukan dalam circular linked list")
    
    def delete(self):
        if self.head is None:
            print("Circular Linked List kosong")
        else:
            posisi = int(input("Input posisi data yang ingin dihapus"))
            if posisi == 0:
                ptr = self.head
                if ptr.next == self.head:
                    self.head = None
                else:
                    while ptr.next != self.head:
                        ptr = ptr.next
                    self.head = self.head.next
                    ptr.next = self.head
            elif posisi != 0:
                ptr = self.head
                index = 1
                while (ptr.next != self.head) and (index != posisi):
                    ptr = ptr.next
                    index += 1
                if (index == posisi):
                    if (ptr.next.next == self.head):
                        ptr.next = self.head
                    else:
                        ptr.next = ptr.next.next
                else:
                    print("Posisi yang nirhiid")
        
    def count_node(self):
        if self.head is None:
            count = 0
        else:
            ptr = self.head
            count = 1
            while ptr.next is not self.head:
                count+=1
                ptr = ptr.next
            return count

    def display(self):
        if self.head is None:
            print("Circular Linked List kosong.")
        else:
            ptr = self.head
            while True:
                print(ptr.data, end=" -> ")
                ptr = ptr.next
                if ptr == self.head:
                    break
            print(f"({self.head.data})")  # Menandakan kembali ke head


# Testing
cll = CirLinkedList()
cll.append()
cll.append()
cll.append()
cll.display()
cll.search()
cll.delete()
cll.display()
cll.delete()
cll.display()
cll.delete()
cll.display()
# Output:
# Input data: 1
# Input posisi 1: 2
# Input data: 2
# Input posisi 2: 3
# Input data: 3
# 1 -> 2 -> 3 -> (1)