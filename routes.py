from flask import Blueprint, jsonify, request, current_app
from models import Imobiliaria, Imovel, TipoImovel, FinalidadeImovel
from serializer import ImovelSchema, ImobiliariaSchema, FinalidadeImovelSchema, TipoImovelSchema

# Configurando os Schemas para um ou varios imoveis e imobiliarias e também para os Tipos e Finalidade de imovel 
imovelS = ImovelSchema()
tipoImovelS = TipoImovelSchema()
finalidadeImovelS = FinalidadeImovelSchema()
imoveisS = ImovelSchema(many=True)

imobiliariaS = ImobiliariaSchema()
imobiliariasS = ImobiliariaSchema(many=True)

# Função para popular o object de novoImovel ou novaImobiliaria, para evitar repetição de código
# ni serão as informações do NovoImovel ou da NovaImobiliaria
def populaNovosImoveis(data):
    niNome = data['nome']
    niEndereco = data['endereco']
    niDescr = data['descr']
    niStatus = data['status']
    niChar = data['caracteristicas']
    niTipoImovel = data['tipoImovelTipo']
    niFinImovel = data['finalidadeImovelFin']
    niImobilNome = data['imobiliariaNome']
    return Imovel(niNome, niEndereco, niDescr, niStatus, niChar, niTipoImovel, niFinImovel, niImobilNome)

def populaNovasImobiliarias(data):
    niNome = data['nome']
    niEndereco = data['endereco']
    return Imobiliaria(niNome, niEndereco)

## Criando os endpoints para os Imoveis
# Blueprint para os imoveis
bpImoveis = Blueprint('imoveis', __name__)

# Listagem de todos os imoveis
@bpImoveis.route('/', methods=['GET'])
def listarImoveis():
    imoveis = Imovel.query.all()
    return imoveisS.jsonify(imoveis)

# Cadastro de 1 imovel
@bpImoveis.route('/cadastrar', methods=['POST'])
def cadastrarImovel():
    novoImovel = populaNovosImoveis(request.json)
    current_app.db.session.add(novoImovel)
    current_app.db.session.commit()
    return imovelS.jsonify(novoImovel)

# Cadastro de vários imoveis
@bpImoveis.route('/cadastrar/batch', methods=['POST'])
def cadastrarImoveis():
    novosImoveis = []
    for imovel in request.json['imoveis']:
        novoImovel = populaNovosImoveis(imovel)
        novosImoveis.append(novoImovel)
        current_app.db.session.add(novoImovel)

    current_app.db.session.commit()
    return imoveisS.jsonify(novosImoveis)

# Edição de imovel
@bpImoveis.route('/editar/<int:id>', methods=['PUT'])
def editarImovel(id):
    imovel = Imovel.query.get(id)

    imovel.nome = request.json['nome']
    imovel.endereco = request.json['endereco']
    imovel.descr = request.json['descr']
    imovel.status = request.json['status']
    imovel.caracteristicas = request.json['caracteristicas']
    imovel.tipoImovelTipo = request.json['tipoImovelTipo']
    imovel.finalidadeImovelFin = request.json['finalidadeImovelFin']
    imovel.imobiliariaNome = request.json['imobiliariaNome']

    current_app.db.session.commit()
    return imovelS.jsonify(imovel)

# Deleção de imovel
@bpImoveis.route('/deletar/<int:id>', methods=['DELETE'])
def deletarImovel(id):
    imovel = Imovel.query.get(id)

    current_app.db.session.delete(imovel)
    current_app.db.session.commit()
    return imovelS.jsonify(imovel)

# Cadastro de 1 Tipo de Imovel
@bpImoveis.route('/cadastrarTipo', methods=['POST'])
def cadastrarTipoImovel():
    novoTipo = TipoImovel(request.json['tipo'])
    current_app.db.session.add(novoTipo)
    current_app.db.session.commit()
    return tipoImovelS.jsonify(novoTipo)

# Cadastro de 1 imovel
@bpImoveis.route('/cadastrarFinalidade', methods=['POST'])
def cadastrarFinalidadeImovel():
    novaFinalidade = FinalidadeImovel(request.json['finalidade'])
    current_app.db.session.add(novaFinalidade)
    current_app.db.session.commit()
    return finalidadeImovelS.jsonify(novaFinalidade)


## Criando os endpoints para as Imobiliarias
# Blueprint para os imobiliarias
bpImobiliarias = Blueprint('imobiliarias', __name__)

# Listagem de todos as imobiliarias
@bpImobiliarias.route('/', methods=['GET'])
def listarImobilirias():
    imobiliarias = Imobiliaria.query.all()
    return imobiliariasS.jsonify(imobiliarias)

# Cadastro de 1 imobiliaria
@bpImobiliarias.route('/cadastrar', methods=['POST'])
def cadastrarImobiliaria():
    novaImobiliaria = populaNovasImobiliarias(request.json)
    current_app.db.session.add(novaImobiliaria)
    current_app.db.session.commit()
    return imovelS.jsonify(novaImobiliaria)

# Cadastro de vários imobiliarias
@bpImobiliarias.route('/cadastrar/batch', methods=['POST'])
def cadastrarImobiliarias():
    novasImobiliarias = []
    for imobiliaria in request.json['imobiliarias']:
        novaImobiliaria = populaNovasImobiliarias(imobiliaria)
        novasImobiliarias.append(novaImobiliaria)
        current_app.db.session.add(novaImobiliaria)

    current_app.db.session.commit()
    return imobiliariasS.jsonify(novasImobiliarias)

# Edição de imobiliaria
@bpImobiliarias.route('/editar/<int:id>', methods=['PUT'])
def editarImobiliaria():
    imobiliaria = Imobiliaria.query.get(id)

    imobiliaria.nome = request.json['nome']
    imobiliaria.endereco = request.json['endereco']

    current_app.db.session.commit()
    return imovelS.jsonify(imobiliaria)

# Deleção de imovel
@bpImobiliarias.route('/deletar/<int:id>', methods=['DELETE'])
def deletarImobiliaria():
    imobiliaria = Imobiliaria.query.get(id)

    current_app.db.session.delete(imobiliaria)
    current_app.db.session.commit()
    return imovelS.jsonify(imobiliaria)