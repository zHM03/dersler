# Ürünler, Müşteriler ve Siparişler listeleri
urunler = []
musteriler = []
siparisler = []

# 1. Ürün Yönetimi
def urun_ekle(urunler, ad, fiyat, stok):
    """Yeni bir ürün ekler."""
    urunler.append({"ad": ad, "fiyat": fiyat, "stok": stok})

def urun_sil(urunler, ad):
    """Verilen adı eşleşen ürünü listeden siler."""
    urunler[:] = [urun for urun in urunler if urun["ad"].lower() != ad.lower()]

def stok_guncelle(urunler, ad, yeni_stok):
    """Ürünün stok miktarını günceller."""
    for urun in urunler:
        if urun["ad"].lower() == ad.lower():
            urun["stok"] = yeni_stok
            break

# 2. Müşteri Yönetimi
def musteri_ekle(musteriler, ad, soyad, email, telefon):
    """Yeni bir müşteri ekler."""
    musteriler.append({"ad": ad, "soyad": soyad, "email": email, "telefon": telefon})

# 3. Sipariş Yönetimi
def siparis_olustur(siparisler, urunler, musteri_email, siparis_detaylari):
    """Yeni bir sipariş oluşturur ve stokları günceller."""
    toplam_tutar = 0
    for siparis in siparis_detaylari:
        urun_ad = siparis["urun"]
        miktar = siparis["miktar"]
        urun = next((urun for urun in urunler if urun["ad"].lower() == urun_ad.lower()), None)
        if urun and urun["stok"] >= miktar:
            urun["stok"] -= miktar
            toplam_tutar += urun["fiyat"] * miktar
        else:
            print(f"Ürün stokta yok veya miktar yetersiz: {urun_ad}")
            return
    siparisler.append({"musteri": musteri_email, "detaylar": siparis_detaylari, "tutar": toplam_tutar})
    print(f"Sipariş başarıyla oluşturuldu! Toplam tutar: {toplam_tutar} TL")

# 4. Veri Analizi
def toplam_satis(siparisler):
    """Toplam satış tutarını hesaplar."""
    return sum(siparis["tutar"] for siparis in siparisler)

def en_cok_satan_urun(siparisler, urunler):
    """En çok satan ürünü bulur."""
    satislar = {}
    for siparis in siparisler:
        for detay in siparis["detaylar"]:
            urun_ad = detay["urun"]
            satislar[urun_ad] = satislar.get(urun_ad, 0) + detay["miktar"]
    # En çok satan ürünü döndürüyoruz
    return max(satislar, key=satislar.get) if satislar else None

# Örnek kullanım
# Ürün ekleme
urun_ekle(urunler, "Telefon", 8000, 10)
urun_ekle(urunler, "Bilgisayar", 15000, 5)
 
# Müşteri ekleme
musteri_ekle(musteriler, "Ali", "Yılmaz", "ali@example.com", "555-123-4567")

# Sipariş oluşturma
siparis_detay = [{"urun": "Telefon", "miktar": 2}]
siparis_olustur(siparisler, urunler, "ali@example.com", siparis_detay)

# Toplam satış ve en çok satan ürün
print(f"\nToplam satış tutarı: {toplam_satis(siparisler)} TL")
print(f"En çok satan ürün: {en_cok_satan_urun(siparisler, urunler)}")
