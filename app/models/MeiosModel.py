from Alchemy import banco

class Meio(banco.Model):
    __tablename__ = "meios"
    id = banco.Column(banco.Integer, primary_key = True)
    nome = banco.Column(banco.String(80))




    def __init__(self, nome): 
        self.nome = nome


    def save_meio(self):
        banco.session.add(self)
        banco.session.commit(self)


    def get_id(self, nome):
        nomedomeio = banco.query.filter_by(nome = nome).first()
        if nomedomeio:
            return nomedomeio.id
        else: 
            banco.session.add(nomedomeio)
            banco.session.commit(nomedomeio)
            return nomedomeio.id   