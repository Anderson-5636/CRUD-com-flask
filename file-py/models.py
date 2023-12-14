from database import dataBase


class Usuario(dataBase.Model):
  __tablename__ = 'usuarios'
  id = dataBase.Column(dataBase.Integer, primary_key=True)
  nome = dataBase.Column(dataBase.String(100))
  email = dataBase.Column(dataBase.String(100))
  senha = dataBase.Column(dataBase.String(100))

  def __init__(self, nome, email, senha):
    self.nome = nome
    self.email = email
    self.senha = senha

  def __repr__(self):
    return 'usuario {}'.format(self.nome)
    #return '<Usuario %r>' % self.nome PESQUISAAR
