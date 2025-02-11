def sepet_toplam_fiyat():
    urun_fiyatlari = []
    while True:
        giris = input("Ürün fiyatını girin (işlemi sonlandırmak için 'q' tuşuna bas): ")
        if giris.lower() == 'q':
            break
        try:
            fiyat = float(giris)
            if fiyat < 0:
                print("Hata negatif fiyat giremezsin. tekrar dene")
            else:
                urun_fiyatlari.append(fiyat)
        
        except ValueError:
            print("Hata geçersiz giriş! lütfen bir sayı gir")
        if not urun_fiyatlari:
            return "sepetiniz boş"
        toplam = sum(urun_fiyatlari)
        if len(urun_fiyatlari) > 5:
            toplam *= 0.9 #%10 indirim
        return round(toplam, 2)
print("toplam sepet fiyatı:", sepet_toplam_fiyat())