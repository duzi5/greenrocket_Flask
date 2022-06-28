
from http.client import SWITCHING_PROTOCOLS
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from sqlalchemy import case
from Alchemy import banco
from ..models.Controle_FinanceiroModel import *
from ..controle_financeiro.controllers.exibeController import controle_financeiro_home
from ..controle_financeiro.controllers.cadastra import cadastra






controle_financeiro = Blueprint('controle_financeiro', __name__, template_folder='pages', static_folder='static')


controle_financeiro.route('/')(controle_financeiro_home)
    

controle_financeiro.route("/cadastra", methods=['GET', 'POST'])(cadastra)



@controle_financeiro.route('/edita_gasto', methods=["GET", "POST"])
def edita_gasto():
    pass

@controle_financeiro.route('/deleta_gasto', methods=["GET", "POST"])
def deleta_gasto():
    pass


