

from flask import Flask
from flask_cors import CORS
from app import create_app

app = create_app()
CORS(app)



# app.run()