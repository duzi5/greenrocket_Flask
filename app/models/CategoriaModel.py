from Alchemy import banco

class CategoriaModel(banco.Model):
    __tablename__ = 'categorias'
    id = banco.Column(banco.Integer, primary_key = True)
    categoria = banco.Column(banco.String(13))
    


    def __init__(self, categoria):
        self.categoria = categoria



