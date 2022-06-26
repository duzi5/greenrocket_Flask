from flask_login import UserMixin
from Alchemy import banco
from flask_sqlalchemy import SQLAlchemy


class VisitanteModel(banco.Model):
    __tablename__ = 'visitantes'
    id = banco.Column(banco.Integer, primary_key =  True)
    nome = banco.Column(banco.String(80))
    email = banco.Column(banco.String(80))
    telefone = banco.Column(banco.String(11))
    objetivo = banco.Column(banco.Integer)
    minimalista = banco.Column(banco.Boolean)
    negocio = banco.Column(banco.String(80))

    def __init__(self, nome, email, telefone, objetivo, minimalista, negocio):
        self.nome = nome
        self.email = email 
        self.telefone = telefone
        self.objetivo = objetivo
        self.minimalista = minimalista
        self.negocio = negocio

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def update_user(self, nome, email, telefone, objetivo, minimalista, negocio):
        self.nome = nome
        self.email = email
        self.telefone =  telefone
        self.objetivo = objetivo
        self.minimalista = minimalista
        self.negocio = negocio
    
    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()
    
