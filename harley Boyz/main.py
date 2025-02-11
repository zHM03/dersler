import tkinter as tk
from PIL import Image, ImageTk
import clean
import power_options
import os
import sys

# Uygulama dizininin yolunu al
if hasattr(sys, '_MEIPASS'):
    base_dir = sys._MEIPASS  # PyInstaller ile oluşturulmuş .exe için geçici dizin
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Normal çalışma dizini

# Logo dosyasının tam yolunu oluştur
logo_path = os.path.join(base_dir, "assets", "logo.png")

# Ana pencereyi oluştur
window = tk.Tk()
window.title("Harley Boyz")
window.geometry("800x600")
window.configure(bg="#242424")
window.resizable(False, False)

# Menü çerçevesini oluştur
menu_frame = tk.Frame(window, bg="#242424", width=150)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)
menu_frame.pack_propagate(False)

# Dikey Tablo (Listbox)
info_listbox = tk.Listbox(
    menu_frame,
    font=("Calibri", 12),
    bg="#1f1e1e",
    fg="black",
    bd=2,
    highlightthickness=0,
    selectbackground="#1f1e1e",
    selectforeground="black"
)
info_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Etiketler
power_options_label = tk.Label(info_listbox, text="Power Options", font=("Calibri", 12), bg="#1f1e1e", fg="white")
power_options_label.pack(fill=tk.BOTH)

clean_label = tk.Label(info_listbox, text="Clean", font=("Calibri", 12), bg="#1f1e1e", fg="white")
clean_label.pack(fill=tk.BOTH)

# Mouse ile üzerindeyken rengi değiştiren fonksiyonlar
def on_enter(event):
    event.widget.config(bg="#333232")

def on_leave(event):
    event.widget.config(bg="#1f1e1e")

# Önceki bilgileri temizle ve yeni bilgileri göster
def display_info(label):
    print(f"Displaying info for: {label}")  # Hangi bölümün gösterileceğini kontrol et

    # Önceki etiketleri gizle
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label) and widget not in [logo_label]:
            widget.pack_forget()

    # Checkboxes frame'ini her seferinde gizle
    checkboxes_frame.pack_forget()

    # Checkbox içeriğini temizle
    for widget in checkboxes_frame.winfo_children():
        widget.pack_forget()  # Önceki bileşenleri gizle
    if label == 'clean':
        print("Showing clean options")
        clean.create_ui_elements(checkboxes_frame)
        checkboxes_frame.pack(pady=10)
    elif label == 'power_options':
        print("Showing power options")
        power_options.show_power_options(checkboxes_frame)
        checkboxes_frame.pack(pady=10)

# Tıklama olaylarını bağla
clean_label.bind("<Button-1>", lambda e: display_info('clean'))  # Clean butonuna tıklandığında temizle
power_options_label.bind("<Button-1>", lambda e: display_info('power_options'))  # Güç seçeneklerini göster

# Mouse olaylarını bağla
for label in [clean_label, power_options_label]:
    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)

# Resmi aç ve boyutlandır
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((300, 300), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Tkinter etiketi oluştur ve resmi göster
logo_label = tk.Label(window, image=logo_photo, bg="#242424")
logo_label.pack(pady=30)

# Logonun altında checkbox'lar ve buton için çerçeve oluştur
checkboxes_frame = tk.Frame(window, bg="#242424")

# UI bileşenlerini oluştur
temp_var, user_temp_var, prefetch_var = clean.create_ui_elements(checkboxes_frame)

# Seçenek çerçevesini başlangıçta gizli tut
checkboxes_frame.pack_forget()

# Tkinter uygulamasını başlat
if __name__ == "__main__":
    window.mainloop()