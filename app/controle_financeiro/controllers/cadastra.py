from ..controllers import Controle_FinanceiroModel, request, banco, render_template

def cadastra():
    if request.method == "POST":
        dados = { 
            'data' : request.form["data"],
            'descricao' : request.form["descricao"],
            'valor' : request.form["valor"],
            'categoria' : request.form["categoria"],
            'parcela_atual' : request.form["parcela_atual"],
            'total_parcelas' : request.form["total_parcelas"],
            'cartao_id' : request.form["cartao"]  
        }
        gastos = Controle_FinanceiroModel(**dados)
        banco.session.add(gastos)
        banco.session.commit()
    return render_template("cadastra.html")