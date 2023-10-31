from flask import Flask, request, jsonify, send_from_directory, make_response
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import random

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secretpassword'
jwt = JWTManager(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "https://ap2uni9.cafuzeira.repl.co"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

usuarios = []
token = []


@app.route('/static/swagger.json')
def serve_swagger():
  return send_from_directory('static', 'swagger.json')


@app.route('/')
def homepage():
  retorno = 'A API está online.</br>'
  retorno += '<h3>Métodos da API</h3>'
  retorno += '<em>/random?minimo=<valor>&maximo=<valor>&quantidade=<valor></em> - Gerar números aleatórios dentro de um intervalo específico.</br>'
  return retorno


@app.route('/token', methods=['GET'])
def get_token():
  return make_response(jsonify(token))


@app.route('/usuarios', methods=['GET'])
def get_usuarios():
  return make_response(jsonify(usuarios))


@app.route('/cadastro', methods=['POST'])
def cadastro():
  novo_usuario = request.json
  if novo_usuario in usuarios:
    return make_response(
        jsonify(
            message='Nome de usuário já em uso. Escolha outro nome de usuário.'
        ), 400)
  else:
    usuarios.append(novo_usuario)
    return make_response(jsonify(message='Usuário cadastrado com sucesso'),
                         200)


@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  username_input = data.get('username')
  password = data.get('password')
  for user in usuarios:
    if user['username'] == username_input and user['password'] == password:
      access_token = create_access_token(identity=username_input)
      token.append({
          'username': username_input,
          'password': password,
          'access_token': access_token
      })
      return jsonify(access_token=access_token), 200
  return jsonify(message='Credenciais inválidas'), 403


@app.route('/random', methods=['GET'])
@jwt_required()
def gerar_numeros():
  try:
    minimo = int(request.args.get('minimo'))
    maximo = int(request.args.get('maximo'))
    quantidade = int(request.args.get('quantidade'))
    lista = []
    for i in range(quantidade):
      lista.append(random.randint(minimo, maximo))
    return make_response(jsonify({'lista': lista}))
  except ValueError:
    return make_response(jsonify(message='Parâmetros inválidos'), 400)


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
