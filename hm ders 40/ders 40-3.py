import random
import time
import re
def validate_tracking_number(tracking_number):
    """
    Takip numarasını doğrular format: en az 10 karakter, büyük harf ve rakam
    """
    if len(tracking_number) < 10:
        raise ValueError("takip numarası en az 10 karakter uzunluğunda olmalı")
    if not re.match(r'^[A-Z0-9]+$', tracking_number):
        raise ValueError("Takip numarası yalnızca büyük harf ve rakamdan oluşmalı")
def process_shipment(tracking_number):
    """
    kargo durumu adım adım takip eder her adımda hata olabilir
    """
    try:
        validate_tracking_number(tracking_number)
        #kargo durumları
        statuses = ["kayıt alındı", "hazırlanıyor", "dağıtıma çıktı", "teslim edildi", "tamamlandı"]
        max_attempts = 3
        for status in statuses:
            attempts = 0
            while attempts < max_attempts:
                try:
                    print(f"kargo durumu: {status}...")
                    time.sleep(1)
                    if random.random() < 0.2:
                        raise RuntimeError(f"{status} adımında bir hata oluştu")
                    #başarılı olursa dögüden çık 
                    print(f"durum başarıyla güncellendi: {status} \n")
                    break
                except RuntimeError as re:
                    attempts += 1
                    print(f"Hata: {re} | {max_attempts - attempts} deneme hakkı kaldı")
                    if attempts == max_attempts:
                        raise RuntimeError(f"{status} adımında işlem başarısız oldu. kargo takibi iptal")
        print("kargo takibi başarıyla tamamlandı \n aras kargo kardeş")
    except ValueError as ve:
        print(f"doğrulama hatası: {ve}")
    except RuntimeError as re:
        print(f"işlem  hatası: {re}")
    except Exception as e:
        print(f"bilinmeyen bir hata oluştu: {e}")
#kullanım
tracking_number = input("takip numarasını girin: ").strip()
process_shipment(tracking_number)
        