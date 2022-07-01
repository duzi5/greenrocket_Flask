
from datetime import datetime, date

from flask import redirect, request, url_for
from app.models.UserControlModel import UserControl
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
        usuario = UserControl.query.filter_by(id = id).first()
        
        if gastos:
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
                totalcat= round(totalcat/(total +0.001) * 100, 2)     
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
        else: 
            return "Não foi encontrado nenhum valor referente ao período refinado"    

    else: 
        return('é necessário estar loggado para acessar o cadastro de gastos, você não está em um endereço permitido')        
        
    

    
    return render_template('gastos.html', ano = ano, mes = mes, id = id ,usuario = usuario, gastos = gastos, total = total, total_c6=total_c6, total_inter = total_inter, total_pan = total_pan, total1 = total1, total2 = total2, total3 = total3, total4 = total4, total5 = total5, total6 = total6, total7 = total7, total8 = total8, total9 = total9, total10 = total10, totalcat1 = totalcat1, totalcat2 = totalcat2, totalcat3 = totalcat3, totalcat4 = totalcat4, totalcat5 = totalcat5, totalcat6 = totalcat6, totalcat7 = totalcat7, totalcat8 = totalcat8, totalcat9 = totalcat9, totalcat10 = totalcat10 )
