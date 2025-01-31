from flask_restful import Resource
from flask import request, jsonify
from models import Artwork, db

# ARTWORK
class ArtworkDisplayResource(Resource):
    def get(self):
        artworks = Artwork.query.all()
        return ([artwork.to_dict() for artwork in artworks])

    def post(self):
        data = request.get_json()
        if not data or not all(key in data for key in ['artist', 'title', 'image', 'price', 'category']):
            return ({'error': 'Missing required fields'}), 400

        new_artwork = Artwork(**data)
        db.session.add(new_artwork)
        db.session.commit()
        return new_artwork.to_dict()

class ArtworkResource(Resource):
    def get(self, id):
        artwork = Artwork.query.get(id)
        if not artwork:
            return jsonify({'error': 'Artwork not found, Invalid'}), 404
        return jsonify(artwork.to_dict()), 200

    def patch(self, id):
        data = request.get_json()
        artwork = Artwork.query.get(id)
        if not artwork:
            return ({'error': 'Artwork trying to update cannot be found'}), 404
        
        if 'artist' in data:
            artwork.artist = data['artist']
        if 'title' in data:
            artwork.title = data['title']
        if 'image' in data:
            artwork.image = data['image']
        if 'price' in data:
            artwork.price = data['price']
        if 'category' in data:
            artwork.category = data['category']

        db.session.commit()
        return (artwork.to_dict()), 200

    def delete(self, id):
        artwork = Artwork.query.get(id)
        if not artwork:
            return ({'error': 'Product not found'}), 404
        
        db.session.delete(artwork)
        db.session.commit()
        return ({'message': 'Artwork Deleted'}), 200
