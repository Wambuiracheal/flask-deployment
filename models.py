from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from sqlalchemy import Enum

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # relationships
    exhibitions = db.relationship('Exhibition', back_populates='user', cascade='all,delete-orphan')

    serialize_rules = ('-exhibitions.user',)

# class Category(db.Model, SerializerMixin):
#     __tablename__ = 'categories'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False)
    
#     # relationships
#     artworks = db.relationship('Artwork', back_populates='categories', cascade='all,delete-orphan')

class Artwork(db.Model, SerializerMixin):
    __tablename__ = 'artworks'
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.Enum('painting','sculpture','photography', name='category_enum'))

    def to_dict(self):
        return {
            "id": self.id, 
            "artist": self.artist,
            "title": self.title,
            "image": self.image,
            "price": self.price,
            "category": self.category
        }

    # relationships
    exhibitions = db.relationship('Exhibition', back_populates='artwork', cascade='all,delete-orphan')

    serialize_rules = ('-exhibitions.artwork',)

class Exhibition(db.Model, SerializerMixin):
    __tablename__ = 'exhibitions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # relationships
    user = db.relationship('User',  back_populates='exhibitions')
    artwork = db.relationship('Artwork', back_populates='exhibitions')

    serialize_rules = ('-user.exhibitions', '-artwork.exhibitions')





    
