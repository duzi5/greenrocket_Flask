
from Alchemy import banco

from flask_login import UserMixin
# from ..controle_financeiro.controle_financeiro import login_manager

class UserControl(banco.Model, UserMixin):
    __tablename__ = 'usuarios_control'
    id = banco.Column(banco.Integer, primary_key = True)
    username = banco.Column(banco.String(20))
    nome = banco.Column(banco.String(80))
    senha = banco.Column(banco.String(200))
    email = banco.Column(banco.String(100))
    data_nascimento = banco.Column(banco.Date)
    sexo = banco.Column(banco.String(1))
    categorias = banco.Column(banco.String(300))
    ultima_visita = banco.Column(banco.DateTime)
    meios = banco.Column(banco.String(80))
    
    def __init__(self,username, nome, senha, email, data_nascimento, sexo, options, ultima_visita, meios):
        self.username = username
        self.nome = nome
        self.senha = senha
        self.email = email
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.categorias = options
        self.ultima_visita = ultima_visita
        self.meios = meios
  

