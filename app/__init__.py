from flask_restful import Api
from flask import Flask, request, copy_current_request_context
from app.resources.usuarios import User, Usuarios, UserLogin, UserRegister
from Alchemy import banco


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(User, '/users')
api.add_resource(Usuarios, '/users/<nomedocidadao>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')







# from app.controllers import defaults

