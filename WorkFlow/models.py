# coding: utf-8
from WorkFlow import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.query.get(usuario_id)


class Cliente(db.Model):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    pedidos = db.relationship('Pedido', backref= 'cliente')



class Pedido(db.Model):
    __tablename__ = 'pedido'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.ForeignKey('cliente.id'), index=True)
    data_pedido = db.Column(db.DateTime)
    status = db.Column(db.String(30))
    valor_total = db.Column(db.Numeric(10, 2))



class Produto(db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Numeric(10, 2))
    estoque = db.Column(db.Integer)



t_relatorio = db.Table(
    'relatorio',
    db.Column('id_cliente', db.ForeignKey('cliente.id'), index=True),
    db.Column('pedido_id', db.ForeignKey('pedido.id'), index=True),
    db.Column('produto_id', db.ForeignKey('produto.id'), index=True),
    db.Column('quantidade', db.Integer)
)



class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    senha = db.Column(db.String(255))
    codigo_recuperacao = db.Column(db.String(10))
