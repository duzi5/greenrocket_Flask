
from app.models.CategoriaModel import CategoriaModel

from flask import render_template, request


def cadastrousuarios():
    
    
    print(request.form.getlist('options'))
      
    return render_template('cadastrousuarios.html')