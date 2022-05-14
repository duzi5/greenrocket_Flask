from flask_restful import Api
from flask import Blueprint, Flask
from app.resources.usuarios import User, Usuarios, UserRegister, UserLogin
from flask_login import LoginManager
from app.models import UserModel
from Alchemy import banco




app = Flask(__name__)

 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dfkzaikcvapuga:53a950cc262dfa0976e626087e8cfc978bdc9295fcffa70acee3a06f662d4c28@ec2-52-200-215-149.compute-1.amazonaws.com:5432/d9utdggln4gbf6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "nada"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(session_token):
    return UserModel.get(session_token)



api = Api(app)

api.add_resource(User, '/users')
api.add_resource(Usuarios, '/users/<nomedocidadao>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')


@app.route("/")
def index():
    return "Página carregada com sucesso"






# from app.controllers import defaults

