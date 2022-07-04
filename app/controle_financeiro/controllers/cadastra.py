from app import controle_financeiro

from app.models.CategoriaModel import CategoriaModel
from app.models.MeiosModel import Meio
from ..controllers import Controle_FinanceiroModel, request, banco, render_template, redirect, url_for, current_user
from datetime import datetime
def cadastra(id):
   
    if current_user and current_user.id == id: 
        
        stringgg = current_user.meios
        meios = eval(stringgg)
        didi2=[]
       
        for meio in meios: 
            nomemeio = Meio.query.filter_by(id = meio).first().nome
            dictmeio ={ 
                "id" : meio,
                "nome" : nomemeio
            }
            didi2.append(dictmeio)
        
        
        
        
        
        stringg = current_user.categorias
        # categorias = stringg.split(',')
        categorias = eval(stringg)
        
       
           
        
        print(categorias)
        didi = []        
        
        for categoria in categorias:
            regcategoria = CategoriaModel.query.filter_by(id = categoria).first()
            dictcategoria = {
                'id' : categoria,
                'categoria' : regcategoria
            }
            didi.append(dictcategoria)

        print(didi[2]['categoria'])
        if request.method == "POST":
            dados = { 
                'data' : request.form["data"],
                'descricao' : request.form["descricao"],
                'valor' : request.form["valor"],
                'categoria' : request.form["categoria"],
                'parcela_atual' : request.form["parcela_atual"],
                'total_parcelas' : request.form["total_parcelas"],
                'meio' : request.form["cartoes"],
                'usuario_control_id' : current_user.id,
                'mes' : 7-2022,
            }

            
            

            gastos = Controle_FinanceiroModel(**dados)
            banco.session.add(gastos)
            banco.session.commit()
            return redirect(url_for('.cadastra', id = id))
        else: 
            return render_template('cadastra.html', id = id, categorias = categorias, didi = didi, didi2 = didi2)

    else:
        return('é necessário estar loggado para acessar o cadastro de gastos, você não está em um endereço permitido')    