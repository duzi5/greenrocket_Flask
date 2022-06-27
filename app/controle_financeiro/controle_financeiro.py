
from http.client import SWITCHING_PROTOCOLS
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from sqlalchemy import case
from Alchemy import banco
from ..models.Controle_FinanceiroModel import *
import pandas as pd

controle_financeiro = Blueprint('controle_financeiro', __name__, template_folder='pages', static_folder='estatico')


@controle_financeiro.route('/', methods=['GET', 'POST'])
def controle_financeiro_home():
    gastos = Controle_FinanceiroModel.query.all()
   
    
    
    
    total = 0 
    total_inter = 0 
    total_pan = 0 
    total_c6 = 0
    for gasto in gastos:
        if gasto.cartao_id == 1:
            gasto.cartao_id = "Pan"
            total_pan = round(total_pan + gasto.valor, 2)
        elif gasto.cartao_id == 2:
            gasto.cartao_id = "Inter"
            total_inter = total_inter + gasto.valor
        else: 
            gasto.cartao_id = "C6" 
            total_c6 = total_c6 + gasto.valor  
        
        if gasto.categoria == 1:
            gasto.categoria2 = "Bem-Estar"
        elif gasto.categoria == 2:
            gasto.categoria2 = "Educação e Softwares"
        elif gasto.categoria == 3:
            gasto.categoria2 = "Transporte"
        elif gasto.categoria == 4 :     
            gasto.categoria2 = "Farmácia"
        elif gasto.categoria == 5 :     
            gasto.categoria2 = "Tabaco e Cia"
        elif gasto.categoria == 6 :     
            gasto.categoria2 = "Informática"
        elif gasto.categoria == 7 :     
            gasto.categoria2 = "Academia"
        elif gasto.categoria == 8 :     
            gasto.categoria2 = "Alimentação"
        elif gasto.categoria == 9 :     
            gasto.categoria2 = "Mercado"
        else:
            gasto.categoria2 = "Outros"
            
       
        
        
        total = total + gasto.valor   
    


    
    
    return render_template('gastos.html', gastos = gastos, total = total, total_c6=total_c6, total_inter = total_inter, total_pan = total_pan)
    

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


