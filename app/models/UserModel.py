from mailbox import NotEmptyError
from Alchemy import banco


class UserModel(banco.Model):
    __tablename__ ='usuarios'
    
    usuario = banco.Column(banco.String, primary_key = True)
    nascimento = banco.Column(banco.Integer)
    email = banco.Column(banco.String(80))
    aluno = banco.Column(banco.String)

    def __init__(self, usuario, nascimento, email, aluno):
        self.usuario =  usuario
        self.nascimento = nascimento 
        self.email = email
        self.aluno = aluno

   
    def json(self):
        return{
            'usuario': self.usuario,
            'nascimento': self.nascimento,
            'email' : self.email,
            'aluno' : self.aluno
        }
    
    
    @classmethod
    def find_user(cls, usuario):
        usuario = cls.query.filter_by(usuario = usuario).first()
        if usuario: 
            return usuario; 
        else: 
            False


    def save_user(self):
        banco.session.add(self)
        banco.session.commit() 


    def update_user(self, usuario, nascimento, email, aluno): 
        self.usuario = usuario
        self.nascimento = nascimento
        self.email = email
        self.aluno = aluno


    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit() 

