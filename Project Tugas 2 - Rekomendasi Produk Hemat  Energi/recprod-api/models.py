from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, default=0.0)
    energy_type = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Product {self.id}: {self.name}>"
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    product = db.relationship("Product", backref="reviews")