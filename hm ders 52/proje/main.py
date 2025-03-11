import json
import streamlit as st

# Araba sınıfı tanımlaması
class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        return f"{self.marka} {self.model} ({self.yil})"

# Elektrikli Araba sınıfı tanımlaması
class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, batarya_kapasitesi):
        super().__init__(marka, model, yil)
        self.batarya_kapasitesi = batarya_kapasitesi

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()}, Batarya: {self.batarya_kapasitesi} kWh"

# Sayfa stilini ve fontu ayarlama
st.markdown("""
    <style>
        body {
            background-color: #570082;
            font-family: 'Arial', sans-serif;
        }
        h1 {
            color: #ed5f00;
            font-size: 40px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextInput>div>input {
            background-color: #ffffff;
            border-radius: 5px;
            padding: 10px;
        }
        .stSelectbox>div>select {
            background-color: #ffffff;
            border-radius: 5px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Başlık
st.title("Araba Kiralama Sistemi")

# Araba türü seçimi
araba_turu = st.selectbox("Araba Türü", ["Normal", "Elektrikli"])

# Marka, model ve yıl girişleri
marka = st.text_input("Marka")
model = st.text_input("Model")
yil = st.number_input("Yıl", min_value=1900, max_value=2023)

# Elektrikli araba için batarya kapasitesi
if araba_turu == "Elektrikli":
    batarya_kapasitesi = st.number_input("Batarya Kapasitesi (kWh)", min_value=0)
    araba = ElektrikliAraba(marka, model, yil, batarya_kapasitesi)
else:
    araba = Araba(marka, model, yil)

# Kaydet butonu
if st.button("Kaydet"):
    araba_bilgisi = {
        "marka": araba.marka,
        "model": araba.model,
        "yil": araba.yil,
        "batarya": getattr(araba, "batarya_kapasitesi", None),  # Elektrikli arabalar için batarya bilgisi
    }
    
    # JSON dosyasına kaydetme
    with open("arabalar.json", "a") as f:
        json.dump(araba_bilgisi, f)
        f.write("\n")  # Her araba bilgisini yeni bir satıra yazıyoruz
        st.success("Araba bilgisi kaydedildi!")

# Arabaları gösterme butonu
if st.button("Arabaları Göster"):
    try:
        with open("arabalar.json", "r") as f:
            # Dosyadaki her bir araba bilgisini gösterme
            for line in f:
                araba = json.loads(line)
                st.write(araba)
    except FileNotFoundError:
        st.error("Henüz kayıtlı araba yok.")
