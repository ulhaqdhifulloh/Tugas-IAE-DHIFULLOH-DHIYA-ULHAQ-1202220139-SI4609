from flask import Flask
from flask_restful import Api
from config import Config
from models import db
from schemas import ma
from resources import ProductListResource, ProductResource, ReviewListResource, ReviewResource
from flask_cors import CORS  # Impor CORS

app = Flask(__name__)
app.config.from_object(Config)

# Aktifkan CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Inisialisasi ekstensi
db.init_app(app)
ma.init_app(app)
api = Api(app)

# Mendaftarkan resource
api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<int:product_id>')
api.add_resource(ReviewListResource, '/products/<int:product_id>/reviews')
api.add_resource(ReviewResource, '/reviews/<int:review_id>')

# Membuat tabel database saat pertama kali dijalankan
@app.before_request
def create_tables():
    db.create_all()
    
@app.route('/')
def index():
    return {'message': 'Welcome to the API Recommended Renewable Energy Products'}, 200


if __name__ == '__main__':
    app.run(debug=True)
