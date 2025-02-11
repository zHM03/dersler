from math_operation import add, subtract, sqrt, factorial
from random_generator import generate_random_number, shuffle_list

def main():
    try: 
        # toplama işlemler
        addNumber1 = float(input("Toplama işlemi yapmak istediğiniz ilk sayıyı giriniz: "))
        addNumber2 = float(input("Toplama işlemi yapmak istediğiniz ikinci sayıyı giriniz: "))
        print(f"sayıların toplamı:", add(addNumber1,addNumber2))       
        #çıkarma işlemleri
        subtractNumber3 = float(input("Çıkarma işlemi yapmak istediğiniz ilk sayıyı girin: "))
        subtractNumber4 = float(input("Çıkarma yapmak istediğiniz ikinci sayıyı girin: "))
        print(f"sayıların çıkarma sonucu:", subtract(subtractNumber3,subtractNumber4))
        #karekök hesaplama
        number = float(input("karekökünü almak istediğiniz sayıyı girin: "))
        print(f"{number} sayısının karekökü:", sqrt(number))
        #faktöryel hesaplama
        number = int(input("Faktöryelini hesaplamak istediğiniz sayıyı girin: "))
        print(f"{number} sayısının faktöryeli:", factorial(number))
        #rastgele sayı üretme
        start = int(input("Rastgele sayı için başlangıç değeri girin: "))
        end = int(input("Rastgele sayı için bitiş değeri girin: "))
        print(f"{start} ile {end} arasında rastgele bir sayı:",generate_random_number(start, end),)
        #liste karıştırma
        items = input("Virgülle ayrılmış bir liste girin (örnek: elma, armut, muz): ").split(",")
        print("Karıştırlmış liste:", shuffle_list(items))
        
    except ValueError as e:
        print("Hata:", e)
    except Exception as e:
        print("Beklenmeyen bir hata oluştu:", e)
if __name__ == "__main__":
    main()