import os
import shutil
import zipfile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Dosya yedekleme fonksiyonu
def backup_file(source_folder, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
        
    # Yedekleme için ZIP dosyası oluşturuluyor
    zip_name = os.path.join(backup_folder, "backup.zip")
    
    # ZIP dosyasına yazma işlemi
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as backup_zip:
        for foldername, subfolders, filenames in os.walk(source_folder):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                # Dosya yolunu dosya ismiyle ilişkilendir
                backup_zip.write(filepath, os.path.relpath(filepath, source_folder))
        print(f"{source_folder} başarıyla yedeklendi ve {zip_name} olarak saklandı")

# İzleyici sınıfı
class Watcher:
    script_dir = os.path.dirname(__file__)  # Çalışma dizini
    DIRECTORY_TO_WATCH = script_dir  # İzlenecek dizin
    
    def __init__(self):
        self.observer = Observer()  # Observer nesnesini oluşturuyoruz
    
    def run(self):
        event_handler = Handler()  # Handler sınıfı ile olayları işleme
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)  # Dizin takibini başlatıyoruz
        self.observer.start()  # İzlemeyi başlatıyoruz
        try:
            while True:
                pass
        except KeyboardInterrupt:  # Kullanıcı durdurma işlemi (Ctrl+C)
            self.observer.stop()
            print("Gözlemci durduruldu")
            self.observer.join()  # İzleyiciyi sonlandır

# Dosya sistemindeki değişiklikleri işleyen handler sınıfı
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            # Dosya değiştiğinde yedekleme işlemi
            print(f"Dosya değiştirildi: {event.src_path}")
            # Yedekleme işlemini çalıştır
            backup_file(os.path.dirname(event.src_path), "C:/Backup")  # Dosyanın bulunduğu dizini yedekle

# Ana çalışma bölümü
if __name__ == '__main__':
    watcher = Watcher()  # İzleyici nesnesini oluştur
    watcher.run()  # İzlemeyi başlat
