# import os
# try:
#     script_dir = os.path.dirname(__file__)
#     abs_file_path = os.path.join(script_dir, "ornek.txt")
#     dosya = open(abs_file_path, "r", encoding="utf-8")
#     icerik = dosya.read()
#     print(icerik)
#     dosya.close()
# except FileNotFoundError:
#     print("Dosya bulunamadı!")

# import os
# try:
#     script_dir = os.path.dirname(__file__)
#     abs_file_path = os.path.join(script_dir, "ornek.txt")
#     dosya = open(abs_file_path, "w", encoding="utf-8")
#     dosya.write("selamün aleyküm")
#     dosya.close()
# except FileNotFoundError:
#     print("Dosya bulunamadı!")
    
# import os
# try:
#     script_dir = os.path.dirname(__file__)
#     abs_file_path = os.path.join(script_dir, "ornek.txt")
#     dosya = open(abs_file_path, "w+", encoding="utf-8")
#     dosya.write("selamün aleyküm")
#     dosya.seek(0)
#     data = dosya.read()
#     print(data)
#     dosya.close()
# except FileNotFoundError:
#     print("Dosya bulunamadı!")

# import os
# try:
#     script_dir = os.path.dirname(__file__)
#     abs_file_path = os.path.join(script_dir, "photo.jpg")
#     dosya = open(abs_file_path, "rb")
#     print("dosya başarıyla eklendi")
# except IOError:
#     print("hata oluştu")

# import errno
# try:
#     dosya = open("ornek.txt", "r")
# except IOError as e:
#     if e.errno == errno.ENOENT:
#         print("dosya bulunmadı")

# import os
# script_dir = os.path.dirname(__file__)
# abs_file_path = os.path.join(script_dir, "ornek.txt")
# dosya = open (abs_file_path, "r", encoding="utf-8")
# for satir in dosya:
#     print(satir, end = "")
# dosya.close()

#bin dosyaysı oluşturma ve yazma

# import os
# script_dir = os.path.dirname(__file__)
# abs_file_path = os.path.join(script_dir, "file.bin")
# dosya = open(abs_file_path,"wb")
# try: 
#     dosya.write(b'\x00\x01\x02\x03\x04\x05')
# finally:
#     dosya.close()
    
# #bin dosyası okuma

# script_dir = os.path.dirname(__file__)
# abs_file_path = os.path.join(script_dir, "file.bin")

# with open(abs_file_path, "rb") as dosya:
#     binary_data = dosya.read()
# print(binary_data)

import os
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, "ornek.txt")
abs_file_path2 = os.path.join(script_dir, "ornek2.txt")

kaynak = open(abs_file_path, "rb")
hedef = open(abs_file_path2, "w+b")
hedef.write(kaynak.read())
kaynak.close()
hedef.close()