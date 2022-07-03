from Alchemy import banco
from app.models.CategoriaModel import CategoriaModel

from flask import redirect, render_template, request, url_for

from app.models.UserControlModel import UserControl
from app.models.MeiosModel import Meio
from datetime import datetime, date
def cadastrousuarios():
    if request.method == "POST":
        
        meiosids= []
        meios = request.form['meios']
        meios = eval(meios)
        for meio in meios:
            x = Meio(meio)
            meiosids.append(x.get_id())

        
        dados = {
            "username" : request.form['username'],
            "nome" : request.form['nome'],
            "sexo" : request.form['sexo'],
            "options" : request.form.getlist('options'),
            "data_nascimento" : request.form['data_nascimento'],
            "email" : request.form['email'],
            "senha" : request.form['senha'],
            "meios" : meiosids,
            "ultima_visita" : datetime.now()

        }

        user = UserControl(**dados)
        banco.session.add(user)
        banco.session.commit()
        
        
   
    
        
        return redirect(url_for('controle_financeiro.login'))

 
      
    return render_template('cadastrousuarios.html')