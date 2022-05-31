from datetime import date
from tabnanny import verbose

class Vehicle:
    
    def __init__(self, plaka="None"):
        self.__plaka = plaka

        self.__aracModeli = input("Aracinizin modelini giriniz: ").strip().upper()
        while not(self.aracModeli.isalpha()):
            print("Arac modeli sadece alfabeden olusabilir!!")
            self.__aracModeli = input("Aracinizin modelini giriniz: ").strip().upper()
                 
        self.__fuelType = input("Benzin tipini giriniz: ").strip().upper()
        while not (self.fuelType.isalpha()):
            print("Benzin tipi sadece alfabeden olusabilir!!")
            self.__fuelType = input("Benzin tipini giriniz: ").strip().upper()
       
        self.__aracYasi = input("Arac yasini giriniz: ").strip().upper()
        while not (self.aracYasi.isnumeric()):
            print("Arac yasi sadece sayılardan olusabilir!!")
            self.__aracYasi = input("Arac yasini giriniz: ").strip().upper()

        self.__motorHacmi = input("Motor hacmini giriniz: ").strip().upper()
        while not (self.motorHacmi.isnumeric()):
            print("Motor hacmi sadece sayılardan olusabilir!!")
            self.__motorHacmi = input("Motor hacmini giriniz: ").strip().upper()

        
        self.__vergiUcreti = int(self.__aracYasi) * int(self.__motorHacmi)              

        self.tarih = input("Muayene tarihini Yil-Ay-Gun seklinde 1 bosluk birakarak giriniz : ").strip()
        while (len(self.tarih) != 10) or (self.whiteSpaceCount(self.tarih) != 2):
            print("Lutfen istenen formatta giris yapiniz!")
            self.tarih = input("Muayene tarihi giriniz: ").strip()
        yil, ay, gun = self.tarih.split()
        self.muayeneTarihi = date(int(yil), int(ay), int(gun))