# görev 1
# görev 1: üç sayının toplamı veya çarpımı
# kullanıcıdan üç sayı girmesini iste 
try:
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    sayi3 = float(input("Üçüncü sayıyı girin: "))
    # kullanıcıdan seçim yapmasını iste
    secim = int(input("Toplam için '1', çarpım için '2' girin"))
    # seçime göre işlem yap
    if secim == 1:
        toplam = sayi1 + sayi2 + sayi3
        print(f"Üç sayının toplamı: {toplam}")
    elif secim == 2:
        carpim = sayi1 * sayi2 * sayi3
        print(f"Üç sayının çarpımı: {carpim}")
    else:
        print("Geçersiz seçim!")
except ValueError as ee:
    print(ee)
    
#Görev3: Metreyi mili inç veya yarda çevirme
metre = float(input("Metre cinsinden bir değer girin: "))
secim = input("Mil için 'M', inç için 'I', yarda için 'Y' girin").upper()

match secim:
    case "M":
        mil = metre * 0.000621371
        print(f"{metre} metre = {mil} mil")
    case "I":
        inc = metre * 39.3701
        print(f"{metre} metre = {inc} inç")
    case "Y":
        yarda = metre * 1.09361
        print(f"{metre} metre = {yarda} yarda")
    case _:
        print("Geçersiz seçim")
        