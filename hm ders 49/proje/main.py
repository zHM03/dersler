import streamlit as st
import sqlite3
import pandas as pd
import os
from datetime import datetime
from cryptography.fernet import Fernet
import matplotlib.pyplot as plt

# Veritabanı bağlantısı ve tablo oluşturma
conn = sqlite3.connect("course_registration.db")
cursor = conn.cursor()

# Kullanıcı tablosu
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    role TEXT
    )"""
)

# Öğrenci tablosu
cursor.execute(
    """CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        course TEXT,
        registration_date TEXT
        )"""
)

# Devam tablosu
cursor.execute(
    """CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course TEXT,
        date TEXT,
        status TEXT,
        FOREIGN KEY(student_id) REFERENCES students(id)
        )"""
)
conn.commit()

# Şifreleme fonksiyonları
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
    return open(abs_file_path, "rb").read()

def encrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(data.encode()).decode()

# Kullanıcı girişi
st.sidebar.subheader("Kullanıcı Girişi")
username = st.sidebar.text_input("Kullanıcı Adı")
password = st.sidebar.text_input("Şifre", type="password")
role = None

if st.sidebar.button("Giriş Yap"):
    user = cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?", (username, password)
    ).fetchone()
    if user:
        role = user[3]
        st.sidebar.success(f"Hoşgeldiniz {username} ({role})")
    else:
        st.sidebar.error("Hatalı kullanıcı adı veya şifre")

# Menü Seçimi
menu = [
    "Öğrenci Kaydı",
    "Kayıtlı Öğrenci",
    "Kayıt Düzenleme",
    "Kayıt Sil",
    "Kayıt Arama",
    "E-posta Gönder",
    "Ders Devam Takibi",
    "İstatistikler",
]
choice = st.sidebar.selectbox("Menü", menu)

# Öğrenci Kaydı
if choice == "Öğrenci Kaydı":
    st.subheader("Yeni Öğrenci Kaydı")
    name = st.text_input("Ad Soyad")
    email = st.text_input("E-posta")
    phone = st.text_input("Telefon")
    course = st.selectbox(
        "Kurs Seçin", ["Python", "Web Geliştirme", "Veri Bilimi", "Siber Güvenlik"]
    )

    if st.button("Kaydı Tamamla"):
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO students (name, email, phone, course, registration_date) VALUES (?, ?, ?, ?, ?)",
            (
                encrypt_data(name),
                encrypt_data(email),
                encrypt_data(phone),
                course,
                registration_date,
            ),
        )
        conn.commit()
        st.success(f"{name} başarıyla kayıt edildi")

# Kayıtlı Öğrenciler
elif choice == "Kayıtlı Öğrenciler":
    st.subheader("Kayıtlı Öğrenciler Listesi")
    students = pd.read_sql_query("SELECT * FROM students", conn)
    if not students.empty:
        students["name"] = students["name"].apply(decrypt_data)
        students["email"] = students["email"].apply(decrypt_data)
        students["phone"] = students["phone"].apply(decrypt_data)
        st.dataframe(students)
    else:
        st.warning("Henüz kayıtlı öğrenci yok.")

# Kayıt Düzenleme
elif choice == "Kayıt Düzenleme":
    st.subheader("Öğrenci Kaydını Düzenle")
    students = pd.read_sql_query("SELECT * FROM students", conn)
    students["name"] = students["name"].apply(decrypt_data)
    student_list = students[["id", "name"]].values.tolist()
    student_options = {f"{i[0]} - {i[1]}": i[0] for i in student_list}
    selected_student = st.selectbox(
        "Düzenlenecek Öğrenciyi Seçin", list(student_options.keys())
    )
    new_name = st.text_input("Yeni Ad Soyad")
    new_email = st.text_input("Yeni E-posta")
    new_phone = st.text_input("Yeni Telefon")

    if st.button("Kaydı Güncelle"):
        cursor.execute(
            "UPDATE students SET name = ?, email = ?, phone = ? WHERE id = ?",
            (
                encrypt_data(new_name),
                encrypt_data(new_email),
                encrypt_data(new_phone),
                student_options[selected_student],
            ),
        )
        conn.commit()
        st.success("Kayıt başarıyla güncellendi!")

# Ders Devam Takibi
elif choice == "Ders Devam Takibi":
    st.subheader("Öğrenci Devam Takibi")
    students = pd.read_sql_query("SELECT * FROM students", conn)
    students["name"] = students["name"].apply(decrypt_data)
    student_list = students[["id", "name"]].values.tolist()
    student_options = {f"{i[0]} - {i[1]}": i[0] for i in student_list}
    selected_student = st.selectbox("Öğrenci Seçin", list(student_options.keys()))
    date = st.date_input("Tarih")
    status = st.selectbox("Devam Durumu", ["Katıldı", "Katılmadı"])

    if st.button("Kaydet"):
        cursor.execute(
            "INSERT INTO attendance (student_id, course, date, status) VALUES (?, ?, ?, ?)",
            (
                student_options[selected_student],
                "Belirtilmemiş",
                date.strftime("%Y-%m-%d"),
                status,
            ),
        )
        conn.commit()
        st.success("Devam kaydı başarıyla eklendi")

# İstatistikler
elif choice == "İstatistikler":
    st.subheader("Öğrenci İstatistikleri")
    attendance_data = pd.read_sql_query(
        "SELECT status, COUNT(*) as count FROM attendance GROUP BY status", conn
    )
    if not attendance_data.empty:
        fig, ax = plt.subplots()
        ax.pie(
            attendance_data["count"],
            labels=attendance_data["status"],
            autopct="%1.1f%%",
            startangle=90,
        )
        ax.axis("equal")
        st.pyplot(fig)
    else:
        st.warning("Henüz devam verisi yok.")
