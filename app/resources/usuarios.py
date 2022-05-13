from flask_restful import Resource, reqparse
from Alchemy import banco
from app.models.UserModel import UserModel
from flask_login import login_user, login_required, login_manager
import psycopg2


class User(Resource):
    
    @login_required
    def get(self):
        return {'usuarios': [hotel.json() for hotel in UserModel.query.all()]}      


        
class Usuarios(Resource): 
   
    argumentos = reqparse.RequestParser() 
    argumentos.add_argument("usuario", required = True, help = "È preciso informar o logim de seu usuário.")
    argumentos.add_argument("nascimento", type = int, help = "Esse campo precisa ser preenchido" )
    argumentos.add_argument("email", type = str,  help = "Preencha seu email" )
    argumentos.add_argument("aluno", type = str, default = True)
    argumentos.add_argument("senha", required = True, help = "È preciso informar a senha.")


    
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

    @login_required
    def put(self, nomedocidadao): 
        
        argumentos = reqparse.RequestParser() 
        argumentos.add_argument("usuario", required = True, help = "È preciso informar o logim de seu usuário.")
        argumentos.add_argument("nascimento", type = int, help = "Esse campo precisa ser preenchido" )
        argumentos.add_argument("email", type = str,  help = "Preencha seu email" )
        argumentos.add_argument("aluno", type = str, default = True)
        argumentos.add_argument("senha", required = True, help = "È preciso informar a senha.")
        dados = argumentos.parse_args()
        
        
        
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


    @login_required
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
        
        argumentos = reqparse.RequestParser() 
        argumentos.add_argument("usuario", required = True, help = "È preciso informar o logim de seu usuário.")
        argumentos.add_argument("nascimento", type = int, help = "Esse campo precisa ser preenchido" )
        argumentos.add_argument("email", type = str,  help = "Preencha seu email" )
        argumentos.add_argument("aluno", type = str, default = True)
        argumentos.add_argument("senha", required = True, help = "È preciso informar a senha.")
        dados = argumentos.parse_args()
        
        
        
        if UserModel.find_user(dados["usuario"]):
            return "nome de usuário não está disponível."
        else:
            try: 
                cidadao = UserModel(**dados) 
                cidadao.save_user()
                return cidadao.json()                  
            except:
                return "Erro no servidor, o usuário não foi adicionado."
            

class UserLogin(Resource): 
   
   
   
    def post(self):  
        argumentos = reqparse.RequestParser() 
        argumentos.add_argument("usuario", type = str, default = True)
        argumentos.add_argument("senha", required = True, help = "È preciso informar a senha.")
        dados = argumentos.parse_args()
        usuario = UserModel.find_user(dados["usuario"])

        if usuario and usuario.verifica_senha(dados['senha']):
            login_user(usuario)
            return "Usuário logado!"
        else: 
            return "Erro inesperado!"


       

        
        