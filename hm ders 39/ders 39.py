#görev 1 belirtilen aralıktaki sayıları gösterme
sayi1 = int(input("lütfen ilk sayıyı girin "))
sayi2 = int(input("lütfen ikinci aralıktaki sayıyı girin "))
#eğer sayi 1 sayi2 den büyükse aralığı ters çevir
if sayi1 > sayi2:
    sayi1, sayi2 = sayi2, sayi1
    #aralıktaki sayıları yazdır
    for sayi in range(sayi1, sayi2 + 1):
        print(sayi)
        
#görev 2 belirtilen aralıktaki tüm tek sayıları gösterme
sayi1 = int(input("lütfen ilk sayıyı girin "))
sayi2 = int(input("ikinci sayıyı gir "))
if sayi1 > sayi2:
    sayi1, sayi2, = sayi2, sayi1
    for sayi in range (sayi1 + 1, sayi2 + 1, 2):
        print(sayi)
        
#görev 3 belirtilen aralıktaki çift sayılar
sayi1 = int(input("lütfen ilk sayıyı girin "))
sayi2 = int(input("ikinci sayıyı gir "))
if sayi1 > sayi2:
    sayi1, sayi2, = sayi2, sayi1
    for sayi in range (sayi1, sayi2 +1):
        if sayi in range (sayi1, sayi2 + 1):
            if sayi % 2 == 0:
                print(sayi)
                
#görev 4 belirtilen aralıktaki tüm sayıları artan sırayla dizmek
sayi1 = int(input("lütfen ilk sayıyı girin "))
sayi2 = int(input("ikinci sayıyı gir "))
if sayi1 < sayi2:
    sayi1, sayi2, = sayi2, sayi1
    for sayi in range (sayi2, sayi1 + 1, + 1 ):
        print(sayi) 
        
#belirtilen aralıktaki tüm sayıları azalan sırayla dizmek
sayi1 = int(input("lütfen ilk sayıyı girin "))
sayi2 = int(input("ikinci sayıyı gir "))
if sayi1 < sayi2:
    sayi1, sayi2, = sayi2, sayi1
    for sayi in range (sayi1, sayi2 - 1, - 1 ):
        print(sayi) 
        
#görev 5 belirtilen sayiıların toplamı ve aritmetik ortalamasını hesaplamak
sayi1 = int(input("lütfen ilk sayıyı girin: "))
sayi2 = int(input("lütfen ikinci sayıyı girin: "))
if sayi1 > sayi2:
    sayi1, sayi2 = sayi2, sayi1
    #aralıktaki tüm sayıların toplamını topla
    toplam = 0
    sayac = 0
    for sayi in range(sayi1, sayi2 + 1):
        toplam += sayi
        sayac += 1
        # aritmetik ortalamayı hesapla
        if sayac > 0:
            ortalama = toplam / sayac
        else:
            ortalama = 0
            #sonuçları ekrana yazdır
            print(f"belirtilen aralıktaki sayıların toplamı: {toplam}")
            print(f"belirtilen aralıktaki sayıların aritmetik toplamı: {ortalama}")
            
#görev 6 çarpım tablosu gösterme
sayi1 = int(input("lütfen ilk sayıyı girin: "))
print(f"{sayi1} için çarpım tablosu:")
for i in range(1, 11):
    print(f"{sayi1} * {i} = {sayi}")