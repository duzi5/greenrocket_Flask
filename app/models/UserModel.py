from mailbox import NotEmptyError
from Alchemy import banco
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class UserModel(banco.Model, UserMixin):
    __tablename__ ='usuarios'
    id = banco.Column(banco.Integer, primary_key = True)
    usuario = banco.Column(banco.String)
    nascimento = banco.Column(banco.String)
    email = banco.Column(banco.String(80))
    aluno = banco.Column(banco.String)
    senha_hash = banco.Column(banco.String(128))
    
    def __init__(self, usuario, nascimento, email, aluno, senha):
        self.usuario =  usuario
        self.nascimento = nascimento 
        self.email = email
        self.aluno = aluno
        self.senha_hash = generate_password_hash(senha)
 
    
    
    
    def json(self):
        return{
            "id": self.id,
            "usuario": self.usuario,
            "nascimento": self.nascimento,
            "email" : self.email,
            "aluno" : self.aluno,
            "senha" : self.senha_hash
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


    def update_user(self, usuario, nascimento, email, aluno, senha_hash): 
        self.usuario = usuario
        self.nascimento = nascimento
        self.email = email
        self.aluno = aluno
         

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit() 


    def verifica_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

  

 
  