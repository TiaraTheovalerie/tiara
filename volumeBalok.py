class Balok :
    def variabel(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

def main():
    panjang = int(input("Masukkan nilai panjang : "))
    lebar = int(input("Masukkan nilai lebar : "))
    tinggi = int(input("Masukkan nilai tinggi : "))

    balok = Balok(panjang, lebar, tinggi)

    volume = balok.hitung_volume()

    print("Volume balok adalah : ", volume)

main()