from sqlalchemy import ForeignKey

from Alchemy import banco




class Controle_FinanceiroModel(banco.Model): 
    __tablename__ = 'gastos'
    id = banco.Column(banco.Integer, primary_key = True)
    data = banco.Column(banco.Date)
    descricao = banco.Column(banco.String(80))
    valor = banco.Column(banco.Float)
    categoria = banco.Column(banco.Integer)
    parcela_atual = banco.Column(banco.Integer)
    total_parcelas = banco.Column(banco.Integer)
    cartao_id = banco.Column(banco.Integer, ForeignKey('cartoes.id'))
    cartoes = banco.relationship("CartaoModel")

    def __init__(self, data, descricao, valor, categoria, parcela_atual, total_parcelas, cartao_id):
        self.data = data
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.parcela_atual = parcela_atual
        self.total_parcelas = total_parcelas
        self.cartao_id = cartao_id










class CartaoModel(banco.Model):
    __tablename__ = 'cartoes'
    id = banco.Column(banco.Integer, primary_key = True)
    cartao = banco.Column(banco.Integer)
    data_vencimento = banco.Column(banco.Date)
    
    def __init__(self, cartao, data_vencimento):    
        self.cartao = cartao
        self.data_vencimento = data_vencimento