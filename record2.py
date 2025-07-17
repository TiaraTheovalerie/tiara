'''
Buatkan tabel mahasiswa dalam 1 kelas (jumlah mahasiswa isi sendiri tapi harus lebih dari 1) mahasiswa memiliki nilai tugas, uts, dan
uas, dengan hitungan tugas 30%, uts 30%, dan uas 40%.
Buatkan tabel mahasiswa hasil akhir mahasiswa tersebut
'''

kelas = []
n = int(input("jumlah mahasiswa : "))

for i in range(n):
    mhs = {
        'nama' : (input("nama : ")),
        'nim' : (input("nim : ")),
        'tugas' : int(input("nilai tugas : ")),
        'uts' : int(input("nilai uts : ")),
        'uas' : int(input("nilai uas : "))
    }
    mhs['total'] = (mhs['tugas'] * 0.3) + (mhs['uts'] * 0.3) + (mhs["uas"] * 0.4)
    kelas.append(mhs)

print("=================================== KELAS ===================================")
print("NO", "NIM", "NAMA", "TUGAS", "UTS", "UAS", "TOTAL", sep="\t||\t", end="\n")

for i in range(len(kelas)):
    print(i+1, kelas[i]["nim"], kelas[i]["nama"], kelas[i]["tugas"], kelas[i]["uts"], kelas[i]["uas"], kelas[i]["total"], sep ="\t||\t", end="\n")