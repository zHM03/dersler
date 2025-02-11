class flower:
    def __init__(self, flower_id, name, price, stock):
        self.flower_id = flower_id
        self.name = name
        self.price = price
        self.stock = stock
        
    def __str__(self):
        return f"{self.flower_id} - {self.name} - ${self.price} - Stok {self.stock}"
    
class FlowerManager:
    def __init__(self):
        self.flowers = []
        
    def add_flower(self, flower_id, name, price, stock):
        new_flower = flower(flower_id, name, price, stock)
        self.flowers.append(new_flower)
        return new_flower
    
    def find_flower(self, flower_id):
        for flower in self.flowers:
            if flower.flower_id == flower_id:
                return flower
        return None
    
    def update_stock(self, flower_id, quantity):
        flower = self.find_flower(flower_id)
        if flower:
            if flower.stock >= quantity:
                flower.stock -= quantity
                return True
        return False