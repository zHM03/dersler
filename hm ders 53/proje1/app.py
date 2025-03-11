from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

class BankaHesabi:
    def __init__(self, isim, bakiye = 0):
        self.isim = isim
        self.bakiye = bakiye
        
    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            return True
        return False
    
    def para_cek(self, miktar):
        if 0 < miktar <= self.bakiye:
            self.bakiye -= miktar
            return True
        return False
    
hesap = BankaHesabi("Ahmet", 1000)

@app.route("/")
def index():
    return render_template("index.html", bakiye=hesap.bakiye)

@app.route("/yatir", methods=["POST"])
def yatir():
    miktar = float(request.form.get("miktar"))
    if hesap.para_yatir(miktar):
        return jsonify({"bakiye": hesap.bakiye, "mesaj": "Para yarıma başarılı"})
    return jsonify({"hata": "Geçersiz miktar!"}), 400

@app.route("/cek", methods=["POST"])
def cek():
    miktar = float(request.form.get("miktar"))
    if hesap.para_cek(miktar):
        return jsonify({"Bakiye": hesap.bakiye, "mesaj": "para çekme başarılı"})
    return jsonify({"hata": "yetersiz bakiye veya geçersiz miktar"}), 400

if __name__ == "__main__":
    app.run(debug=True)