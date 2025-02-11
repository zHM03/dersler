import math
def add(a, b):
    """iki sayi toplar"""
    return a + b
def subtract(a, b):
    """iki sayiyi çıkar"""
    return a - b
def sqrt(a):
    """bir sayının karekökünü toplar"""
    if a < 0:
        raise ValueError("Negatif sayıların karekökü alınamaz")
    return math.sqrt(a)
def factorial(a):
    """bir sayının faktöriyelini hesaplar"""
    if a < 0:
        raise ValueError("value sayıların faktöryeli hesaplanamaz")
    return math.factorial(a)
def ucgenAlanHesapla(a, b, c):
    cevre = (a+b+c) / 2
    return math.sqrt(cevre * (cevre-a) * (cevre - b) * (cevre -c))