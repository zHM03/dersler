# class Araba:
#     def __init__(self, marka, model):
#         self.marka = marka
#         self.model = model
        
#     def bilgileri_goster(self):
#         print(f"Araba: {self.marka} {self.model}")
# arabam = Araba("Toyota", "Corolla")
# arabam.bilgileri_goster()

# class Hayvan:
#     def __init__(self, isim):
#         self.isim = isim
        
#     def ses_cikar(self):
#         pass
# class Kopek(Hayvan):
#     def ses_cikar(self):
#         print(f"{self.isim} hav hav!")
        
# class Kedi(Hayvan):
#     def ses_cikar(self):
#         print(f"{self.isim} miyav!")
        
# kopek = Kopek("Karabaş")
# kedi = Kedi("Biso")
# kopek.ses_cikar()
# kedi.ses_cikar()

# def toplama(a, b):
#     return a+b
# def cikarma(a, b):
#     return a - b
# print(toplama(5, 3))
# print(cikarma(5, 3))

# class Matematik:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
        
#     def toplama(self):
#         return self.a + self.b

#     def cikarma(self):
#         return self.a - self.b
    
# islem = Matematik(5,3)
# print(islem.toplama())
# print(islem.cikarma())

# class Arac:
#     def __init__(self, marka):
#         self.marka = marka
        
#     def bilgileri_goster(self):
#         print(f"Araç Modeli: {self.marka}")
        
# class Araba(Arac):
#     def __init__(self, marka, model):
#         super().__init__(marka)
#         self.model = model
        
#     def bilgileri_goster(self):
#         super().bilgileri_goster()
#         print(f"araba Modeli: {self.model}")
        
# arabam = Araba("Toyota", "Corolla")
# arabam.bilgileri_goster()

# class Kisi:
#     def __init__(self, isim, yas):
#         self.isim = isim
#         self.yas = yas
#     def bilgileri_goster(self):
#         print(f"isim: {self.isim}, yaş: {self.yas}")
        
# kisi1 = Kisi("Ahmet", 25)
# kisi1.bilgileri_goster()

# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack.pop())
# print(stack.pop())


# stack = []

# def push(val):
#     stack.append(val)

# def pop():
#     return

# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack.pop())
# print(stack.pop())


# class Stack:
#     def __init__(self):
#         self.stack = []
        
#     def push(self, val):
#         self.stack.append(val)
        
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             return "Stack boş"
        
#     def is_empty(self):
#         return len(self.stack) == 0
    
# s = Stack()
# s.push(1)    
# s.push(2)
# print(s.pop())
# print(s.pop())
# print(s.pop())

# class Kisi:
#     nufus = 0
    
#     def __init__(self,isim):
#         self.isim = isim
#         Kisi.nufus += 1

# kisi1 = Kisi("Ahmet")
# kisi2 = Kisi("Mehmet")
# print(Kisi.nufus)

# class Kisi:
#     def __init__(self, isim):
#         self.isim = isim
        
# kisi = Kisi("Ahmet")
# print (hasattr(kisi,"isim"))
# print(hasattr(kisi,"yas"))

class Kisi:
    def __init__(self, isim):
        self.isim = isim
        
kisi= Kisi("Ahmet")
print(kisi.__dict__)