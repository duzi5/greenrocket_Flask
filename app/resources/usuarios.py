import email
from genericpath import exists
from flask_restful import Resource, reqparse
from Alchemy import banco
from app.models.UserModel import UserModel



class User(Resource):
    def get(self):
        return {'usuarios': [hotel.json() for hotel in UserModel.query.all()]}      


        
class Usuarios(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('usuario')
    argumentos.add_argument('nascimento')
    argumentos.add_argument('email')
    argumentos.add_argument('aluno')
    
    
    def get(self, nomedocidadao):   
        user =  UserModel.find_user(nomedocidadao)
        if user: 
            return user.json()
        else:
            return "Não existe!"
            

    def post(self, nomedocidadao):
        user = UserModel.find_user(nomedocidadao)
        if user:
           return "Já existe"
        dados = Usuarios.argumentos.parse_args()
        user = UserModel(**dados)
        user.save_user() 
        return user.json()


    def put(self, nomedocidadao): 
        user = UserModel.find_user(nomedocidadao)
        dados = Usuarios.argumentos.parse_args()       
        if user:
            user.update_user(**dados)
        else: 
            user = UserModel(**dados)
            user.save_user()
        return user.json()


    def delete(self, nomedocidadao):
        user = UserModel.find_user(nomedocidadao)
        if user: 
            user.delete_user()
        return "Usuário apagado"
