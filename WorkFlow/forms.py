from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, PasswordField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_login import current_user


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


class Cliente_Status(FlaskForm):
    nome = StringField('nome: ', validators=[DataRequired()])
    pedido = StringField('pedido: ', validators=[DataRequired()])
    registrar = SubmitField('registrar: ')


    def registrar_pedido(self):

        cliente = Cliente(
            nome = self.nome.data,
            pedido = self.pedido.data
        )

        db.session.add(cliente)
        db.session.commit()
        return cliente