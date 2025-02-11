import os
import shutil

def dosya_kopyala(kaynak, hedef):
    try:
        shutil.copy(kaynak,hedef)
        print(f"{kaynak} dosyası {hedef} konumuna kopyalandı")
    except IOError as e:
        print(f"Hata: {e}")
        
def dosya_sil(dosya_adi):
    try:
        os.remove(dosya_adi)
        print(f"{dosya_adi} dosyası silindi")
    except IOError as e:
        print(f"Hata:{e}")
        
dosya_kopyala("kaynak.txt", "hedef.txt")
dosya_sil("silinecek.txt")