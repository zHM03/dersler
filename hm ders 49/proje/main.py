import streamlit as st
import sqlite3
import pandas as pd
import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from cryptography.fernet import Fernet
import matplotlib.pyplot as plt

conn = sqlite3.connect("course_registation.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    role TEXT
    )"""
)
cursor.execute(
    """CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        cursor TEXT,
        registration_date TEXT
        )"""
)
cursor.execute(
    """CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course TEXT,
        date TEXT,
        status TEXT,
        FOREIGN KEY(student_id) REFERNCES sutdents(id)
        )"""
)
conn.commit()

def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

