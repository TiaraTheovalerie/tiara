class Tabung:
  def __init__(self, jari=0,tinggi=0):
    self.__jari = jari
    self.__tinggi = tinggi
  
  def setJari(self,jari):
    self.__jari = jari
  
  def getJari(self):
    return self.__jari
  
  def setTinggi(self, tinggi):
    self.__tinggi = tinggi

  def getTinggi(self):
    return self.__tinggi
  
  def hitung_volume(self):
    return 3.14 * self.__jari * self.__jari * self.__tinggi
  
def main():
    tabung = Tabung()

    tabung.setJari(float(input("Masukkan Jari-jari : ")))
    tabung.setTinggi(float(input("Masukkan Tinggi : ")))
    print("Jari-jari : ", tabung.getJari())
    print("Tinggi : ", tabung.getTinggi())
    print(f"Volume Tabung :  {tabung.hitung_volume():.2f}")
    print("Volume Tabung : ", '{:0,.2f}'.format(tabung.hitung_volume()))

main()