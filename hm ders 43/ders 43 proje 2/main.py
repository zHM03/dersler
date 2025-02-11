from my_package import divide, power, random_choice
def main():
    try: 
        #bölme işlemi
        a = float(input("Bölünen sayıyı girin: "))
        b = float(input("Bölen sayıyı girin: "))
        print(f"{a} / {b} =", divide(a, b))
        #üs alma işlemi
        a = float(input("Taban sayıyı girin: "))
        b = float(input("Üs sayıyı girin: "))
        print(f"{a} ^ {b} =", power(a, b))
        #Rastgele seçim
        items = input("Virgülle ayrılmış bir liste girin (örnek: elma, armut, muz): ").split(",")
        print("Rastgele Seçilen öğe:", random_choice(items))
    except ZeroDivisionError as e:
        print("Hata:", e)
    except ValueError as e:
        print("Hata:", e)
    except Exception as e:
        print("Beklenmeyen bir hata oluştu:", e)
    
if __name__ == "__main__":
    main()