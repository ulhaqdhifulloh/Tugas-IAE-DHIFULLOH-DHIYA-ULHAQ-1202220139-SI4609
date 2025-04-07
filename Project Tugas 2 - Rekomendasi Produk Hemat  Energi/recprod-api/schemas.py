from flask_marshmallow import Marshmallow
from models import Product, Review

ma = Marshmallow()

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(required=True)
    description = ma.auto_field()
    price = ma.auto_field(required=True)
    rating = ma.auto_field()
    energy_type = ma.auto_field(required=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True

    id = ma.auto_field(dump_only=True)
    product_id = ma.auto_field(required=True)
    username = ma.auto_field(required=True)
    comment = ma.auto_field(required=True)
    rating = ma.auto_field(required=True)
    created_at = ma.auto_field(dump_only=True)

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)