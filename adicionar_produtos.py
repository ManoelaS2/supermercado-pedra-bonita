from supermercadopedrabonita import db, app
from supermercadopedrabonita.models import Produto

with app.app_context():
    db.create_all()
    
    produtos = [
        Produto(nome='Arroz 5kg', preco=22.50, categoria='Alimentos', imagem_url='img/produtos/arroz.png'),
        Produto(nome='Feijão 1kg', preco=14.80, categoria='Alimentos', imagem_url='img/produtos/feijao.png'),
        Produto(nome='Sorvete 2L', preco=39.00, categoria='Congelados', imagem_url='img/produtos/sorvete.png'),
        Produto(nome='Tapete de Crochê', preco=35.00, categoria='Artesanato', imagem_url='img/produtos/tapete-croche.png'),
        Produto(nome='Leite 1L', preco=7.50, categoria='Laticínios', imagem_url='img/produtos/leite.png'),
        Produto(nome='Café 500g', preco=17.40, categoria='Bebidas', imagem_url='img/produtos/cafe.png'),

        Produto(nome='Rexona Desodorante Rollon', preco=12.50, categoria='Higiene', imagem_url='img/produtos/rexona-rollon.png'),
        Produto(nome='Rexona Desodorante Spray', preco=18.75, categoria='Higiene', imagem_url='img/produtos/rexona-spray.png'),
        Produto(nome='Rexona Rollon Nivea', preco=11.90, categoria='Higiene', imagem_url='img/produtos/nivea-rollon.png'),
        Produto(nome='Nivea Rexona Spray', preco=15.75, categoria='Higiene', imagem_url='img/produtos/nivea-spray.png'),
        Produto(nome='Shampoo Seda', preco=16.50, categoria='Higiene', imagem_url='img/produtos/shampoo-seda.png'),
        Produto(nome='Condicionador Seda', preco=17.50, categoria='Higiene', imagem_url='img/produtos/condicionador-seda.png'),
        Produto(nome='Sabonete Palmolive', preco=2.70, categoria='Higiene', imagem_url='img/produtos/sabonete-palmolive.png'),
        Produto(nome='Papel Higiênico Carinho', preco=23.50, categoria='Higiene', imagem_url='img/produtos/papel-higienico.png'),

         Produto(nome='Desinfetante', preco=6.50, categoria='Limpeza', imagem_url='img/produtos/desinfetante.png'),
        Produto(nome='Balde Grande', preco=20.50, categoria='Limpeza', imagem_url='img/produtos/balde-grande.png'),
        Produto(nome='Balde Pequeno', preco=9.50, categoria='Limpeza', imagem_url='img/produtos/balde-pequeno.png'),
        Produto(nome='Balde Médio', preco=15.50, categoria='Limpeza', imagem_url='img/produtos/balde-medio.png'),
        Produto(nome='Bacia', preco=38.50, categoria='Limpeza', imagem_url='img/produtos/bacia.png'),
        Produto(nome='Pote Médio', preco=10.50, categoria='Limpeza', imagem_url='img/produtos/pote-medio.png'),
        Produto(nome='Pote de Plástico', preco=3.75, categoria='Limpeza', imagem_url='img/produtos/pote-plastico.png'),

        Produto(nome='Salgadinho Keleck', preco=2.00, categoria='Alimentos', imagem_url='img/produtos/salgadinho.png'),
        Produto(nome='Mentos Iogurte', preco=3.00, categoria='Alimentos', imagem_url='img/produtos/mentos.png'),
        Produto(nome='Trident', preco=2.50, categoria='Alimentos', imagem_url='img/produtos/trident.png'),
        Produto(nome='Fine', preco=1.00, categoria='Alimentos', imagem_url='img/produtos/fine.png'),
        Produto(nome='Paçoca', preco=0.50, categoria='Alimentos', imagem_url='img/produtos/pacoca.png'),
    
    ]
    
    db.session.add_all(produtos)
    db.session.commit()
    print("Produtos adicionados!")