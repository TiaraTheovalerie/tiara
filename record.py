'''
Buatkan record mahasiswa yang terdiri dari nama, nim, dan ipk
'''

mahasiswa = {
    'nama' : 'Tiara',
    'nim' : '32240039',
    'ipk' : 4.00
}

print('nama : ', mahasiswa['nama'])

'''
Buatlah 5 nama mahasiswa yang ada dalam sebuah kels dan tampilkan hasilnya dalam bentuk list tabel
'''

print("input mahasiswa : ")
kelas = []
n = int(input("masukkan jumlah mahasiawa : "))

for i in range(n):
    mhs = {
        'nama' : (input("nama : ")),
        'nim' : (input("nim : ")),
        'ipk' : 4.00
    }
    kelas.append(mhs)

print("=============== KELAS ===============")
print("NO", "NIM", "NAMA", "IPK", sep="\t||\t", end="\n")

for i in range(len(kelas)):
    print(i+1, kelas[i]["nim"], kelas[i]["nama"], kelas[i]["ipk"], sep ="\t||\t", end="\n")