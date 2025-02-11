import os
import shutil
import time
import matplotlib.pyplot as plt
import zipfile
import logging
import re
import streamlit as st
import pandas as pd
from cryptography.fernet import Fernet
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(
    filename="file_manager.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)

def generate_key():
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, "secret.key")
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
            
def load_key():
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, "secret.key")
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = fernet.encrypt(file.read())
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)
    logging.info(f"Şifreleme tamamlandı: {filename}")
    
def decrypt_file(encrypted_filename):
    key = load_key()
    fernet = Fernet(key)
    with open(encrypted_filename, "rb") as file:
        decrypted_data = fernet.decrypt(file.read())
    original_filename = encrypted_filename.replace(".enc", "")
    with open(original_filename, "wb") as file:
        file.write(decrypted_data)
    logging.info(f"şifre çözme tamamlandı: {encrypted_filename}")
    
def search_in_file(file_path, pattern):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    matches = re.findall(pattern, content)
    logging.info(f"arama yapıldı: {file_path} içinde {pattern}")
    return matches

def backup_files(source_folder, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
        zip_name= os.path.join(backup_folder, "backup.zip")
        with zipfile.ZipFile(zip_name, "w") as back_zip:
            for foldername, _, filenames in os.walk(source_folder):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    back_zip.write(filepath, os.path.relpath(filepath, source_folder))
        logging.info(f"yedekleme tamamlandı:{source_folder} -> {zip_name}")
        
def restore_backup(backup_folder, restore_path):
    zip_name = os.path.join(backup_folder, "backup.zip")
    with zipfile.ZipFile(zip_name, "r") as zip_ref:
        zip_ref.extractall(f"Geri yükleme tamamlandı: {backup_folder} -> {restore_path}")
        
st.title("dosya yönetim ve yedekleme sistemi")
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1)
if st.button("şifreleme anahtarın oluştur"):
    generate_key()
    st.success("şifreleme anahtarı oluşturuldu")
uploaded_file = st.file_uploader("bir dosya yükleyin")
if uploaded_file:
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.success(f"{uploaded_file.name} yüklendi")
        if st.button("dosya şifrele"):
            encrypt_file(file_path)
            st.success("dosya şifrelendi")
        if st.button("dosya şifre çöz"):
            decrypt_file(file_path + ".enc")
            st.success("dosyanın şifresi çözüldü")
pattern = st.text_input("aranacak kelime/regex pattern")
if st.button("dosyada ara"):
    if uploaded_file:
        results = search_in_file(file_path, pattern)
        st.write(f"bulunan eşleşmeler: {results}")
    else:
        st.warning("önce bir dosya yükleyin")
if st.button("dosyaları yedekle"):
    backup_files("uploads", "bakcup")
    st.success("yedekleme tamamlandı")
    restore_backup("backup", "restored")
    st.success("dosyaları geri yüklendi")
    
st.subheader("dosya işlemi istatistikleri")
data = {
    "işlem": ["şifreleme", "şifre çözme", "yedekleme", "geri yükleme"],
    "adet": [5, 3, 7, 2],
}
df = pd.DataFrame(data)
st.bar_chart(df.set_index("işlem"))