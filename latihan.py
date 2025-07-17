nama = (input("Masukkan nama karyawan: "))
jabatan = (input("Masukkan jabatan karyawan (manager/supervisor/staf): "))
pokok = float(input("Masukkan gaji pokok karyawan: "))

print("")

print("Informasi Gaji karyawan")
print("-----------------------")

if jabatan == "manager":
    tunjangan = pokok * 0.2
    total = pokok + tunjangan
    print("Nama\t    : ", nama)
    print("Jabatan\t    : ", jabatan)
    print("Gaji Pokok  : ", pokok)
    print("Tunjangan   : ", tunjangan)
    print("Total Gaji  : ", total)
elif jabatan == "supervisor":
    tunjangan = pokok * 0.15
    total = pokok + tunjangan
    print("Nama\t    : ", nama)
    print("Jabatan\t    : ", jabatan)
    print("Gaji Pokok  : ", pokok)
    print("Tunjangan   : ", tunjangan)
    print("Total Gaji  : ", total)
elif jabatan == "staf":
    tunjangan = pokok * 0.1
    total = pokok + tunjangan
    print("Nama\t    : ", nama)
    print("Jabatan\t    : ", jabatan)
    print("Gaji Pokok  : ", pokok)
    print("Tunjangan   : ", tunjangan)
    print("Total Gaji  : ", total)
else:
    print("tidak ada jabatan tersebut")


class Karyawan:
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan.lower()
        self.gaji = gaji

    def hitung_tunjangan(self):
        if self.jabatan == "manager":
            return 0.2 * self.gaji
        elif self.jabatan == "supervisor":
            return 0.15 * self.gaji
        elif self.jabatan == "staf":
            return 0.1 * self.gaji
        else:
            raise ValueError("Jabatan tidak valid")

    def hitung_total_gaji(self):
        return self.gaji + self.hitung_tunjangan()

    def tampilkan_gaji(self):
        tunjangan = self.hitung_tunjangan()
        total = self.hitung_total_gaji()
        print("Informasi Gaji karyawan")
        print("-----------------------")
        print("Nama\t    : ", self.nama)
        print("Jabatan\t    : ", self.jabatan)
        print("Gaji Pokok  : ", self.gaji)
        print("Tunjangan   : ", tunjangan)
        print("Total Gaji  : ", total)

def main():
    nama = input("Masukkan nama karyawan: ")
    jabatan = input("Masukkan jabatan karyawan (Manager/Supervisor/Staf): ").strip().lower()
    gaji = float(input("Masukkan gaji pokok: "))

    # Membuat objek karyawan
    karyawan = Karyawan(nama, jabatan, gaji)
    # Menampilkan hasil
    karyawan.tampilkan_gaji()

if __name__ == "__main__":
    main()
