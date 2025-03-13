# API Flask com JWT e Swagger

## Visão Geral
Esta é uma API desenvolvida em Flask que inclui autenticação com JWT, documentação via Swagger e funcionalidades para cadastro, login e geração de números aleatórios.

## Tecnologias Utilizadas
- Python
- Flask
- Flask-JWT-Extended
- Flask-Swagger-UI

## Instalação
1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando a API
Para rodar a API localmente, execute:
```bash
python app.py
```
A API estará disponível em `http://localhost:5000`.

## Endpoints
### 1. Homepage
- **GET /**
- Retorna uma mensagem indicando que a API está online e uma descrição dos endpoints disponíveis.

### 2. Documentação Swagger
- **GET /swagger**
- Disponibiliza a documentação interativa via Swagger.

### 3. Cadastro de Usuário
- **POST /cadastro**
- Requisição (JSON):
  ```json
  {
    "username": "usuario",
    "password": "senha"
  }
  ```
- Respostas:
  - 200: Usuário cadastrado com sucesso
  - 400: Nome de usuário já em uso

### 4. Login
- **POST /login**
- Requisição (JSON):
  ```json
  {
    "username": "usuario",
    "password": "senha"
  }
  ```
- Respostas:
  - 200: Retorna um token JWT
  - 403: Credenciais inválidas

### 5. Obter Lista de Usuários
- **GET /usuarios**
- Retorna a lista de usuários cadastrados.

### 6. Obter Tokens Gerados
- **GET /token**
- Retorna a lista de tokens gerados.

### 7. Gerar Números Aleatórios (Requer JWT)
- **GET /random?minimo=<valor>&maximo=<valor>&quantidade=<valor>**
- Gera uma lista de números aleatórios dentro do intervalo especificado.
- Requisição:
  - Headers: `Authorization: Bearer <token>`
- Respostas:
  - 200: Retorna um JSON com a lista de números aleatórios
  - 400: Parâmetros inválidos

## Autenticação JWT
Os endpoints protegidos requerem um token JWT válido. Após o login, o token deve ser incluído no cabeçalho da requisição como:
```
Authorization: Bearer <token>
```

## Considerações Finais
- Certifique-se de que o arquivo `swagger.json` esteja na pasta `static` para que a documentação seja carregada corretamente.
- Para ambiente de produção, substitua a `JWT_SECRET_KEY` por uma chave mais segura.

---
**Autor:** Lucas Gonçalves

