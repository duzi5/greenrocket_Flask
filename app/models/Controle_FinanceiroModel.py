from email.policy import default
from sqlalchemy import ForeignKey

from Alchemy import banco
from .UserControlModel  import UserControl



class Controle_FinanceiroModel(banco.Model): 
    __tablename__ = 'gastos'
    id = banco.Column(banco.Integer, primary_key = True)
    data = banco.Column(banco.Date)
    descricao = banco.Column(banco.String(80))
    valor = banco.Column(banco.Float)
    categoria = banco.Column(banco.Integer)
    parcela_atual = banco.Column(banco.Integer)
    total_parcelas = banco.Column(banco.Integer)
    mes = banco.Column(banco.Integer)
    ano = banco.Column(banco.Integer)
    meio = banco.Column(banco.Integer)
    usuario_control_id = banco.Column(banco.Integer, banco.ForeignKey('usuarios_control.id'))
    usuario = banco.relationship('UserControl', foreign_keys = usuario_control_id)

    

    def __init__(self, data, descricao, valor, categoria, parcela_atual, total_parcelas, usuario_control_id, mes, ano, meio ):
        self.data = data
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.parcela_atual = parcela_atual
        self.total_parcelas = total_parcelas
        self.usuario_control_id= usuario_control_id
        self.mes = mes
        self.ano = ano
        self.meio = meio









