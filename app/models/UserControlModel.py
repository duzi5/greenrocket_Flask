from sqlalchemy import ForeignKey
from Alchemy import banco
from flask_login import UserMixin
# from ..controle_financeiro.controle_financeiro import login_manager


class UserControl(banco.Model, UserMixin):
    __tablename__ = 'usuarios_control'
    id = banco.Column(banco.Integer, primary_key = True)
    username = banco.Column(banco.String(20))
    nome = banco.Column(banco.String(80))
    senha = banco.Column(banco.String(200))
   
    def __init__(self,username, nome, senha):
        self.username = username
        self.nome = nome
        self.senha = senha

  

