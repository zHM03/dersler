from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename,"rb") as file:
        file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)
        print(f"{filename} şifrelendi")
        
def decrypt_file(encrypted_filename):
    key = load_key()
    fernet = Fernet(key)
    with open(encrypted_filename, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        original_filename = encrypted_filename.replace(".enc", "")
    with open(original_filename, "wb") as file:
        file.write(decrypted_data)
        print(f"{encrypted_filename} çözüldü!")
        
generate_key()
encrypt_file("C:/Users/Nova 14/Desktop/SİLME!/hm ders 48 dosya okuma/proje2/text.txt")
decrypt_file("C:/Users/Nova 14/Desktop/SİLME!/hm ders 48 dosya okuma/proje2/text.txt.enc")