from app import controle_financeiro
from ..controllers import Controle_FinanceiroModel, request, banco, render_template, redirect, url_for, current_user
from datetime import datetime
def cadastra(id):
   
    if current_user and current_user.id == id: 
        if request.method == "POST":
            dados = { 
                'data' : request.form["data"],
                'descricao' : request.form["descricao"],
                'valor' : request.form["valor"],
                'categoria' : request.form["categoria"],
                'parcela_atual' : request.form["parcela_atual"],
                'total_parcelas' : request.form["total_parcelas"],
                'cartao_id' : request.form["cartao"],
                'mes' : request.form["mes"],
                'ano' : request.form["ano"],  
                'user_control_id' : id
            }

            gastos = Controle_FinanceiroModel(**dados)
            banco.session.add(gastos)
            banco.session.commit()
            return redirect(url_for('.cadastra', id = id))
        else: 
            return render_template('cadastra.html', id = id)

    else:
        return('é necessário estar loggado para acessar o cadastro de gastos, você não está em um endereço permitido')    