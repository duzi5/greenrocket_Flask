
from datetime import datetime, date

from flask import redirect, request, url_for
from app.models.UserControlModel import UserControl
from app.models.MeiosModel import Meio
from app.models.CategoriaModel import Categoria

from  ..controllers import banco, render_template, Controle_FinanceiroModel, login 
from flask_login import current_user



def controle_financeiro_home(id, mes,ano):
    gastos = Controle_FinanceiroModel.query.filter_by(usuario_control_id = id).filter_by(mes = mes).filter_by(ano = ano)  
    if current_user and request.method == "POST": 
        split = request.form['mes'].split('-')
        mes = split[1]
        ano = split[0]
        
        print (ano)
        print(mes)
        return redirect(url_for('controle_financeiro.controle_financeiro_home', id = id, mes = mes, ano = ano))
    
    if current_user and current_user.id == id and gastos: 
        meios = eval(current_user.meios)
        totalmeio = []
        totalcat = []
        totalm = 0
        totalcategoria = 0
        totalgeral = 0
        percentual = 0

        for meio in meios: 
            totalm = 0 

            meioClass = Meio.query.filter_by(id = meio).first().nome
            for gasto in gastos:
                if gasto.meio == meio:
                    totalm += gasto.valor
                    totalgeral += gasto.valor
            totalmeio.append( {
                    "meio": meioClass,
                    "total": totalm
                    })
                

        categorias = eval(current_user.categorias)
        for categoria in categorias:
            totalcategoria = 0
            catClass = Categoria.query.filter_by(id = categoria).first().nome  
            catClassId = Categoria.query.filter_by(id = categoria).first().id  
            for gasto in gastos: 
                if gasto.categoria == categoria:
                    totalcategoria += gasto.valor 
                if totalgeral == 0: 
                    percentual = 0
                else: 
                    percentual = totalcategoria / totalgeral * 100

            totalcat.append({
                "id" : catClassId,
                "categoria" : catClass,
                "total": totalcategoria, 
                "percentual" : percentual
            })    

        print(totalmeio)
        print(totalcat) 
        
    

    
    return render_template('gastos.html', totalmeio = totalmeio, totalcat = totalcat, gastos = gastos, categorias = categorias, meios = meios, totalm = totalm, totalcategoria = totalcategoria, ano = ano, mes = mes, totalgeral = totalgeral)
