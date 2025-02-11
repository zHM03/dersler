import json
import logging
import sqlite3
from datetime import datetime
import os
from typing import Dict, List
from dataclasses import dataclass

# Log ayarları
logging.basicConfig(
    filename="kutuphane.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

@dataclass
class Kitap:
    isbn: str
    baslik: str
    yazar: str
    kopya_sayisi: int
    mevcut_kopya: int
    eklenme_tarihi: str
    
class Veritabani:
    def __init__(self):
        self.conn = sqlite3.connect("kutuphane.db")
        self.cursor = self.conn.cursor()
        self.tablolari_olustur()
        
    def tablolari_olustur(self):
        self.cursor.executescript(
        """
        CREATE TABLE IF NOT EXISTS kitaplar (
            isbn TEXT PRIMARY KEY,
            baslik TEXT NOT NULL,
            yazar TEXT NOT NULL,
            kopya_sayisi INTEGER,
            kategori TEXT,
            eklenme_tarihi TEXT
        );
        
        CREATE TABLE IF NOT EXISTS uyeler (
            uye_id INTEGER PRIMARY KEY AUTOINCREMENT,
            uye_adi TEXT NOT NULL UNIQUE,
            email TEXT,
            telefon TEXT,
            kayit_tarihi TEXT
        );
        
        CREATE TABLE IF NOT EXISTS odunc_kayitlari (
            kayit_id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT,
            uye_id INTEGER,
            odunc_tarihi TEXT,
            iade_tarihi TEXT,
            durum TEXT,
            FOREIGN KEY (isbn) REFERENCES kitaplar (isbn),
            FOREIGN KEY (uye_id) REFERENCES uyeler (uye_id)
        );
        """
        )
        self.conn.commit()

class GelismisKutuphane:
    def __init__(self):
        self.db = Veritabani()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Kütüphane sistemi başlatıldı")
        
    def kitap_ekle(
        self, isbn: str, baslik: str, yazar: str, kopya_sayisi: int = 1
    ) -> str:
        try:
            self.db.cursor.execute(
                """
                INSERT INTO kitaplar (isbn, baslik, yazar, kopya_sayisi, kategori, eklenme_tarihi)
                VALUES(?, ?, ?, ?, ?, ?)
                """,
                (
                    isbn,
                    baslik,
                    yazar,
                    kopya_sayisi,
                    "",  # Kategori boş olabilir
                    datetime.now().isoformat(),
                ),
            )
            self.db.conn.commit()
            self.logger.info(f"Yeni kitap eklendi: {baslik} (ISBN: {isbn})")
            return f"{baslik} kitabı başarıyla eklendi."
        except sqlite3.IntegrityError:
            self.logger.error(f"Kitap ekleme hatası: ISBN {isbn} zaten mevcut")
            return "Bu ISBN'de bir kitap mevcut."
        except Exception as e:
            self.logger.error(f"Kitap ekleme hatası: {str(e)}")
            return f"Kitap eklenirken bir hata oluştu: {str(e)}"
        
    def uye_ekle(self, uye_adi: str, email: str, telefon: str) -> str:
        try:
            self.db.cursor.execute(
                """
                INSERT INTO uyeler (uye_adi, email, telefon, kayit_tarihi)
                VALUES(?, ?, ?, ?)
                """,
                (uye_adi, email, telefon, datetime.now().isoformat()),
            )
            self.db.conn.commit()
            self.logger.info(f"Yeni üye eklendi: {uye_adi}")
            return f"{uye_adi} üye olarak eklendi."
        except sqlite3.IntegrityError:
            self.logger.error(f"Üye ekleme hatası: {uye_adi} zaten mevcut")
            return "Bu üye adı zaten kullanımda."
        except Exception as e:
            self.logger.error(f"Üye ekleme hatası: {str(e)}")
            return f"Üye eklenirken bir hata oluştu: {str(e)}"
        
    def kitap_odunc_al(self, isbn: str, uye_adi: str) -> str:
        try:
            self.db.cursor.execute(
                "SELECT uye_id FROM uyeler WHERE uye_adi = ?", (uye_adi,)
            )
            uye_result = self.db.cursor.fetchone()
            if not uye_result:
                return "Üye bulunamadı."
            uye_id = uye_result[0]

            self.db.cursor.execute(
                "SELECT kopya_sayisi, mevcut_kopya FROM kitaplar WHERE isbn = ?", (isbn,)
            )
            kitap_result = self.db.cursor.fetchone()
            if not kitap_result:
                self.logger.warning(f"Kitap bulunamadı: {isbn}")
                return "Kitap bulunamadı."
            kopya_sayisi, mevcut_kopya = kitap_result
            if mevcut_kopya <= 0:
                self.logger.warning(f"Kitap mevcut değil: {isbn}")
                return "Kitap mevcut değil."

            # Odunc kaydını ekleyelim
            self.db.cursor.execute(
                """
                INSERT INTO odunc_kayitlari (isbn, uye_id, odunc_tarihi, durum)
                VALUES (?, ?, ?, ?)
                """,
                (isbn, uye_id, datetime.now().isoformat(), "ödünç"),
            )

            # Kitap kopyalarını güncelle
            self.db.cursor.execute(
                """
                UPDATE kitaplar
                SET mevcut_kopya = mevcut_kopya - 1
                WHERE isbn = ? AND mevcut_kopya > 0
                """,
                (isbn,),
            )
            self.db.conn.commit()
            self.logger.info(f"Kitap ödünç alındı: {isbn} - Üye: {uye_adi}")
            return "Kitap başarıyla ödünç alındı."
        except Exception as e:
            self.logger.error(f"Kitap ödünç alma hatası: {str(e)}")
            return f"Kitap ödünç alınırken bir hata oluştu: {str(e)}"
        
    def istatistikler(self) -> Dict:
        try:
            self.db.cursor.execute("SELECT COUNT(*) FROM kitaplar")
            toplam_kitap = self.db.cursor.fetchone()[0]
            self.db.cursor.execute("SELECT COUNT(*) FROM uyeler")
            toplam_uye = self.db.cursor.fetchone()[0]
            self.db.cursor.execute(
                'SELECT COUNT(*) FROM odunc_kayitlari WHERE durum = "ödünç"'
            )
            odunc_kitap = self.db.cursor.fetchone()[0]
            self.db.cursor.execute("SELECT SUM(kopya_sayisi) FROM kitaplar")
            mevcut_kitap = self.db.cursor.fetchone()[0] or 0
            istatistik = {
                "toplam_kitap": toplam_kitap,
                "toplam_uye": toplam_uye,
                "odunc_kitap_sayisi": odunc_kitap,
                "mevcut_kitap_sayisi": mevcut_kitap,
            }
            self.logger.info("İstatistikler görüntülendi.")
            return istatistik
        except Exception as e:
            self.logger.error(f"İstatistik alma hatası: {str(e)}")
            return {}
        
    def __del__(self):
        try:
            self.db.conn.close()
            self.logger.info("Veritabanı bağlantısı kapatıldı.")
        except Exception as e:
            self.logger.error(f"Veritabanı kapatma hatası: {str(e)}")

def main():
    kutuphane = GelismisKutuphane()
    print(
        kutuphane.kitap_ekle(
            "978-0-7475-3269-9", "Harry Potter", "J.K. Rowling", kopya_sayisi=3
        )
    )
    print(kutuphane.uye_ekle("Fatih Şahinbaş", "fatih@example.com", "5432151245"))
    print(kutuphane.kitap_odunc_al("978-0-7475-3269-9", "Fatih Şahinbaş"))
    print(kutuphane.istatistikler())
    
if __name__ == "__main__":
    main()
