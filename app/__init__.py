from crypt import methods
import email
from ensurepip import bootstrap

from flask_restful import Api
from flask import Blueprint, Flask, render_template, request, redirect, url_for

from flask_login import LoginManager

from Alchemy import banco
from flask_bootstrap import Bootstrap
from werkzeug.middleware.proxy_fix import ProxyFix
from app.ceo.controllers.ceoController import ceoController
from app.controle_financeiro.controle_financeiro import controle_financeiro
from app.controle_financeiro.controle_financeiro import UserControl
from flask_migrate import Migrate
from app.ceo import ceo
import os


app = Flask(__name__)

banco.init_app(app)


app.register_blueprint(controle_financeiro, url_prefix="/financas")
app.register_blueprint(ceo, url_prefix="/ceo")


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('STRING_CONEXAO')
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
