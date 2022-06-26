
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from Alchemy import banco
from ..models.Controle_FinanceiroModel import *

controle_financeiro = Blueprint('controle_financeiro', __name__, template_folder='pages', static_folder='static')


@controle_financeiro.route('/', methods=['GET', 'POST'])
def controle_financeiro_home():
    gastos = Controle_FinanceiroModel.query.all()
    return render_template('gastos.html', gastos = gastos)
    

@controle_financeiro.route("/cadastra", methods=['GET', 'POST'])
def cadastra():
    if request.method == "POST":
        dados = { 
            'data' : request.form["data"],
            'descricao' : request.form["descricao"],
            'valor' : request.form["valor"],
            'categoria' : request.form["categoria"],
            'parcela_atual' : request.form["parcela_atual"],
            'total_parcelas' : request.form["total_parcelas"],
            'cartao_id' : request.form["cartao"]  
        }
        gastos = Controle_FinanceiroModel(**dados)
        banco.session.add(gastos)
        banco.session.commit()
    return render_template("cadastra.html")


@controle_financeiro.route('/edita_gasto', methods=["GET", "POST"])
def edita_gasto():
    pass

@controle_financeiro.route('/deleta_gasto', methods=["GET", "POST"])
def deleta_gasto():
    pass


