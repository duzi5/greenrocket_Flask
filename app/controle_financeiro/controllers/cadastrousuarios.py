from Alchemy import banco
from app.models.CategoriaModel import Categoria

from flask import redirect, render_template, request, url_for

from app.models.UserControlModel import UserControl
from app.models.MeiosModel import Meio
from datetime import datetime, date
def cadastrousuarios():
    if request.method == "POST":
        
        meios = request.form['meios']
        meios2 = eval(meios)
        meiosids= []
        print(meios2)
        for meio in meios2:
            print(meio)
            
            x = Meio(meio)
            y = x.get_id(meio)
            
            
            meiosids.append(y)

        
        dados = {
            "username" : request.form['username'],
            "nome" : request.form['nome'],
            "sexo" : request.form['sexo'],
            "categorias" : request.form.getlist('categorias'),
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