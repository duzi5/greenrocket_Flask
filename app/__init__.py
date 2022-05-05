from flask_restful import Api
from flask import Flask
from app.resources.usuarios import User, Usuarios
from Alchemy import banco


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(User, '/users')
api.add_resource(Usuarios, '/users/<nomedocidadao>')






from app.controllers import defaults

