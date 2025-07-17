class Toko:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def hitung_total(self):
        return self.harga * self.jumlah

daftar_barang = []
    
n = int(input("Masukkan jumlah jenis barang: "))
for i in range(n):
    nama = input(f"Masukkan nama barang ke-{i+1}: ")
    harga = int(input(f"Masukkan harga per unit {nama}: "))
    jumlah = int(input(f"Masukkan jumlah {nama} yang dibeli: "))
    toko = Toko(nama, harga, jumlah)
    daftar_barang.append(toko)

total_semua = 0

for barang in daftar_barang:
    total = barang.hitung_total()
    total_semua += total

print(f"Total harga semua barang yang dibeli: {total}")