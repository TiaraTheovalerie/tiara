class Pegawai:
    def __init__(self, nama, tgllahir, alamat, gaji):
        self._nama = nama
        self._tgllahir = tgllahir
        self._alamat = alamat
        self._gaji = gaji

    def setNama(self, nama):
        self._nama = nama
    
    def getNama(self):
        return self._nama
    
    def setTgllahir(self, tgllahir):
        self._tgllahir = tgllahir

    def getTgllahir(self):
        return self._tgllahir
    
    def setAlamat(self,alamat):
        self._alamat = alamat
    
    def getAlamat(self):
        return self._alamat
    
    def setGaji(self, gaji):
        self._gaji = gaji
    
    def getGaji(self):
        return self._gaji
    
    #method tunjangan
    def tunjangan(self):
        return self.getGaji() * 0.15

class PegawaiTetap(Pegawai):
    def __init__(self, nama, tgllahir, alamat, gaji):
        super().__init__(nama, tgllahir, alamat, gaji)
    
    def transport(self):
        return self.getGaji() * 0.05
    
    def totalGaji(self):
        return self.getGaji() + self.tunjangan() + self.transport()
    
#main program
nama = input("Masukkan nama : ")
tgllahir = input("Masukkan tanggal lahir : ")
alamat = input("Masukkan alamat : ")
gaji = int(input("Masukkan gaji : "))

#membuat objek pegawai tetap
objpegTetap = PegawaiTetap(nama, tgllahir, alamat, gaji)

#manampilkan hasil hitungan
print("=" * 35)
print("\t Data Pegawai")
print("=" * 35)
print("Nama \t\t : ", objpegTetap.getNama())
print("Tanggal Lahir \t : ", objpegTetap.getTgllahir())
print("Alamat \t\t : ", objpegTetap.getAlamat())
print("Gaji \t\t : ", objpegTetap.getGaji())
print("Tunjangan \t : ", objpegTetap.tunjangan())
print("Transport \t : ", objpegTetap.transport())
print("Total Gaji \t : ", objpegTetap.totalGaji())