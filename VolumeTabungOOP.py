class Tabung : 
  def __init__(self):
    self.jari = float(input("Masukkan Jari-jari : "))
    self.tinggi = float(input("Masukkan tinggi : "))
  
  def hitung_volume(self):
    return 3.14 * self.jari * self.jari * self.tinggi

tabung = Tabung()
print(f"Volume Tabung : {tabung.hitung_volume():.2f}")
