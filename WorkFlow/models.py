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
    foto_perfil = db.Column(db.String(100))
    

class Produto(db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Numeric(10, 2))
    estoque = db.Column(db.Integer)



class Pedido(db.Model):
    __tablename__ = 'pedido'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.ForeignKey('cliente.id'), index=True)
    produto_id = db.Column(db.ForeignKey('produto.id'), index=True)
    quantidade = db.Column(db.Integer)
    data_pedido = db.Column(db.DateTime)
    valor_total = db.Column(db.Numeric(10, 2))




itens_pedidos = db.Table(
    'itens_pedidos',
    db.Column('pedido_id', db.ForeignKey('pedido.id'), index=True),
    db.Column('produto_id', db.ForeignKey('produto.id'), index=True),
    db.Column('quantidade', db.Integer)
)


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    senha = db.Column(db.String(255))
    
