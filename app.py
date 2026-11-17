from flask import Flask, render_template, request
from models import db, Cliente, Agendamento

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleanpro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

def get_common_styles(contraste):
    bg = "#111827" if contraste == "alto" else "#f4f6f9"
    card = "#1f2937" if contraste == "alto" else "white"
    text = "#f9fafb" if contraste == "alto" else "#333"
    border = "#475569" if contraste == "alto" else "#e2e8f0"
    return bg, card, text, border

@app.route('/')
def home():
    contraste = request.args.get('contraste')
    bg, card, text, border = get_common_styles(contraste)
    
    return f"""
    <html>
        <head>
            <meta charset="utf-8">
            <title>Cleanpro Serviços - Painel</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: {bg}; margin: 0; padding: 20px; color: {text}; }}
                .container {{ max-width: 1000px; margin: auto; background: {card}; padding: 30px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); position: relative; }}
                .top-bar {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }}
                .nav a {{ margin-right: 15px; text-decoration: none; color: #0284c7; font-weight: bold; padding: 6px 12px; background: #e0f2fe; border-radius: 4px; }}
                .btn-contraste {{ background: #334155; color: #fff; padding: 5px 12px; font-size: 12px; text-decoration: none; border-radius: 4px; }}
                h1 {{ color: #0284c7; margin-bottom: 5px; }}
                .subtitle {{ color: #666; margin-bottom: 25px; font-size: 14px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
                th, td {{ padding: 14px; text-align: left; border-bottom: 1px solid {border}; font-size: 14px; }}
                th {{ background-color: #0284c7; color: white; }}
                .badge {{ background-color: #10b981; color: white; padding: 5px 10px; border-radius: 20px; font-size: 12px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="top-bar">
                    <div class="nav">
                        <a href="/?contraste={contraste}">🏠 Painel Principal</a>
                        <a href="/clientes?contraste={contraste}">👥 Gestão de Clientes</a>
                    </div>
                    <a href="/?contraste={'alto' if contraste != 'alto' else 'normal'}" class="btn-contraste">👁️ Alto Contraste</a>
                </div>

                <h1>Cleanpro Serviços</h1>
                <div class="subtitle">Painel de Gestão e Acompanhamento Operacional (MVP)</div>
                
                <h3>Agendamentos Recentes</h3>
                <table>
                    <tr><th>Cliente</th><th>Serviço</th><th>Data e Hora</th><th>Status</th></tr>
                    <tr><td>Mariana Silva</td><td>Limpeza Residencial</td><td>17 Nov 2026, 09:00</td><td><span class="badge">Confirmado</span></td></tr>
                    <tr><td>Carlos Souza</td><td>Limpeza de Vidros</td><td>17 Nov 2026, 14:00</td><td><span class="badge">Confirmado</span></td></tr>
                </table>
            </div>
        </body>
    </html>
    """

@app.route('/clientes')
def clientes():
    contraste = request.args.get('contraste')
    bg, card, text, border = get_common_styles(contraste)
    
    return f"""
    <html>
        <head>
            <meta charset="utf-8">
            <title>Cleanpro Serviços - Clientes</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: {bg}; margin: 0; padding: 20px; color: {text}; }}
                .container {{ max-width: 1000px; margin: auto; background: {card}; padding: 30px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); position: relative; }}
                .top-bar {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }}
                .nav a {{ margin-right: 15px; text-decoration: none; color: #0284c7; font-weight: bold; padding: 6px 12px; background: #e0f2fe; border-radius: 4px; }}
                .btn-contraste {{ background: #334155; color: #fff; padding: 5px 12px; font-size: 12px; text-decoration: none; border-radius: 4px; }}
                h1 {{ color: #0284c7; margin-bottom: 5px; }}
                .subtitle {{ color: #666; margin-bottom: 25px; font-size: 14px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
                th, td {{ padding: 14px; text-align: left; border-bottom: 1px solid {border}; font-size: 14px; }}
                th {{ background-color: #0f172a; color: white; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="top-bar">
                    <div class="nav">
                        <a href="/?contraste={contraste}">🏠 Painel Principal</a>
                        <a href="/clientes?contraste={contraste}">👥 Gestão de Clientes</a>
                    </div>
                    <a href="/clientes?contraste={'alto' if contraste != 'alto' else 'normal'}" class="btn-contraste">👁️ Alto Contraste</a>
                </div>

                <h1>Cleanpro Serviços - Clientes</h1>
                <div class="subtitle">Módulo Secundário de Cadastro e Contato</div>
                
                <table>
                    <tr><th>ID</th><th>Nome do Cliente</th><th>Telefone</th><th>Endereço</th></tr>
                    <tr><td>1</td><td>Mariana Silva</td><td>(38) 99888-1111</td><td>Rua das Flores, 120</td></tr>
                    <tr><td>2</td><td>Carlos Souza</td><td>(38) 99777-2222</td><td>Av. Brasil, 450</td></tr>
                </table>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
