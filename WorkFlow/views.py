import os 
import random
from WorkFlow import app
from flask import render_template, url_for, redirect
from WorkFlow.models import Usuario, Produto, Cliente
from WorkFlow.forms import UserCadastro, ProdutoDados, LoginCadastro, Pedido_Cadastro, Cliente_Cadastro
from flask_login import login_user, logout_user, current_user


@app.route('/', methods = ['GET', 'POST'])
def pagina_piloto():
    usuario = 'Visitante'

    cliente = Cliente.query.order_by(Cliente.id)

    lista_Clientes = {'clientes': cliente.all()}

    pasta_imagens = os.path.join(app.root_path, 'static', 'images')

    listar_imagens = os.listdir(pasta_imagens)
    escolha_aleatória = random.choice(listar_imagens)

    return render_template('dashboard.html', 
                           lista_Clientes = lista_Clientes, 
                           usuario = usuario,
                           escolha_aleatória= escolha_aleatória )


@app.route('/cadastrar_pedido', methods = ['GET', 'POST'])
def cadastrar_pedido():
    form = Pedido_Cadastro()

    if form.validate_on_submit():
        return redirect(url_for('pagina_piloto'))
    else:
        print("erro inesperado: ", form.errors)
    return render_template('cadastrar_pedido.html', form= form)


@app.route('/cadastrar_produto', methods = ['GET', 'POST'])
def cadastrar_produto():

    return render_template('cadastrar_produto.html')


@app.route('/cadastrar_cliente', methods = ['GET', 'POST'])
def cadastrar_cliente():

    form = Cliente_Cadastro()
    if form.validate_on_submit():
        return redirect(url_for('pagina_piloto'))
    else:
        print("erro inesperado: ", form.errors)
        
    return render_template('cadastrar_cliente.html', form= form)