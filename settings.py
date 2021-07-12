from decouple import config

# Configuração para fazer o Heroku funcionar, pq ele quem da a porta
HEROKU_URL = config('HEROKU_URL')
PORT = config('PORT', default=5000)

# Buscando informações do environment, nesse caso usando arquivo .env
DATABASE_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=config('POSTGRES_USER'),pw=config('POSTGRES_PW'),url=config('POSTGRES_URL'),db=config('POSTGRES_DB'))
