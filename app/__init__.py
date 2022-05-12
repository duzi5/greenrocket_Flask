from flask_restful import Api
from flask import Blueprint, Flask
from app.resources.usuarios import User, Usuarios, UserRegister, UserLogin
from flask_login import LoginManager
from app.models import UserModel






app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
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








# from app.controllers import defaults

