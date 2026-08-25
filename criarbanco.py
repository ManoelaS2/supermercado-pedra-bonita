from supermercadopedrabonita import db, app

from supermercadopedrabonita.models import Produto, Pedido

with app.app_context():
    db.create_all()
    print("Banco de dados criado com sucesso!")