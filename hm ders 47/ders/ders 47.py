#demetler

# 1.
# ogrenci = (12345, "Ayşe", "Yılmaz", "2000-05-15")
# print(ogrenci[1])
# print(ogrenci[1:3])
# no, ad , soyad, dogum = ogrenci
# print(no)
# print(ad)
# print(soyad)
# print(dogum)

# 2.
# python_kursu={"Ahmet", "Mehmet", "Ayşe"}
# java_kursu={"Mehmet", "Fatma", "Ali"}

# tum_ogrenciler = python_kursu.union(java_kursu)
# ortak_ogrenciler = python_kursu.intersection(java_kursu)
# sadece_python = python_kursu.difference(java_kursu)
# print(f"Ortak öğrenciler: {ortak_ogrenciler}")
# print(f"Tüm Öğrenciler: {tum_ogrenciler}")
# print(f"Python öğrenciler: {sadece_python}")

#3.
# meyveler = {"elma", "armut", "portakal"}
# meyveler.add("muz")
# print(meyveler)
# meyveler.remove("elma")
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# fark = A - B
# kesisim = A & B

#4.
# urun = {
#     "id":1001,
#     "ad":"laptop",
#     "fiyat": 15000,
#     "stok": 5,
#     "ozellikler": {"ram": "16GB", "islemci": "i7", "disk": "512GB SSD"},
# }
# print(urun["ad"])
# print(urun.get("renk", "Belirtilmemiş"))
# urun["fiyat"] = 16000
# urun.update({"stok": 4, "renk": "Gri"})

#5.
# ogrenci = {"ad": "Ahmet", "yas":21, "bolum":"Bilgisayar Mühendisliği"}
# print(ogrenci["ad"])
# ogrenci["okul"] = "Ankara Üniversitesi"

# print(ogrenci)
# ogrenci["yas"] = 22
# print("ad" in ogrenci)