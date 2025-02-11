from flower_shop import (
    FlowerManager, OrderManager, UserManager, FlowerNotFoundError, 
    OutOfStockError, UserNotFoundError, save_to_file, load_from_file,
    Flower, Order, User
)

def main():
    flower_manager = FlowerManager()
    order_manager = OrderManager()
    user_manager = UserManager()
    
    # Örnek çiçekler ve kullanıcılar ekleyelim
    flower_manager.add_flower("001", "Gül", 10.0, 50)
    flower_manager.add_flower("002", "Lale", 5.0, 100) 
    user_manager.add_user("001", "Alice")
    user_manager.add_user("002", "Bob")
    
    while True:
        print("\nÇiçek Satış Platformu")
        print("1. Çiçekleri Listele")
        print("2. Sepete Çiçek Ekle")
        print("3. Sipariş Ver")
        print("4. Verileri Kaydet")
        print("5. Verileri Yükle")
        print("6. Çıkış")
        choice = input("Seçiminiz: ")
        
        if choice == "1":
            # Çiçekleri listele
            for flower in flower_manager.flowers:
                print(flower)
                
        elif choice == "2":
            try:
                flower_id = input("Sepete eklemek istediğiniz çiçeğin ID'sini girin: ")
                flower = flower_manager.find_flower(flower_id)
                
                if not flower:
                    raise FlowerNotFoundError("Çiçek bulunamadı.")
                
                quantity = int(input("Miktar girin: "))
                
                if quantity > flower.stock:
                    raise OutOfStockError("Yeterli stok yok.")
                
                flower_manager.update_stock(flower_id, quantity)
                print(f"{flower.name} sepete eklendi.")
                
            except (FlowerNotFoundError, OutOfStockError) as e:
                print("Hata:", e)
                
        elif choice == "3":
            user_id = input("Kullanıcının ID'sini girin: ")
            user = user_manager.find_user(user_id)
            
            if not user:
                print("Kullanıcı bulunamadı.")
                continue
            
            items = []
            while True:
                flower_id = input("Sepete eklemek istediğiniz çiçeğin ID'sini girin (çıkmak için 'q'): ")
                
                if flower_id.lower() == 'q':
                    break
                
                flower = flower_manager.find_flower(flower_id)
                
                if not flower:
                    print("Çiçek bulunamadı.")
                    continue
                
                quantity = int(input("Miktar girin: "))
                
                if quantity > flower.stock:
                    print("Yeterli stok yok.")
                    continue
                
                items.append({"flower": flower, "quantity": quantity})
                flower_manager.update_stock(flower_id, quantity)
            
            if items:
                order = order_manager.place_order(user.name, items)
                print(f"Sipariş verildi: {order}")
            else:
                print("Sepetiniz boş.")
                
        elif choice == "4":
            # Verileri kaydet
            data = {
                "flowers": [
                    {
                        "flower_id": f.flower_id,
                        "name": f.name,
                        "price": f.price,
                        "stock": f.stock,
                    }
                    for f in flower_manager.flowers
                ],
                "orders": [
                    {
                        "user": o.user,
                        "items": [
                            {
                                "flower_id": item["flower"].flower_id,
                                "quantity": item["quantity"],
                            }
                            for item in o.items
                        ],
                    }
                    for o in order_manager.orders
                ],
                "users": [{"user_id": u.user_id, "name": u.name} for u in user_manager.users],
            }
            save_to_file(data, "data.json")
            print("Veriler kaydedildi.")
        
        elif choice == "5":
            # Verileri yükle
            data = load_from_file("data.json")
            if data:
                flower_manager.flowers = [
                    Flower(f["flower_id"], f["name"], f["price"], f["stock"])
                    for f in data["flowers"]
                ]
                order_manager.orders = [
                    Order(
                        o["user"],
                        [
                            {
                                "flower": flower_manager.find_flower(item["flower_id"]),
                                "quantity": item["quantity"],
                            }
                            for item in o["items"]
                        ],
                    )
                    for o in data["orders"]
                ]
                user_manager.users = [
                    User(u["user_id"], u["name"]) for u in data["users"]
                ]
                print("Veriler yüklendi.")
            else:
                print("Kayıtlı veri bulunamadı.")
        
        elif choice == "6":
            break
        
        else: 
            print("Geçersiz seçim.")
            
if __name__ == "__main__":
    main()
