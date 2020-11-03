from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    customer_ordes = db.relationship('Order_created', backref='customer')
    

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(30), nullable=False)
    product_order = db.relationship('Order_created', backref='product')

class Order_created(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable = False)

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')
