import sqlite3
import json

class Database:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = sqlite3.connect("store_users.db")
            cls._instance.cursor = cls._instance.connection.cursor()
            cls._instance.create_tables()
            return cls._instance
        
    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        quantity INTEGER
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        role TEXT
        )
        """)

class ProductManager:
    def __init__(self, json_file):
        self.json_file = json_file
    
    def load_products(self):
        with open(self.json_file, "r") as file:
            return json.load(file)
        
    def update_stock(self, product_name, new_quantity):
        products = self.load_products()
        for product in products:
            if product["name"] == product_name:
                product["stock"] = new_quantity
                with open(self.json_file, "w") as file:
                    json.dump(products, file, indent=4)

class Product:
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price

class ProductFactory:
    @staticmethod
    def create_product(name, stock, price):
        return Product(name, stock, price)
    
class User:
    def __init__(self, username, role):
        self.username = username

class UserFactory:
    @staticmethod
    def create_user(username, role):
        return User(username, role)