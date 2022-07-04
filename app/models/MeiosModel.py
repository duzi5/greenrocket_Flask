from Alchemy import banco

class Meio(banco.Model):
    __tablename__ = "meios"
    id = banco.Column(banco.Integer, primary_key = True)
    nome = banco.Column(banco.String(80))




    def __init__(self, nome): 
        self.nome = nome


    def save_meio(self):
        banco.session.add(self)
        banco.session.commit()


    def get_id(self, nome):
        x = self.query.filter_by(nome = nome).first()
        if  x:
            return x.id
        else:  
            y = Meio(nome)
            banco.session.add(y)
            banco.session.commit()
            return y.id   