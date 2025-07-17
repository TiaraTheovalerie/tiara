'''
Buat class playlist dengan atribut "nama" dan "songs" (sebuah array).
Definisikan method dalam class 'playlist' untuk menambahkan lagu ke dalam array 'song'
'''

class Playlist:
    def __init__(self):
        self.nama = input("Nama Playlist : ")
        self.song = []
    
    def addsong(self):
        n = int(input("Jumlah Lagu : "))
        for nama in range(n):
            nama = input("Judul Lagu : ")
            self.song.append(nama)
    
    def display(self):
        print("Playlist", self.nama)
        for i in range(len(self.song)):
            print(f'- {self.song[i]}')

pl = Playlist()
pl.addsong()
pl.display()
