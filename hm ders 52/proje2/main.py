import json
import streamlit as st

class PizzaError(Exception):
    def __init__(self, pizza, message):
        super().__init__(message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        super().__init__(pizza, message)
        self.cheese = cheese
        
def pizza_yap(pizza, peynir):
    if pizza not in ["margherita", "Capricciosa", "Calzone"]:
        raise PizzaError(pizza, "Menüde böyle bir pizza yok!")
    if peynir > 100:
        raise TooMuchCheeseError(pizza, peynir,"çok fazla peynir!")
    return f"{pizza} pizza hazır"

st.title("pizza sipariş sistemi")
pizza = st.selectbox("pizza türü", ["margharita", "Capricciosa", "Calzone"])
peynir = st.number_input("peynir miktarı (gram)", min_value=0)
if st.button("sipariş ver"):
    try:
        sonuc = pizza_yap(pizza, peynir)
        pizza_bilgisi = {
            "PizzaTuru": pizza,
            "peynir": peynir
        }
        with open("siparişler.json", "a",encoding='utf-8') as f:
            json.dump(pizza_bilgisi, f)
            f.write("\n")
            st.success("pizza eklendi!")
        st.success(sonuc)
    except TooMuchCheeseError as e:
        st.error(f"{e}: {e.cheese} gram peynir")
    except PizzaError as e:
        st.error(f"{e}: {e.pizza}")
if st.button("sipariş geçmişini göster"):
    try:
        with open("siparişler.json", "r") as f:
            for line in f:
                siparis = json.loads(line)
                st.write(siparis)
    except FileNotFoundError:
        st.error("Henüz sipariş yok!")