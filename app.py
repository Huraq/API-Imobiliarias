# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from settings import DATABASE_URL, PORT
from models import db
from routes import bpImoveis, bpImobiliarias

# Inicializando o App e as configuração de DB do SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# "Conectando" o objeto DB com a aplicação
db.init_app(app)
app.db = db

# Adicionando os endpoints para imoveis e imobiliarias 
app.register_blueprint(bpImoveis, url_prefix='/imoveis')
app.register_blueprint(bpImobiliarias, url_prefix='/imobiliarias')

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'Message': 'It\'s up and running!'})

# Roda o app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=PORT)