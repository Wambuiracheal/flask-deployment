import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models import db
from flask_restful import Api
from resources.art import ArtworkDisplayResource, ArtworkResource
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
CORS(app)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

with app.app_context():
    db.create_all()

api.add_resource(ArtworkDisplayResource, '/artworks')
api.add_resource(ArtworkResource, '/artworks/<int:id>')


@app.route('/')
def home():
    return '<h1>Welcome to the Artwork Page</h1>'

if __name__ == '__main__':
    app.run(debug=True)
