# criar as rotas da aplicação
from flask import Flask, app, render_template, request, url_for, redirect, session 

from supermercadopedrabonita import app 

NOME = "Supermercado Pedra Bonita"
TELEFONE = "(62) 99999-9999"

@app.route('/')
def home():
    return render_template('index.html', nome_empresa=NOME, telefone=TELEFONE)

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

@app.route('/finalizar-pedido', methods=['GET', 'POST'])
def finalizar_pedido():
    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')    
        
        return "Pedido recebido!"
    
    return render_template('finalizar_pedido.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
    
        return "Cadastro realizado!"
    
    return render_template('cadastro.html')