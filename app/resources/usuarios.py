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
    argumentos.add_argument('usuario', type = str, required = True, help = "Esse campo não pode estar em branco")
    argumentos.add_argument('nascimento', type = int, required =True, help = "Esse campo precisa ser preenchido" )
    argumentos.add_argument('email', type = str, required = True, help = "Preencha seu email" )
    argumentos.add_argument('aluno', type = bool, required = True, default = True)
    
    
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
        try:
            user.save_user()
        except: 
            return{"Erro interno do servidor, tente criar novamente"}, 500 
        return user.json()


    def put(self, nomedocidadao): 
        user = UserModel.find_user(nomedocidadao)
        dados = Usuarios.argumentos.parse_args()       
        if user:
            user.update_user(**dados)
        else: 
            user = UserModel(**dados)
            try:
                user.save_user()
            except: 
                return{"Erro interno do servidor, tente criar novamente"}, 500 
        return user.json()


    def delete(self, nomedocidadao):
        user = UserModel.find_user(nomedocidadao)
        if user: 
            try: 
                user.delete_user()
            except:
                return {"Erro do servidor, usuário não foi deletado"}, 500
        return "Usuário apagado"



class UserRegister(Resource):
    def post(self): 
        atributos = reqparse.RequestParser()
        atributos.add_argument('login', required = True, help = "È preciso informar o logim de seu usuário.")
        atributos.add_argument('senha', required = True, help = "È preciso informar a senha.")
        dados = atributos.parse_args()
        if UserModel.find_by_login(dados['login']):
            return "nome de usuário não está disponível."
        else:
            try: 
                user = UserModel(**dados)
                user.save_user()
                return "Usuário criado com sucesso!"
            except:
                return "Erro no servidor, o usuário não foi adicionado."
            

