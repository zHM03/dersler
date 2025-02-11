#def toplam_hesapla(liste):
#     toplam = 0 
#     for sayi in liste:
#         if sayi == 0:
#             return "Sıfır tesiptlendi"
#         toplam += sayi
#     return toplam
# print(toplam_hesapla([1, 2, 3, 4]))
# print(toplam_hesapla([1, 2, 0, 4, 5]))

# def harf_say(dize):
#     sonuc = ""
#     sayac = 1
#     for i in range(len(dize)):
#         if i + 1 < len(dize) and dize [i] == dize[i + 1]:
#             sayac += 1
#         else:
#             sonuc += dize[i] + str(sayac)
#             sayac = 1
#     return sonuc
# print(harf_say("aabbc"))
# print(harf_say("aaabbbcc"))
# print(harf_say("ggtuyylkj"))

# def sayi_say(dize):
#     sonuc = ""
#     sayac = 1
#     for i in range(1,len(dize)):
#         if dize [i]== dize [i-1]:
#             sayac += 1
#         else:
#             if dize [i-1].isdigit():
#                 sonuc+=f"{sayac} tane {dize[i-1]} vardır \n"
#                 sayac=1
#     if dize[-1].isdigit():
#         sonuc+=f"{sayac} tane {dize[-1]} vardır \n amazing yazılmcı"
#     return sonuc
# print(sayi_say("55447711"))

def sayi_al():
    while True:
        try:
            sayi = int(input("Bir sayi gir bro: "))
            return sayi 
        except ValueError:
            print("Geçersiz giriş! lütfen bir sayi gir")
print("Girdiğiniz sayi:", sayi_al())