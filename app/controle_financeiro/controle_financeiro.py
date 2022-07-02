
from http.client import SWITCHING_PROTOCOLS
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from sqlalchemy import case
from Alchemy import banco
from ..models.Controle_FinanceiroModel import *
from ..models.UserControlModel import UserControl
from ..controle_financeiro.controllers.exibeController import controle_financeiro_home
from ..controle_financeiro.controllers.cadastra import cadastra
from ..controle_financeiro.controllers.login import login
from ..controle_financeiro.controllers.logout import logout
from ..controle_financeiro.controllers.cadastrousuarios import cadastrousuarios

from flask_login import LoginManager, login_required



controle_financeiro = Blueprint('controle_financeiro', __name__, url_prefix = 'financas', template_folder='pages', static_folder='static')


controle_financeiro.route('/exibe/<int:id>/<int:mes>/<int:ano>', methods=['GET', 'POST'])(login_required(controle_financeiro_home))
    
controle_financeiro.route('/cadastra/<int:id>', methods=['GET', 'POST'])(login_required(cadastra))

controle_financeiro.route('/', methods=["GET", "POST"])(login)

controle_financeiro.route('/logout', methods=["GET", "POST"])(logout)

controle_financeiro.route('/cadastrousuarios', methods=["GET", "POST"])(cadastrousuarios)



@controle_financeiro.route('/edita_gasto', methods=["GET", "POST"])
def edita_gasto():
    pass

@controle_financeiro.route('/deleta_gasto', methods=["GET", "POST"])
def deleta_gasto():
    pass



