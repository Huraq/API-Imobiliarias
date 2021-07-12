
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Inicializando o DB para controle das integrações do flask
db = SQLAlchemy()

## Definição das Classes/Modelos das tabelas
# Class/Model do Imóvel
class Imovel(db.Model):
    __tablename__ = "Imovel"
    # Relacionamentos
    tipoImovel = db.relationship('TipoImovel')
    finalidadeImovel = db.relationship('FinalidadeImovel')
    imobiliaria = db.relationship('Imobiliaria', backref=db.backref('imoveis', lazy=True))

    # Campos da tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(120), nullable=False)
    descr = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    caracteristicas = db.Column(db.Text)
    tipoImovelTipo = db.Column(db.String(16), db.ForeignKey('TipoImovel.tipo'), nullable=False)
    finalidadeImovelFin = db.Column(db.String(16), db.ForeignKey('FinalidadeImovel.fin'), nullable=False)
    imobiliariaNome = db.Column(db.String(150), db.ForeignKey('Imobiliaria.nome'), nullable=False)

    # Construtor da classe Imovel
    def __init__(self, nome, endereco, descr, status, caracteristicas, tipoImovelTipo, finalidadeImovelFin, imobiliariaNome):
        self.nome = nome
        self.endereco = endereco
        self.descr = descr
        self.status = status
        self.caracteristicas = caracteristicas
        self.tipoImovelTipo = tipoImovelTipo
        self.finalidadeImovelFin = finalidadeImovelFin
        self.imobiliariaNome = imobiliariaNome



# Class/Model de controle dos tipos de Imoveis
class TipoImovel(db.Model):
    __tablename__ = "TipoImovel"
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(16), unique=True)

    # Construtor da classe TipoImovel
    def __init__(self, tipo):
        self.tipo = tipo


# Class/Model de controle das finalidades dos Imoveis
class FinalidadeImovel(db.Model):
    __tablename__ = "FinalidadeImovel"
    id = db.Column(db.Integer, primary_key=True)
    fin = db.Column(db.String(16), unique=True)

    # Construtor da classe FinalidadeImovel
    def __init__(self, fin):
        self.fin = fin

# Class/Model da Imobiliária
class Imobiliaria(db.Model):
    __tablename__ = "Imobiliaria"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), unique=True, nullable=False)
    endereco = db.Column(db.String(120))

    # Construtor da classe Imobiliaria
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
    