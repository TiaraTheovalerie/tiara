class Node:
    def __init__(self, data):
        self.data = data # menyimpan data pada node
        self.next = None # menunjuk ke node berikutnya pada level yang sama
        self.child = None # menunjuk ke LL di level bawah

class MultilevelLL:
    def __init__(self):
        self.head = None # head dari LL tingkat atas

    def append(self, data):
        # Menambahkan node baru di level atas (paling akhir)
        new_node = Node(data)
        if not self.head:         # Jika linked list kosong, set head ke node baru
            self.head = new_node
        else:
            temp = self.head
            while temp.next:      # Iterasi sampai node terakhir
                temp = temp.next
            temp.next = new_node  # Tambahkan node di akhir

    def add_child(self, parentdata, childdata):
        # Menambahkan child list ke node tertentu berdasarkan data parent
        temp = self.head
        while temp:
            if temp.data == parentdata:
                child_list = MultilevelLL()        # Buat linked list level anak
                for data in childdata:             # Tambahkan setiap data ke child list
                    child_list.append(data)
                temp.child = child_list.head       # Sambungkan ke child dari parent
                return
            else:
                temp = temp.next
        print(f"Parent node with data {parentdata} not found")  # Kalau parent tidak ditemukan

    def search(self, node, cari):
        # Mencari nilai dalam multilevel linked list (rekursif)
        if node is None:
            print("Multilevel tidak boleh kosong")
        else:
            while node:
                if node.data == cari:
                    return True
                if node.child:
                    if self.search(node.child, cari):  # Rekursif ke child jika ada
                        return True
                node = node.next
            return False

    def delete(self, node, hapus):
        # Menghapus node berdasarkan data yang dicari, dari semua level
        if self.head is None:
            print("Multilevel tidak boleh kosong")
            return
        if self.head.data == hapus:       # Kasus khusus: hapus head
            self.head = self.head.next
            return True
        else:
            prev = None
            while node:
                if node.data == hapus:
                    if prev:
                        prev.next = node.next  # Hapus node di tengah
                    return True
                if node.child:
                    if self.delete(node.child, hapus):  # Cek dan hapus di child
                        return True
                prev = node
                node = node.next
            return False

    def display(self, node, level=0):
        # Menampilkan multilevel linked list secara rekursif, dengan indentasi level
        if not self.head:
            print("Kosong")
            return
        else:
            while node:
                print("|"*level + str(node.data))  # Indentasi berdasarkan level
                if node.child:
                    self.display(node.child, level + 1)  # Tampilkan child dengan level++
                node = node.next

mll = MultilevelLL()

# menambahkan elemen di level atas
mll.append("A")
mll.append("B")
mll.append("C")

# menambahkan child nodes
mll.add_child("A", ["Ayam", "Anjing"])
mll.add_child("B", ["Babi", "Bison"])
mll.add_child("C", ["Caida", "Cadar"])

# menampilkan multilevel LL
print("Multilevel linked list")
mll.display(mll.head)
print()