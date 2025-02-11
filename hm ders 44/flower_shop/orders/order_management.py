class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items
        self.total_price = sum(item["flower"].price * item["quantity"] for item in items)
        
    def __str__(self):
        return f"Sipariş Sahibi: {self.user} - Toplam Tutar: ${self.total_price}"

class OrderManager:
    def __init__(self):
        self.orders = []
        
    def __init__(self):
        self.orders = []
        
    def place_order(self, user, items):
        new_order = Order(user, items)
        self.orders.append(new_order)
        return new_order