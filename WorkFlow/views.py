from WorkFlow import app
from flask import render_template, url_for, redirect
from WorkFlow.models import Usuario, Produto
from WorkFlow.forms import UserCadastro, ProdutoDados, LoginCadastro
from flask_login import login_user, logout_user, current_user


@app.route('/', methods = ['GET', 'POST'])
def pagina_piloto():
    usuario = 'Visitante'
    form = ProdutoDados()

    if form.validate_on_submit():
       print("formulário válido")

       form.cadastrar_produto()
       print("produto enviado!!")

       return redirect(url_for('pagina_piloto'))
    else:
        print("erro desconhecido!!")
        print("Se acusa!!: ",form.errors)
    return render_template('dashboard.html', form = form, usuario = usuario)


@app.route('/cadastrar_cliente', methods = ['GET', 'POST'])
def cadastrar_cliente():

    return render_template('cadastrar_cliente.html')


@app.route('/cadastrar_produto', methods = ['GET', 'POST'])
def cadastrar_produto():

    return render_template('cadastrar_produto.html')


@app.route('/cadastrar_pedido', methods = ['GET', 'POST'])
def cadastrar_pedido():

    return render_template('cadastrar_pedido.html')