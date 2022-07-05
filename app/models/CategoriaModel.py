from sqlalchemy import null
from Alchemy import banco

class Categoria(banco.Model):
    __tablename__ = 'categorias'
    id = banco.Column(banco.Integer, primary_key = True)
    nome = banco.Column(banco.String(13))
    


    def __init__(self, nome):
        self.nome = nome


    def get_cat( id):
        if Categoria is not null:
            return Categoria.query.filter_by(id = id).first().nome
        else:
            return null    
