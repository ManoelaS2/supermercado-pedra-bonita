# criar a estrutura do banco de dados

from supermercadopedrabonita import db
from datetime import datetime

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text)
    categoria = db.Column(db.String(50))
    disponivel = db.Column(db.Boolean, default=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    imagem_url = db.Column(db.String(200))
    
    def __repr__(self):
        return f'<Produto {self.nome}>'

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(200))
    observacoes = db.Column(db.Text)
    itens = db.Column(db.Text)  # JSON com os itens do pedido
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pendente')
    data_pedido = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Pedido {self.id} - {self.nome_cliente}>'