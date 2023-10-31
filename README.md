<h1>Desenvolvimento de uma API</h1>

<h3>Resumo do Projeto</h3>
<p>O projeto consiste em uma API desenvolvida com o uso do framework Flask em 
Python. A API proporciona três principais funcionalidades: autenticação de usuários, 
cadastro de novos usuários e geração de números aleatórios dentro de um intervalo 
específico. A segurança das operações é garantida por meio de tokens JWT (JSON 
Web Tokens) para autenticação.</p>

Tecnologias Utilizadas:

• Flask: Framework web utilizado para construir a API.

• Flask JWT Extended: Extensão do Flask para autenticação de usuários usando 
JSON Web Tokens (JWT).

• Flask Swagger UI: Extensão para incorporar a interface Swagger UI, que 
facilita a visualização e teste da API.

• Python: Linguagem de programação utilizada para desenvolver a lógica da 
aplicação.

<br />

<h3>Validação de Dados</h3>

<h4>1.	Página Inicial:</h4>
 
![image](https://github.com/Lucas1726/API-Random/assets/92900328/dc21b036-3da7-40c6-89ed-98b24932715e)

Link: https://ap2uni9.cafuzeira.repl.co

<strong>@app.route('/')</strong> = Esta rota exibe uma mensagem indicando que a API está online e fornece informações sobre os métodos da API.

<br />

<h4>2.	Armazenamento de Informação:</h4>

![image](https://github.com/Lucas1726/API-Random/assets/92900328/fe98f8b8-04e7-4bb0-a2cb-74688cbbfef9)
 
Link: https://ap2uni9.cafuzeira.repl.co/usuarios

<strong>@app.route('/usuarios', methods=['GET'])</strong> = Esta rota permite obter a lista de usuários cadastrados.

![image](https://github.com/Lucas1726/API-Random/assets/92900328/0725ca08-7ae3-41ac-877c-0cab904f533c)

Link: https://ap2uni9.cafuzeira.repl.co/token

<strong>@app.route('/token', methods=['GET'])</strong> = Esta rota permite obter a lista de usuários cadastrados com o Token.

<br />

<h4>3.	Cadastro de Usuários:</h4>

![image](https://github.com/Lucas1726/API-Random/assets/92900328/cd400112-b338-47f7-a536-ec4e66fc554b)

Link: https://ap2uni9.cafuzeira.repl.co/cadastro

<strong>@app.route('/cadastro', methods=['POST'])</strong> = Esta rota permite cadastrar novos usuários na lista usuários, através da chamada JSON abaixo:
{
    "username": "username",
    "password": "password"
}
Para confirmar se o usuário foi cadastrado com sucesso, você pode fazer outra chamada à rota de Armazenamento de Informações (@app.route('/usuarios', methods=['GET'])), caso deseje verificar os dados após o cadastro.
 
![image](https://github.com/Lucas1726/API-Random/assets/92900328/9567a12c-3fb6-4da7-9972-c33510afa897)

<br />

<h4>4.	Autenticação de Usuários:</h4>

![image](https://github.com/Lucas1726/API-Random/assets/92900328/c1634d27-9318-493d-b24e-568168e13a37)

Link: https://ap2uni9.cafuzeira.repl.co/login

<strong>@app.route('/login', methods=['POST'])</strong> = Esta rota permite que os usuários façam login e recebam um token de acesso JWT válido.
Após o token ser gerado, será salvo no de Armazenamento de Informações (@app.route('/token, methods=['GET']))
 
![image](https://github.com/Lucas1726/API-Random/assets/92900328/f1ff2a38-701e-4195-8479-68cd8228ab44)

<br />

<h4>5.	Geração de Números Aleatórios:</h4>

![image](https://github.com/Lucas1726/API-Random/assets/92900328/2de886fc-8852-40cb-8d5d-4060f1b8e83b)

Durante esta etapa, o usuário insere o token gerado no momento do login para acessar a funcionalidade de geração de números aleatórios.

![image](https://github.com/Lucas1726/API-Random/assets/92900328/a29f54e0-4668-44b8-a7e1-e36b860fcc0a)

Link: https://ap2uni9.cafuzeira.repl.co/random?minimo=1&maximo=999&quantidade=10

<strong>@app.route('/random', methods=['GET'])</strong> = Esta rota gera números aleatórios dentro de um intervalo específico, mas requer autenticação usando um token JWT válido.
