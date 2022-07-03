from datetime import datetime, date
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from ...models.UserControlModel import UserControl


def login():
    data = date.today()
    mes =   data.month
    ano = data.year

    if request.method == "POST":
        username = request.form['username']
        senha = request.form['senha'] 
        print(username)
        usuario = UserControl.query.filter_by(username = username).first()
        if usuario and usuario.senha == senha:
            login_user(usuario)
            print('Entramos')    
            return redirect(url_for('controle_financeiro.controle_financeiro_home', id = usuario.id, mes = mes, ano = ano))
        else:
            flash('Login inválido') 
    
    return render_template('login.html')    



         