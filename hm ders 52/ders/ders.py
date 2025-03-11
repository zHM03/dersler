class Araba:
    def __init__(self,marka,model):
        self.marka = marka
        self.model = model
        
    def bilgileri_goster(self):
        print(f"Marka: {self.marka}, Model: {self.model}")
        
class ElektrikliAraba(Araba):
    def __init__(self, marka, model, batarya_kapasitesi):
        super().__init__(marka, model)
        self.batarya_kapasitesi = batarya_kapasitesi
        
    def batarya_bilgisi(self):
        print(f"batarya kapasitesi: {self.batarya_kapasitesi} kWH")
        
elektrikli_araba = ElektrikliAraba("Tesle", "Model s", 100)
elektrikli_araba.bilgileri_goster()
elektrikli_araba.batarya_bilgisi()

print(issubclass(ElektrikliAraba, Araba)) # class var mı yok mu kontrol eder

print(isinstance(elektrikli_araba, ElektrikliAraba))

araba1 = Araba("BMW", "X5")
araba2 = araba1
print(araba1 is araba2)
2
