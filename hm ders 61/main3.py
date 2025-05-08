import multiprocessing
import time

def kare_hesapla(sayilar, sonuc, baslangic, bitis):
    for i in range(baslangic, bitis):
        sonuc[i] = sayilar[i] ** 2

if __name__ == "__main__":
    sayilar = [i for i in range(100000)]
    sonuc = multiprocessing.Array('i', len(sayilar))  # Shared memory array for the results

    # Creating two processes with the correct ranges
    p1 = multiprocessing.Process(target=kare_hesapla, args=(sayilar, sonuc, 0, 50000))  # First process
    p2 = multiprocessing.Process(target=kare_hesapla, args=(sayilar, sonuc, 50000, 100000))  # Second process

    baslangic_zaman = time.time()
    
    p1.start()
    p2.start()

    p1.join()  # Wait for p1 to finish
    p2.join()  # Wait for p2 to finish

    print(f"Hesaplama {time.time() - baslangic_zaman:.2f} saniye sürdü")
    print("İlk 10 sonuç:", list(sonuc)[:10])  # Convert to list for better display
