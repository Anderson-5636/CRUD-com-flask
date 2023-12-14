from flask import Flask

from database import dataBase

from flask_migrate import Migrate

from usuarios import bp_usuarios

app = Flask(__name__)

conexao = "sqlite:///meubanco.sqlite"

app.config['SECRET_KEY'] = 'SECRETO'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATION'] = False
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')

migrate = Migrate(app, dataBase)

dataBase.init_app(app)


@app.route('/')
def index():
  return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)
