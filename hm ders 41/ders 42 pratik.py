stok = [
    {"urun": "Bilgisayar", "fiyat": 15000, "stok": 5},
    {"urun": "telefon", "fiyat": 8000, "stok":10},
    {"urun":"tablet", "fiyat": 5000, "stok":8,}
]

def stok_listele(stok):
    for urun in stok:
        print(f"{urun['urun']} - {urun['fiyat']} TL, stok: {urun['stok']}")

print("mevcut stok:")
stok_listele(stok)

def urun_ekle(stok, urun, fiyat, stok_miktar):
    stok.append({"urun": urun, "fiyat": fiyat, "stok": stok_miktar})
    
    urun_ekle(stok, "akıllı saat", 2000, 15)
    print("\nYeni ürün eklendi:")
    stok_listele(stok)
    
    def stok_sorgula(stok, min_stok):
        return[urun for num in stok if urun["stok"]>= min_stok]
    
    print("\nStok Miktarı 8'den fazla olan ürünler:")
    for urun in stok_sorgula(stok, 8):
        print(f"{urun['urun']} - stok: {urun['stok']}")
        
    def toplam_stok_degeri(stok):
        return sum(urun["fiyat"] * urun["stok"] for urun in stok)
        
print(f"\n toplam stok değeri: {toplam_stok_degeri(stok)} TL")






















































































