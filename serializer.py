from flask_marshmallow import Marshmallow
from models import Imovel, Imobiliaria, FinalidadeImovel, TipoImovel

ma = Marshmallow()

# Schema de Serialização e De-Serialização do Imovel
class ImovelSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'endereco', 'descr', 'status', 'caracteristicas', 'tipoImovelTipo', 'finalidadeImovelFin', 'imobiliariaNome')

# Schema de Serialização e De-Serialização da Imobiliaria
class ImobiliariaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'endereco')

# Schema de Serialização e De-Serialização dos Tipos de Imoveis
class TipoImovelSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tipo')

# Schema de Serialização e De-Serialização das Finalidades dos Imoveis
class FinalidadeImovelSchema(ma.Schema):
    class Meta:
        fields = ('id', 'fin')