<h1>Desenvolvimento de uma API</h1>

<h2>Resumo do Projeto</h2>
<p>O projeto consiste em uma API desenvolvida com o uso do framework Flask em Python. A API proporciona três principais funcionalidades: autenticação de usuários, cadastro de novos usuários, e geração de números aleatórios dentro de um intervalo específico. A segurança das operações é garantida por meio de tokens JWT (JSON Web Tokens) para autenticação.</p>

<h2>Tecnologias Utilizadas</h2>
<ul>
    <li><strong>Flask:</strong> Framework web utilizado para construir a API.</li>
    <li><strong>Flask JWT Extended:</strong> Extensão do Flask para autenticação de usuários usando JSON Web Tokens (JWT).</li>
    <li><strong>Flask Swagger UI:</strong> Extensão para incorporar a interface Swagger UI, que facilita a visualização e teste da API.</li>
    <li><strong>Python:</strong> Linguagem de programação utilizada para desenvolver a lógica da aplicação.</li>
</ul>

<h2>Validação de Dados</h2>

<h3>1. Página Inicial</h3>
<p><img src="https://github.com/Lucas1726/API-Random/assets/92900328/dc21b036-3da7-40c6-89ed-98b24932715e" alt="Página Inicial da API"></p>
<p>Link: <a href="https://ap2uni9.cafuzeira.repl.co">https://ap2uni9.cafuzeira.repl.co</a></p>
<pre><code>@app.route('/')
</code></pre>
<p>Esta rota exibe uma mensagem indicando que a API está online e fornece informações sobre os métodos da API.</p>

<h3>2. Armazenamento de Informação</h3>
<p><img src="https://github.com/Lucas1726/API-Random/assets/92900328/fe98f8b8-04e7-4bb0-a2cb-74688cbbfef9" alt="Armazenamento de Informação"></p>
<p>Link: <a href="https://ap2uni9.cafuzeira.repl.co/usuarios">https://ap2uni9.cafuzeira.repl.co/usuarios</a></p>
<pre><code>@app.route('/usuarios', methods=['GET'])
</code></pre>
<p>Esta rota permite obter a lista de usuários cadastrados.</p>

<p><img src="https://github.com/Lucas1726/API-Random/assets/92900328/0725ca08-7ae3-41ac-877c-0cab904f533c" alt="Token JWT"></p>
<p>Link: <a href="https://ap2uni9.cafuzeira.repl.co/token">https://ap2uni9.cafuzeira.repl.co/token</a></p>
<pre><code>@app.route('/token', methods=['GET'])
</code></pre>
<p>Esta rota permite obter a lista de usuários cadastrados com o Token.</p>

<h3>3. Cadastro de Usuários</h3>
<p><img src="https://github.com/Lucas1726/API-Random/assets/92900328/cd400112-b338-47f7-a536-ec4e66fc554b" alt="Cadastro de Usuários"></p>
<p>Link: <a href="https://ap2uni9.cafuzeira.repl.co/cadastro">https://ap2uni9.cafuzeira.repl.co/cadastro</a></p>
<pre><code>@app.route('/cadastro', methods=['POST'])
</code></pre>
<p>Esta rota permite cadastrar novos usuários na lista de usuários, através da chamada JSON abaixo:</p>
<pre><code>{
    "username": "username",
    "password": "password"
}
</code></pre>
<p>Para confirmar se o usuário foi cadastrado com sucesso, você pode fazer outra chamada à rota de Armazenamento de Informações (<code>@app.route('/usuarios', methods=['GET'])</code>), caso deseje verificar os dados após o cadastro.</p>
<p><img src="https://github.com/Lucas1726/API-Random/assets/92900328/9567a12c-3fb6-4da7-9972-c33510afa897" alt="Confirmação de Cadastro"></p>

<h3>4. Autenticação de Usuários</h3>
<p><img src="https://github.com/Lucas1726/API-Random/assets/92900328/c1634d27-9318-493d-b24e-568168e13a37" alt="Autenticação de Usuários"></p>
<p>Link: <a href="https://ap2uni9.cafuzeira.repl.co/login">https://ap2uni9.cafuzeira.repl.co/login</a></p>
<pre><code>@app.route('/login', methods=['POST'])
</code></pre>
<p>Esta rota permite que os usuários façam login e recebam um token de acesso JWT válido. Após o token ser gerado, será salvo na rota de Armazenamento de Informações (<code>@app.route('/token', methods=['GET'])</code>).</p>
<p><img src="https://github.com/Lucas1726/API-Random/assets/92900328/f1ff2a38-701e-4195-8479-68cd8228ab44" alt="Token de Autenticação"></p>

<h3>5. Geração de Números Aleatórios</h3>
<p><img src="https://github.com/Lucas1726/API-Random/assets/92900328/2de886fc-8852-40cb-8d5d-4060f1b8e83b" alt="Geração de Números Aleatórios"></p>
<p>Durante esta etapa, o usuário insere o token gerado no momento do login para acessar a funcionalidade de geração de números aleatórios.</p>
<p><img src="https://github.com/Lucas1726/API-Random/assets/92900328/a29f54e0-4668-44b8-a7e1-e36b860fcc0a" alt="Resultado da Geração de Números"></p>
<p>Link: <a href="https://ap2uni9.cafuzeira.repl.co/random?minimo=1&maximo=999&quantidade=10">https://ap2uni9.cafuzeira.repl.co/random?minimo=1&maximo=999&quantidade=10</a></p>
<pre><code>@app.route('/random', methods=['GET'])
</code></pre>
<p>Esta rota gera números aleatórios dentro de um intervalo específico, mas requer autenticação usando um token JWT válido.</p>
