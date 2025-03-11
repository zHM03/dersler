# 1
# class Araba:
#     def __init__(self, marka, model):
#         self.marka = marka
#         self.model = model
    
#     def bilgileri_goster(self):
#         print(f"Araba: {self.marka} {self.model}")
        
# araba1 = Araba("Toyota", "Corolla")
# araba1.bilgileri_goster()

# 2

# class BankaHesabi:
#     def __init__(self, isim, bakiye):
#         self.isim = isim
#         self.__bakiye = bakiye
        
#     def bakiye_goster(self):
#         return self.__bakiye
    
#     def para_yatir(self, miktar):
#         if miktar > 0:
#             self.__bakiye += miktar
            
#     def para_cek(self,miktar):
#         if 0 < miktar <= self.__bakiye:
#             self.__bakiye -= miktar
            
# hesap = BankaHesabi("Ahmet", 1000)
# print(hesap.bakiye_goster())
# hesap.para_yatir(500)
# print(hesap.bakiye_goster())
# hesap.para_cek(200)
# print(hesap.bakiye_goster())

# 3

# 1
# from abc import ABC, abstractmethod

# class Sekil(ABC):
#     @abstractmethod
#     def alan(self):
#         pass

# class Dikdortgen(Sekil):
#     def __init__(self, uzunluk, genislik):
#         self.uzunluk = uzunluk
#         self.genislik = genislik
        
#     def alan(self):
#         return self.uzunluk * self.genislik
    
# dikdortgen = Dikdortgen(5, 10)
# print(dikdortgen.alan())

# 2

# class Arac:
#     def calistir(self):
#         print("Araç çalıştır")
        
# class Otomobil(Arac):
#     def calistir(self):
#         print("Otomobil çalıştır")
        
# otomobil = Otomobil()
# otomobil.calistir()

# 3

