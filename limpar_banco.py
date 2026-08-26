from supermercadopedrabonita import db, app
from supermercadopedrabonita.models import Produto

with app.app_context():
    Produto.query.delete()
    db.session.commit()
    print("Banco limpo!")