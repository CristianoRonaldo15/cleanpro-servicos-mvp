from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servico = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='Pendente')
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)