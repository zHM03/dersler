# Öğrenciler, Dersler ve Notlar listeleri
ogrenciler = []
dersler = []
notlar = {}

# 1. Öğrenci Ekleme
def ogrenci_ekle(ogrenciler, ad, soyad, sinif):
    """Yeni bir öğrenci ekler."""
    ogrenciler.append({"ad": ad, "soyad": soyad, "sinif": sinif})

# 2. Ders Ekleme
def ders_ekle(dersler, ders_adi, ogretmen):
    """Yeni bir ders ekler."""
    dersler.append({"ad": ders_adi, "ogretmen": ogretmen})

# 3. Not Ekleme
def not_ekle(notlar, ogrenci_ad, ders_ad, notu):
    """Öğrenciye ders ve not ekler."""
    if ogrenci_ad not in notlar:
        notlar[ogrenci_ad] = {}  # Öğrencinin notları için yeni bir sözlük başlat
    notlar[ogrenci_ad][ders_ad] = notu  # Öğrencinin dersine notu ekler

# 4. Öğrenci Raporlama
def ogrenci_raporla(notlar, ogrenci_ad):
    """Öğrencinin aldığı ders ve notları raporlar."""
    if ogrenci_ad in notlar:
        print(f"{ogrenci_ad} için notlar:")
        for ders, notu in notlar[ogrenci_ad].items():
            print(f"- {ders}: {notu}")
    else:
        print(f"{ogrenci_ad} için not bulunmamaktadır.")

# 5. Genel Ortalama Hesaplama
def genel_ortalama_hesapla(notlar):
    """Tüm öğrencilerin genel ortalamasını hesaplar."""
    toplam = 0
    sayac = 0
    for ogrenci, dersler in notlar.items():
        for notu in dersler.values():
            toplam += notu
            sayac += 1
    return toplam / sayac if sayac > 0 else 0  # Sayac 0'dan büyükse ortalama hesapla

# Örnek kullanım
ogrenci_ekle(ogrenciler, "Ali", "Yılmaz", "10/A")
ogrenci_ekle(ogrenciler, "Ayşe", "Kaya", "10/A")

ders_ekle(dersler, "Matematik", "Ahmet Hoca")
ders_ekle(dersler, "Fizik", "Mehmet Hoca")

not_ekle(notlar, "Ali Yılmaz", "Matematik", 85)
not_ekle(notlar, "Ali Yılmaz", "Fizik", 90)
not_ekle(notlar, "Ayşe Kaya", "Matematik", 92)
not_ekle(notlar, "Ayşe Kaya", "Fizik", 88)

# Öğrenci raporu yazdırma
ogrenci_raporla(notlar, "Ali Yılmaz")
ogrenci_raporla(notlar, "Ayşe Kaya")

# Genel not ortalamasını hesaplama
print(f"\nGenel Not Ortalaması: {genel_ortalama_hesapla(notlar):.2f}")
