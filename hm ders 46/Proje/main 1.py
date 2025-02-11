products = [
    {"id": 1, "name": "Çeliç", "category": "El aletleri", "price": 50, "stock": 10},
    {
        "id": 2,
        "name": "Tornavida Seti",
        "category": "El Aletleri",
        "price": 120,
        "stock": 5,
    },
    {
        "id": 3,
        "name": "Çivi 1kg",
        "category": "bağlantı elemanları",
        "price": 120,
        "stock": 5,
    },
    {
        "id": 4,
        "name": "Matkap ucu",
        "category": "elektrikli aletler",
        "price": 30,
        "stock": 2,
    },
    {
        "id": 5,
        "name": "kablo 10m",
        "category": "elektrik malzemeleri",
        "price": 80,
        "stock": 8,
    },
]

# Ürünleri stok durumuna göre sıralama
def sort_products_by_stock():
    return sorted(products, key=lambda x: x["stock"])

# Yeni ürün eklemek için fonksiyon
def add_product(name, category, price, stock):
    new_id = len(products) + 1  # Yeni ID'yi, mevcut ürün sayısından 1 fazla olarak belirle
    products.append(
        {
            "id": new_id,
            "name": name,
            "category": category,
            "price": price,
            "stock": stock,
        }
    )
    print(f"{name} ürünü başarıyla eklendi.")

# Düşük stoklu ürünleri listeleme
def get_low_stock_products(threshold=5):
    return [product for product in products if product["stock"] < threshold]

# Örnek kullanım
print("Stok durumuna göre sıralanmış ürünler:", sort_products_by_stock())

# Yeni ürün eklemek
add_product("Vida Seti", "bağlantı elemanları", 25, 15)

# Düşük stoklu ürünleri listelemek
print("Düşük stoklu ürünler:", get_low_stock_products())
