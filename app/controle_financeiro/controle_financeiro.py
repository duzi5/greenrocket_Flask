
from http.client import SWITCHING_PROTOCOLS
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from sqlalchemy import case
from Alchemy import banco
from ..models.Controle_FinanceiroModel import *


controle_financeiro = Blueprint('controle_financeiro', __name__, template_folder='pages', static_folder='static')


@controle_financeiro.route('/', methods=['GET', 'POST'])
def controle_financeiro_home():
    gastos = Controle_FinanceiroModel.query.all()   
    total = 0 
    total_inter = 0 
    total_pan = 0 
    total_c6 = 0
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    total7 = 0
    total8 = 0
    total9 = 0
    total10 = 0

    for gasto in gastos:
        if gasto.cartao_id == 1:
            gasto.cartao_id2 = "Pan"
            total_pan = round(total_pan + gasto.valor, 2)
        elif gasto.cartao_id == 2:
            gasto.cartao_id2 = "Inter"
            total_inter = total_inter + gasto.valor
        else: 
            gasto.cartao_id2 = "C6" 
            total_c6 = total_c6 + gasto.valor  
        
        if gasto.categoria == 1:
            gasto.categoria2 = "Bem-Estar"
            total1 = total1 + gasto.valor
        elif gasto.categoria == 2:
            gasto.categoria2 = "Educação e Softwares"
            total2 = total2 + gasto.valor
        elif gasto.categoria == 3:
            total3 = total3 + gasto.valor
            gasto.categoria2 = "Transporte"
        elif gasto.categoria == 4 :     
            gasto.categoria2 = "Farmácia"
            total4 = round(total4 + gasto.valor, 2)
        elif gasto.categoria == 5 :     
            gasto.categoria2 = "Tabaco e Cia"
            total5 = total5 + gasto.valor
        elif gasto.categoria == 6 :     
            gasto.categoria2 = "Informática"
            total6 = total6 + gasto.valor
        elif gasto.categoria == 7 :     
            gasto.categoria2 = "Academia"
            total7 = total7 + gasto.valor
        elif gasto.categoria == 8 :     
            gasto.categoria2 = "Alimentação"
            total8 = total8 + gasto.valor
        elif gasto.categoria == 9 :     
            gasto.categoria2 = "Mercado"
            total9 = total9 + gasto.valor
        else:
            gasto.categoria2 = "Outros"
            total10 = round(total10 + gasto.valor, 2)
            
       
        
        total = total + gasto.valor   
    
    def totalpercentual(totalcat):
        totalcat= round(totalcat/total * 100, 2)     
        return totalcat 
    
    totalcat1 = totalpercentual(total1)
    totalcat2 = totalpercentual(total2)
    totalcat3 = totalpercentual(total3)
    totalcat4 = totalpercentual(total4)
    totalcat5 = totalpercentual(total5)
    totalcat6 = totalpercentual(total6)
    totalcat7 = totalpercentual(total7)
    totalcat8 = totalpercentual(total8)
    totalcat9 = totalpercentual(total9)
    totalcat10 = totalpercentual(total10)
    
    
    
    
    return render_template('gastos.html', gastos = gastos, total = total, total_c6=total_c6, total_inter = total_inter, total_pan = total_pan, total1 = total1, total2 = total2, total3 = total3, total4 = total4, total5 = total5, total6 = total6, total7 = total7, total8 = total8, total9 = total9, total10 = total10, totalcat1 = totalcat1, totalcat2 = totalcat2, totalcat3 = totalcat3, totalcat4 = totalcat4, totalcat5 = totalcat5, totalcat6 = totalcat6, totalcat7 = totalcat7, totalcat8 = totalcat8, totalcat9 = totalcat9, totalcat10 = totalcat10 )
    

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


