# criar as rotas da aplicação
from flask import Flask, app, render_template, request, url_for, redirect, session 
from supermercadopedrabonita import app, db 

from supermercadopedrabonita.models import Produto 
import unicodedata

def remover_acentos(texto):
    """Remove acentos e deixa minúsculo"""
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ASCII', 'ignore').decode('ASCII')
    return texto.lower()

NOME = "Supermercado Pedra Bonita"
TELEFONE = "(62) 99999-8888"

@app.route('/')
def home():
    produtos = Produto.query.all()
    return render_template('index.html', nome_empresa=NOME, telefone=TELEFONE, produtos=produtos)

@app.route('/login')
def login():
    pass

@app.route('/meus-pedidos')
def meus_pedidos():
    pass

@app.route('/admin')
def admin():
    pass

@app.route('/admin/produtos')
def admin_produtos():
    pass

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
    
        return "Cadastro realizado!"
    
    return render_template('cadastro.html')

@app.route('/produtos')
def produtos():
    categoria = request.args.get('categoria', 'todos')
    busca = request.args.get('q', '')
    
    if categoria == 'todos':
        lista_produtos = Produto.query.all()
    else:
        lista_produtos = Produto.query.filter_by(categoria=categoria).all()
    
    if busca:
        busca_sem_acentos = remover_acentos(busca)
        
        todos_produtos = Produto.query.all()
        lista_produtos = [
            p for p in todos_produtos 
            if busca_sem_acentos in remover_acentos(p.nome)
        ]
    
    categorias = db.session.query(Produto.categoria).distinct().all()
    
    return render_template('produtos.html', 
                         produtos=lista_produtos, 
                         categorias=categorias, 
                         categoria_atual=categoria,
                         busca=busca)

@app.route('/adicionar-carrinho/<int:produto_id>')
def adicionar_carrinho(produto_id):
    produto = Produto.query.get(produto_id)
    
    if produto:
        if 'carrinho' not in session:
            session['carrinho'] = []
        
        carrinho = session['carrinho']
        
        for item in carrinho:
            if item['id'] == produto.id:
                item['quantidade'] = item.get('quantidade', 1) + 1  
                session['carrinho'] = carrinho
                return redirect(url_for('carrinho'))
        
        carrinho.append({
            'id': produto.id,
            'nome': produto.nome,
            'preco': produto.preco,
            'imagem': produto.imagem_url,
            'quantidade': 1 
        })
        session['carrinho'] = carrinho
        
        return redirect(url_for('carrinho'))
    
    return "Produto não encontrado"

@app.route('/aumentar/<int:produto_id>')
def aumentar_quantidade(produto_id):
    carrinho = session.get('carrinho', [])
    
    for item in carrinho:
        if item['id'] == produto_id:
            item['quantidade'] += 1
    
    session['carrinho'] = carrinho
    return redirect(url_for('carrinho'))

@app.route('/diminuir/<int:produto_id>')
def diminuir_quantidade(produto_id):
    carrinho = session.get('carrinho', [])
    
    for item in carrinho:
        if item['id'] == produto_id:
            item['quantidade'] -= 1
            if item['quantidade'] <= 0:
                carrinho.remove(item)
    
    session['carrinho'] = carrinho
    return redirect(url_for('carrinho'))

@app.route('/carrinho')
def carrinho():
    itens = session.get('carrinho', [])
    
    total = sum(item['preco'] * item.get('quantidade', 1) for item in itens)
    
    return render_template('carrinho.html', itens=itens, total=total)

@app.route('/remover/<int:produto_id>')
def remover_item(produto_id):
    carrinho = session.get('carrinho', [])
    
    carrinho = [item for item in carrinho if item['id'] != produto_id]
    
    session['carrinho'] = carrinho
    return redirect(url_for('carrinho'))

@app.route('/finalizar-pedido')
def finalizar_pedido():
    itens = session.get('carrinho', [])
    
    if not itens:
        return redirect(url_for('carrinho'))
    
    total = sum(item['preco'] * item.get('quantidade', 1) for item in itens)
    
    return render_template('finalizar_pedido.html', itens=itens, total=total)

@app.route('/processar-pedido', methods=['POST'])
def processar_pedido():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    endereco = request.form.get('endereco')
    observacoes = request.form.get('observacoes')
    
    itens = session.get('carrinho', [])
    total = sum(item['preco'] * item.get('quantidade', 1) for item in itens)
    
    # Salvar pedido
    novo_pedido = Pedido(
        nome_cliente=nome,
        telefone=telefone,
        endereco=endereco,
        observacoes=observacoes,
        itens=json.dumps(itens),
        total=total
    )
    
    db.session.add(novo_pedido)
    db.session.commit()
    
    # Gerar mensagem
    mensagem = f" *NOVO PEDIDO #{novo_pedido.id}*\n\n"
    mensagem += f"*Cliente:* {nome}\n"
    mensagem += f"*Telefone:* {telefone}\n"
    if endereco:
        mensagem += f"*Endereço:* {endereco}\n"
    mensagem += f"\n*Itens:*\n"
    
    for item in itens:
        subtotal = item['preco'] * item.get('quantidade', 1)
        mensagem += f"- {item.get('quantidade', 1)}x {item['nome']} = R$ {subtotal:.2f}\n"
    
    mensagem += f"\n*TOTAL: R$ {total:.2f}*"
    
    if observacoes:
        mensagem += f"\n\n*Observações:* {observacoes}"
    
    session.pop('carrinho', None)
    
    numero_whatsapp = "5562999998888"
    link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensagem}"
    
    return redirect(link_whatsapp)