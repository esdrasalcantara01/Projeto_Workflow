from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, PasswordField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_login import current_user
import random
import os
from WorkFlow import app
from flask import session

from WorkFlow import db, bcrypt

from WorkFlow.models import Pedido, Cliente, Produto, Usuario


class UserCadastro(FlaskForm):
    nome = StringField('Nome: ', validators=[DataRequired()])
    senha = PasswordField('Senha: ', validators=[DataRequired()])
    email = StringField('E-mail: ', validators=[DataRequired(), Email()])
    btmSubmit = SubmitField('Cadastrar')

    def validate_email(self, email):
        if Usuario.query.filter(Usuario.email == email.data).first():
            raise ValidationError("E-mail já existente!!")

    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))

        usuario = Usuario (
            nome= self.nome.data,
            email= self.email.data,
            senha = senha
        )

        db.session.add(usuario)
        db.session.commit()
        return usuario


class LoginCadastro(FlaskForm):
    nome = StringField('nome: ', validators=[DataRequired()])
    senha = PasswordField('Senha: ', validators=[DataRequired()])
    btmSubmit = SubmitField('Enviar')

    def login(self):
        usuario = Usuario.query.filter_by(nome= self.nome.data).first()

        if usuario:
            if bcrypt.check_password_hash(usuario.senha, self.senha.data.encode('utf-8')):
                return usuario
            else:
                erro = f'senha incorreta!'
                return erro
        else:
            erro = f'usuário inexistente!!'
            return erro


class ProdutoDados(FlaskForm):
    nome = StringField('nome: ', validators=[DataRequired()])
    preco = FloatField('preço: ', validators=[DataRequired()])
    estoque = IntegerField('estoque: ', validators=[DataRequired()])
    cadastrar = SubmitField('Aplicar')


    def cadastrar_produto(self):

        produto = Produto(
         nome= self.nome.data,
         preco= self.preco.data,
         estoque= self.estoque.data
        )

        db.session.add(produto)
        db.session.commit()
        return produto


class Cliente_Cadastro(FlaskForm):
    nome = StringField('nome: ', validators=[DataRequired()])
    registrar = SubmitField('registrar ')

    def registrar_cliente(self):
        foto_salvar = session.pop('escolha_aleatória', None)
                  
        cliente = Cliente(
            nome = self.nome.data,
            foto_perfil = foto_salvar
        )


        db.session.add(cliente)
        db.session.commit()
        return cliente


class Pedido_Cadastro(FlaskForm):
    nome_cliente = StringField('nome', validators=[DataRequired()])
    nome_produto = StringField('produto', validators=[DataRequired()])
    quantidade = IntegerField('quantidade', validators=[DataRequired()])
    registrar = SubmitField('registrar')

    def salvar_pedido(self, cliente):

        produto = Produto.query.filter_by(
        nome=self.nome_produto.data
         ).first()

        if not produto:
          raise ValidationError('Produto não encontrado.')

        valor_total = produto.preco * self.quantidade.data

        pedido = Pedido(
          cliente_id = cliente.id,
          produto_id = produto.id,
          quantidade = self.quantidade.data,
          valor_total= valor_total
      )

        db.session.add(pedido)
        db.session.commit()
        return pedido