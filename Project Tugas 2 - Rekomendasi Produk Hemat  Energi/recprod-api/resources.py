from flask_restful import Resource, request
from models import Product, Review, db
from schemas import product_schema, products_schema, review_schema, reviews_schema 
from http import HTTPStatus
from marshmallow import ValidationError

class ProductListResource(Resource):
    def get(self):
        try:
            products = Product.query.all()
            return products_schema.dump(products), HTTPStatus.OK
        except Exception as e:
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

    def post(self):
        data = request.get_json()
        try:
            product = product_schema.load(data)
            db.session.add(product)
            db.session.commit()
            return product_schema.dump(product), HTTPStatus.CREATED
        except ValidationError as err:
            return {'message': str(err)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

class ProductResource(Resource):
    def get(self, product_id):
        try:
            product = Product.query.get_or_404(product_id)
            return product_schema.dump(product), HTTPStatus.OK
        except Exception as e:
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

    def put(self, product_id):
        data = request.get_json()
        try:
            product = Product.query.get_or_404(product_id)
            product = product_schema.load(data, instance=product, partial=True)
            db.session.commit()
            return product_schema.dump(product), HTTPStatus.OK
        except ValidationError as err:
            return {'message': str(err)}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

    def delete(self, product_id):
        try:
            product = Product.query.get_or_404(product_id)
            db.session.delete(product)
            db.session.commit()
            return {'message': 'Produk dihapus'}, HTTPStatus.OK
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
        
class ReviewListResource(Resource):
    def get(self, product_id):
        try:
            reviews = Review.query.filter_by(product_id=product_id).all()
            return reviews_schema.dump(reviews), HTTPStatus.OK
        except Exception as e:
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

    def post(self, product_id):
        data = request.get_json()
        try:
            data['product_id'] = product_id  # inject foreign key
            review = review_schema.load(data)
            db.session.add(review)
            db.session.commit()
            return review_schema.dump(review), HTTPStatus.CREATED
        except ValidationError as err:
            return {'message': err.messages}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR


class ReviewResource(Resource):
    def put(self, review_id):
        data = request.get_json()
        try:
            review = Review.query.get_or_404(review_id)
            review = review_schema.load(data, instance=review, partial=True)
            db.session.commit()
            return review_schema.dump(review), HTTPStatus.OK
        except ValidationError as err:
            return {'message': err.messages}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

    def delete(self, review_id):
        try:
            review = Review.query.get_or_404(review_id)
            db.session.delete(review)
            db.session.commit()
            return {'message': 'Ulasan dihapus'}, HTTPStatus.OK
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR