# kod 1
x = 10
if x > 15:
    print("x 15ten büyüktür")
elif x == 15:
    print("x 15'e eşittir")
else :
    print("x 15'ten küçüktür")
    
# kod 2
a = 5
b = 10
if a > 0 and b > 0:
    print("Her iki sayı da pozitif")
if a > 0 or b < 0:
    print("En az bir sayı pozitiftir")
if not a > 10:
    print("a 10'dan büyük değildir")
    
# kod 3
if True:
    print("deneme1")
    print("deneme2")
print("deneme 3")

# kod 4
x = 10
y = 20
if x > 5:
    if y > 15:
        print("x 5'ten büyük ve y 15'ten büyük")
    else:
        print("x 5'ten büyük ama y 15'ten küçük")
else:
    print("x 5'ten küçük")
    
# kod 5
try: 
    x = 10 / 0
except ZeroDivisionError:
    print("Sıfıra bölme hatası")
finally:
    print("Bu kod her zaman çalışır")
    
# kod 6
try:
    x= int("abc")
except ValueError:
    print("Geçersiz bir değer girdiniz")
    
# kod 7
try: 
    x = int(input("Bir sayı girin: "))
    y = 10 / x
except (ValueError, ZeroDivisionError):
    print("Geçersiz bir değer veya sıfıra bölme hatası")
    
# kod 8
# while döngüsü
i = 0 
while i > 5:
    print(i)
i += 1
# for dögüsü
for i in range (5):
    print(i+1)
    
# kod 9
for i in range(10):
    print(f"Iterasyon {i + 1}")
    
# kod 10 
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
        
# kod 11
for i in range(5):
    if i == 3:
        continue # 3ü atla
    print(i)
for i in range(5):
    if i == 3:
        break #dögüyü sonlandır
    print(i)
for i in range(5):
    print(i)
else:
    print("Döngü tamamlandı")
