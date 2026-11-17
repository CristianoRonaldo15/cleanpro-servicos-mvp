from flask import Flask, render_template, request, redirect, url_for
from models import db, Cliente, Agendamento

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleanpro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    clientes = Cliente.query.all()
    agendamentos = Agendamento.query.all()
    return render_template('index.html', clientes=clientes, agendamentos=agendamentos) if False else "Cleanpro Serviços - Banco de Dados Conectado com Sucesso!"

if __name__ == '__main__':
    app.run(debug=True)