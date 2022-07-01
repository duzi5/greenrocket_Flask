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
    cartao_id = banco.Column(banco.Integer, banco.ForeignKey('cartoes.id'))
    cartoes = banco.relationship('CartaoModel', foreign_keys = cartao_id )
    usuario_control_id = banco.Column(banco.Integer, banco.ForeignKey('usuarios_control.id'))
    usuario = banco.relationship('UserControl', foreign_keys = usuario_control_id)

    

    def __init__(self, data, descricao, valor, categoria, parcela_atual, total_parcelas, cartao_id, usuario_control_id, mes ):
        self.data = data
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.parcela_atual = parcela_atual
        self.total_parcelas = total_parcelas
        self.cartao_id = cartao_id
        self.usuario_control_id= usuario_control_id
        self.mes = mes


class CartaoModel(banco.Model):
    __tablename__ = 'cartoes'
    id = banco.Column(banco.Integer, primary_key = True)
    cartao = banco.Column(banco.String(10))
    data_vencimento = banco.Column(banco.Date)
    
    def __init__(self, cartao, data_vencimento):    
        self.cartao = cartao
        self.data_vencimento = data_vencimento







