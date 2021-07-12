# API-Imobiliarias
Humberto de Souza Reque Junior
Python Dev

## Como rodar o projeto
------

# Bibliotecas necessárias

- flask
- flask_sqlalchemy
- flask_script
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy
- decouple

# Arquivo de configuração de ambiente (.env)

Primeiramente é necessário criar o arquivo de environment (.env) e dentro dele dispor as seguintes informações:
```python
POSTGRES_URL="<URL do Banco>"
POSTGRES_USER="<Usuário do Banco>"
POSTGRES_PW="<Password do usuário>"
POSTGRES_DB="<Nome do Banco>"
```

# Rodando o projeto

Tendo estas informações em mãos, basta rodar o projeto `python app.py`.
Se preferir é possivel criar um pyenv, mas a maneira de rodar o projeto será o mesmo, só será necessário entrar no shell do pyenv primeiro.



## Como fazer as migrações do banco, caso seja necessário
------

# Windows

```PowerShell
py .\manage.py db init
py .\manage.py db migrate
py .\manage.py db upgrade
```

# Linux

```sh
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

ou, caso seu python não esteja apontando paro o python3:

```sh
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
```

## Extras
------

Eu hospedei o projeto no heroku, então a API está ligada, caso queira testar é só clicar [AQUI](https://register-control-senior-test.herokuapp.com)
Eu também deixei um arquivo "exemplo.json", la eu deixei exemplos de dados que os endpoints de criação recebem, lebrando que eles esperam um json com 1 objeto apenas ou 1 array de objetos com nome "imoveis" ou "imobiliarias".

Endpoints:
```Python
<Rule '/imobiliarias/cadastrar/batch' (OPTIONS, POST) -> imobiliarias.cadastrarImobiliarias>
<Rule '/imoveis/cadastrar/batch' (OPTIONS, POST) -> imoveis.cadastrarImoveis>
<Rule '/imobiliarias/cadastrar' (OPTIONS, POST) -> imobiliarias.cadastrarImobiliaria>
<Rule '/imoveis/cadastrarFinalidade' (OPTIONS, POST) -> imoveis.cadastrarFinalidadeImovel>
<Rule '/imoveis/cadastrarTipo' (OPTIONS, POST) -> imoveis.cadastrarTipoImovel>
<Rule '/imoveis/cadastrar' (OPTIONS, POST) -> imoveis.cadastrarImovel>
<Rule '/imobiliarias/' (OPTIONS, HEAD, GET) -> imobiliarias.listarImovobilirias>
<Rule '/imoveis/' (OPTIONS, HEAD, GET) -> imoveis.listarImoveis>
<Rule '/imobiliarias/deletar/<id>' (OPTIONS, DELETE) -> imobiliarias.deletarImobiliaria>
<Rule '/imobiliarias/editar/<id>' (OPTIONS, PUT) -> imobiliarias.editarImobiliaria>
<Rule '/imoveis/deletar/<id>' (OPTIONS, DELETE) -> imoveis.deletarImovel>
<Rule '/imoveis/editar/<id>' (OPTIONS, PUT) -> imoveis.editarImovel>
```
