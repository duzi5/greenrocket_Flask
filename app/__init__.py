from crypt import methods
import email
from ensurepip import bootstrap

from flask_restful import Api
from flask import Blueprint, Flask, render_template, request, redirect, url_for

from flask_login import LoginManager

from Alchemy import banco
from flask_bootstrap import Bootstrap
from werkzeug.middleware.proxy_fix import ProxyFix

from app.controle_financeiro.controle_financeiro import controle_financeiro
from app.controle_financeiro.controle_financeiro import UserControl
from flask_migrate import Migrate


app = Flask(__name__)

banco.init_app(app)


app.register_blueprint(controle_financeiro, url_prefix="/financas")


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dfkzaikcvapuga:53a950cc262dfa0976e626087e8cfc978bdc9295fcffa70acee3a06f662d4c28@ec2-52-200-215-149.compute-1.amazonaws.com:5432/d9utdggln4gbf6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "nada"


Migrate(app, banco)



bootstrap = Bootstrap(app)


api = Api(app)




@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/cadastro_form")
def cadastro():    
    return render_template("cadastro.html")


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return UserControl.query.filter_by(id = id).first()
