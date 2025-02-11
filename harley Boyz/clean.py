import os
import shutil
import tkinter as tk

# Dizini temizleme fonksiyonu
def clear_directory(path):
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"{file} dosyası silindi.")
                except PermissionError:
                    print(f"{file} dosyası silinemedi (erişim reddedildi, dosya açık).")
                except Exception as e:
                    print(f"{file} dosyası silinirken hata: {e}")

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path)
                    print(f"{dir} klasörü ve içindekiler silindi.")
                except Exception as e:
                    print(f"{dir} klasörü silinirken hata: {e}")

    except Exception as e:
        print(f"Hata: {e}")

# Temizleme işlemini seçili checkbox'lara göre yapma fonksiyonu
def clean_selected_directories(temp_var, user_temp_var, prefetch_var, status_label):
    # Temizleme işlemi kontrol
    cleaned = False
    
    if temp_var.get():
        clear_directory("C:\\Windows\\Temp")
        cleaned = True
    if user_temp_var.get():
        clear_directory(os.path.join(os.environ['USERPROFILE'], "AppData\\Local\\Temp"))
        cleaned = True
    if prefetch_var.get():
        clear_directory("C:\\Windows\\Prefetch")
        cleaned = True

    # Eğer en az bir dizin temizlendi ise "Clean Completed" mesajını göster
    if cleaned:
        status_label.config(text="Clean Completed", fg="green")
    else:
        status_label.config(text="No Directories Selected", fg="red")

# UI elemanlarını oluşturma fonksiyonu
def create_ui_elements(parent):
    # Önceki checkboxları temizle
    for widget in parent.winfo_children():
        widget.destroy()

    # Checkbox değişkenlerini oluştur
    temp_var = tk.BooleanVar()
    user_temp_var = tk.BooleanVar()
    prefetch_var = tk.BooleanVar()

    # Checkbox çerçevesini oluştur
    global checkboxes_frame
    checkboxes_frame = tk.Frame(parent, bg="#242424")

    # Checkbox'ları oluştur
    temp_checkbox = tk.Checkbutton(
        parent,
        text="Temp",
        variable=temp_var,
        bg="#242424",
        fg="white",
        font=("Calibri", 12),
        selectcolor="#944e2b",
        highlightthickness=0,
        bd=0,
        activebackground="#242424",
        highlightcolor="#242424"
    )

    user_temp_checkbox = tk.Checkbutton(
        parent,
        text="%Temp%",
        variable=user_temp_var,
        bg="#242424",
        fg="white",
        font=("Calibri", 12),
        selectcolor="#944e2b",
        highlightthickness=0,
        bd=0,
        activebackground="#242424",
        highlightcolor="#242424"
    )

    prefetch_checkbox = tk.Checkbutton(
        parent,
        text="Prefetch",
        variable=prefetch_var,
        bg="#242424",
        fg="white",
        font=("Calibri", 12),
        selectcolor="#944e2b",
        highlightthickness=0,
        bd=0,
        activebackground="#242424",
        highlightcolor="#242424"
    )
    
    # Checkbox'ları yerleştir
    temp_checkbox.grid(row=0, column=0, sticky='w', padx=50)
    user_temp_checkbox.grid(row=1, column=0, sticky='w', padx=50)
    prefetch_checkbox.grid(row=2, column=0, sticky='w', padx=50)

    # CLEAN butonunu ekleyelim
    clean_button = tk.Button(
        parent,
        text="CLEAN",
        command=lambda: clean_selected_directories(temp_var, user_temp_var, prefetch_var, status_label),
        bg="#944e2b",
        fg="white",
        font=("Calibri", 12),
        relief="flat",
        overrelief="raised",
        activebackground="#b55a38",
        activeforeground="white",
        width=20,
        height=2
    )
    clean_button.grid(row=3, column=0, pady=20, padx=10)

    # Status label'ı ekleyelim
    global status_label
    status_label = tk.Label(parent, text="", bg="#242424", fg="white", font=("Calibri", 12))
    status_label.grid(row=4, column=0, pady=10, padx=50)

    return temp_var, user_temp_var, prefetch_var