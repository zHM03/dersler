from multiprocessing import Pool
import time

def kare(x):
    return x * x

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        baslangic = time.time()
        sonuclar = pool.map(kare, range(1000000))
        print(f"hesaplama {time.time() - baslangic: .2f} saniye sürdü")
        print(f"ilk 10 sonuc:", sonuclar[:10])