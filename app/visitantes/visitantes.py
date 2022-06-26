from flask import Blueprint, render_template, request, redirect, url_for, current_app 
from Alchemy import banco
from ..models.VisitanteModel import *

visitantes = Blueprint('visitantes', __name__, template_folder="templeteVisitantes", static_folder="static2")



@visitantes.route("/questionario", methods=["GET", "POST"])
def questionario(): 
    return render_template("questionario.html")

@visitantes.route('/visitas', methods=['POST', 'UPDATE'])
def visitas():    
    if request.method == "POST":
        dados = {
            "nome" : request.form.get('nome'),
            "email" : request.form.get('email'),            
            "telefone" : request.form.get('telefone'),
            "objetivo" : request.form.get('objetivo'), 
            "minimalista" : request.form.get('minimalista'),
            "negocio" : request.form.get("negocio")
        }
        visitante = VisitanteModel(**dados)
        visitante.save_user()
    return render_template("visitas.html")


@visitantes.route("/listaVisitantes", methods=["POST", "GET"])
def ListaVisitante():
    visitantes = VisitanteModel.query.all()
    return render_template('listaVisitantes.html', visitantes = visitantes)

@visitantes.route('/editaVisitante/<int:id>', methods=["POST", "GET"])
def EditaVisitante(id):
    visitante = VisitanteModel.query.filter_by(id=id).first()
    return render_template("editaVisitante.html", visitante = visitante)

@visitantes.route('/editaVisitante/atualizaVisitante/<int:id>', methods=["POST"])
def AtualizaVisitante(id):
    if request.method == "POST":
        dados = {
            "nome" : request.form.get('nome'),
            "email" : request.form.get('email'),            
            "telefone" : request.form.get('telefone'),
            "objetivo" : request.form.get('objetivo'), 
            "minimalista" : request.form.get('minimalista'),
            "negocio" : request.form.get("negocio")
        }
        VisitanteModel.query.filter_by(id=id).update(dados)
        banco.session.commit()
        
        return redirect(url_for('ListaVisitante'))
     
@visitantes.route('/editaVisitante/apagar/<int:id>', methods=["POST", "GET"])
def deletaVisitante(id):
    visitante = VisitanteModel.query.filter_by(id=id).first()
    banco.session.delete(visitante)
    banco.session.commit()
    return redirect(url_for('ListaVisitante'))

    