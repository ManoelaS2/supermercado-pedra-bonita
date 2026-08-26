from supermercadopedrabonita import db, app
from supermercadopedrabonita.models import Produto

with app.app_context():
    db.create_all()
    
    produtos = [
        Produto(nome='Arroz 5kg', preco=18.90, categoria='Alimentos', imagem_url='img/produtos/arroz.png'),
        Produto(nome='Feijão 1kg', preco=7.50, categoria='Alimentos', imagem_url='img/produtos/feijao.png'),
        Produto(nome='Sorvete 2L', preco=22.90, categoria='Congelados', imagem_url='img/produtos/sorvete.png'),
        Produto(nome='Tapete de Crochê', preco=35.00, categoria='Artesanato', imagem_url='img/produtos/tapete-croche.png'),
        Produto(nome='Leite 1L', preco=4.20, categoria='Laticínios', imagem_url='img/produtos/leite.png'),
        Produto(nome='Café 500g', preco=12.90, categoria='Bebidas', imagem_url='img/produtos/cafe.png'),
    ]
    
    db.session.add_all(produtos)
    db.session.commit()
    print("✅ Produtos adicionados!")