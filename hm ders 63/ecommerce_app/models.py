from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    UserID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Email = db.Column(db.String(100), unique=True)
    passwordhash = db.Column(db.String(266))

class Category(db.Model):
    __tablename__ = 'categories'
    CategoryID = db.Column(db.Integer, primary_key=True)
    CategoryName = db.Column(db.String(100))

class Product(db.Model):
    __tablename__ = 'products'
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(100))
    Price = db.Column(db.Numeric(10, 2))
    Stock = db.Column(db.Integer)
    CategoryID = db.Column(db.Integer, db.ForeignKey('categories.CategoryID'))

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
class Order(db.Model):
    __tablename__ = 'orders'
    OrderID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'))
    OrderDate = db.Column(db.DateTime)
    TotalAmount = db.Column(db.Numeric(10, 2))
    status = db.Column(db.String(50), default='Pending')

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    OrderItemID = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.Integer, db.ForeignKey('orders.OrderID'))
    ProductID = db.Column(db.Integer, db.ForeignKey('products.ProductID'))
    Quantity = db.Column(db.Integer)
    Price = db.Column(db.Numeric(10, 2))

class User(db.Model):
    __tablename__ = 'users'
    UserID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Email = db.Column(db.String(100), unique=True)
    passwordhash = db.Column(db.String(266))

    def set_password(self, password):
        self.passwordhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordhash, password)
    