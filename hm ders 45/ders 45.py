# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

#      ---

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count = 1
        
counter = count_up_to(5)
for num in counter:
    print(num)

#      ---

# def fibonacci():
#     a, b = 0,1
#     while True:
#         yield a
#         a, b = b, a + b
        
# fib = fibonacci()
# for _ in range(10):
#     print(next(fib))

# ---

# def squares(n):
#     for i in range(n):
#         yield i ** 2
# for square in squares(5):
#     print(square)
    
# ---

# #liste ifadesi
# squares_list = [x ** 2 for x in range(5)]
# print(squares_list)
# #jeneratör ifadesi
# squares_gen = (x ** 2 for x in range(5))
# for square in squares_gen:
#     print(square)

# ---

# add = lambda x, y: x + y
# subtract = lambda x, y: x - y
# multiply = lambda x, y: x * y
# divide = lambda x, y : x / y
# print(add(2, 3))
# print(subtract(2, 3))
# print(multiply(2, 3))
# print(divide(2, 3))

# ---

# numbers = [1, 2, 3, 4]
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)

# ---

# numbers = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)

# ---

# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return

# closure = outer_function(10)
# print(closure(5))

#pratik

# def randevu_ayarla(acilis_saati):
#     def randevu(musteri_ad, hizmet):
#         print(f"{musteri_ad}, {acilis_saati} saatinde '{hizmet}' hizmeti alacak.")
        
#     return randevu
# açılış_09_00 = randevu_ayarla("09.00")

# açılış_09_00("Ali", "Saç kesimi")
# açılış_09_00("Ayşe", "Saç boyaması")

# ---

