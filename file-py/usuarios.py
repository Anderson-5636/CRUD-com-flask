# importando o Blueprint para ver as rotas
from re import U
from flask import Blueprint, request, redirect 
from flask.templating import render_template
from models import Usuario
from database import dataBase

bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates')


#adicionando rota para os templates
@bp_usuarios.route('/create', methods=['GET', 'POST'])
def Create():
  if request.method=='GET':
    return render_template('Create_usuarios.html')

  elif request.method=='POST':
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    csenha = request.form['csenha']

    u = Usuario(nome, email, senha)
    dataBase.session.add(u)
    dataBase.session.commit()
    return 'Usuário cadastrado com sucesso'

@bp_usuarios.route('/list')
def List(): 

    usuarios = Usuario.query.all()
    return render_template('List_usuario.html', usuarios=usuarios)  

@bp_usuarios.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

  u = Usuario.query.get(id)

  if request.method=='GET':
    return render_template('update_usuarios.html', u=u)

  elif request.method=='POST':
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    csenha = request.form['csenha']

    u.nome = nome
    u.email = email
    dataBase.session.commit()
    return redirect('/usuarios/list')

@bp_usuarios.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  u = Usuario.query.get(id)
  if request.method=='GET':
    return render_template('Delete_usuarios.html', u = u)

  elif request.method=='POST':
    dataBase.session.delete(u)
    dataBase.session.commit()
    return redirect('/usuarios/list')
