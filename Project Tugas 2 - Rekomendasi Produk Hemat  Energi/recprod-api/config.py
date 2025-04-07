import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///recprod.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False