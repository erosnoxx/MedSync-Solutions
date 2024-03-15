# SUMÁRIO
1. [Sobre o Projeto]()
2. [Instalação](#instalação)
    - [Requisitos de Sistema](#1-requisitos-de-sistema)
    - [Clonar o Repositório](#2-clonar-o-repositório)
    - [Instalar Dependências](#3-instalar-dependências)
    - [Fazer Migrações com Flask Migrate](#4-fazer-migrações-com-flask-migrate)
    - [Executar o Projeto](#5-executar-o-projeto)
3. [APIs](#apis)
    - [Registro de Usuário](#registro-de-usuário)
    - [Login de Usuário](#login-de-usuário)
    - [Adicionar Paciente](#adicionar-paciente)

---

# Instalação

Siga estas etapas para configurar e executar o projeto localmente:

### 1. Requisitos de Sistema

- Python 3.11.0: Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo e instalá-lo a partir do [site oficial do Python](https://www.python.org/downloads/) ou usando um gerenciador de pacotes, como o Anaconda.

### 2. Clonar o Repositório

Clone o repositório do projeto em sua máquina local usando o seguinte comando:

```bash
git clone git@github.com:erosnoxx/MedSync-Solutions.git
```

### 3. Instalar Dependências

Navegue até o diretório do projeto e instale as dependências listadas no arquivo `requirements.txt`. Você pode fazer isso executando o seguinte comando:

```bash
cd seu-repositorio
pip install -r requirements.txt
```

### 4. Fazer Migrações com Flask Migrate

Certifique-se de que todas as migrações do banco de dados estejam atualizadas. Se o seu projeto estiver usando Flask Migrate, você pode fazer isso executando os seguintes comandos:

```bash
flask db init
flask db migrate
flask db upgrade
```

### 5. Executar o Projeto

Após instalar as dependências e fazer as migrações, você pode iniciar o servidor de desenvolvimento. Use o seguinte comando:

```bash
flask run
```

O servidor será iniciado e o seu projeto estará disponível localmente. Você pode acessá-lo em um navegador da web digitando `http://localhost:5000`.

Agora você está pronto para começar a trabalhar no projeto localmente!

Se você tiver qualquer problema durante a instalação ou execução do projeto, não hesite em entrar em contato para obter ajuda.

# API's


# Registro de Usuário

Este endpoint é responsável por registrar um novo usuário no sistema.

## Requisição

- **Método:** `POST`
- **URL:** `/api/v1/auth/register/`

### Parâmetros da Requisição

O corpo da requisição deve ser enviado no formato JSON e conter os seguintes campos:

- `name` (*string*): Nome completo do usuário.
- `email` (*string*): Endereço de e-mail do usuário.
- `password` (*string*): Senha escolhida pelo usuário.

Exemplo de corpo da requisição:

```json
{
  "name": "Nome Completo",
  "email": "usuario@example.com",
  "password": "SenhaSegura1#" // Único padão aceito
}
```
# Respostas
### Sucesso (Código 200)

Caso o registro seja bem-sucedido, a resposta será um JSON contendo:


- `message` (*string*): Mensagem indicando o sucesso.
- `user` (*integer*): ID do usuário registrado
- `statuscode` (*integer*): Código de status HTTP 200.

Exemplo de resposta de sucesso:

```json
{
  "message": "user registered",
  "statuscode": 200
}
```
## Erros
### E-mail Inválido (Código 400)

Caso o e-mail fornecido não seja válido, a resposta será um JSON contendo:

`message` (*string*): Mensagem indicando o motivo do erro.
`statuscode` (*integer*): Código de status HTTP 400.

Exemplo de resposta para e-mail inválido:
```json
{
  "message": "invalid email",
  "statuscode": 400
}
```
### Senha Fraca (Código 400)

Caso a senha fornecida não atenda aos critérios mínimos de segurança, a resposta será um JSON contendo:

`message` (*string*): Mensagem indicando o motivo do erro.
`statuscode` (*integer*): Código de status HTTP 400.

Exemplo de resposta para senha fraca:
```json
{
  "message": "weak password",
  "statuscode": 400
}
```
### Usuário Já Registrado (Código 400)

Caso o e-mail fornecido já tenha sido registrado, a resposta será um JSON contendo:

`message` (*string*): Mensagem indicando o motivo do erro.
`statuscode` (*integer*): Código de status HTTP 400.

Exemplo de resposta para usuário já registrado:
```json
{
  "message": "user already registered",
  "statuscode": 400
}
```
### Erro Interno no Servidor (Código 500)

Caso ocorra um erro interno no servidor durante o processo de registro, a resposta será um JSON contendo:

`message` (*string*): Mensagem indicando o motivo do erro.
`statuscode` (*integer*): Código de status HTTP 500.

Exemplo de resposta para erro interno:
```json
{
  "message": "error: Descrição do erro",
  "statuscode": 500
}
```

# Login de Usuário

Este endpoint é responsável por autenticar um usuário existente no sistema.

## Requisição

- **Método:** `POST`
- **URL:** `/api/v1/auth/login/`

### Parâmetros da Requisição

O corpo da requisição deve ser enviado no formato JSON e conter os seguintes campos:

- `email` (*string*): Endereço de e-mail do usuário.
- `password` (*string*): Senha do usuário.

Exemplo de corpo da requisição:

```json
{
  "email": "usuario@example.com",
  "password": "SenhaSegura123"
}
```
# Respostas

## Sucesso (Código 200)

Caso a autenticação seja bem-sucedida, a resposta será um JSON contendo:

```json
{
  "message": "user authenticated",
  "user_id": 1,
  "statuscode": 200
}
```
## Erros

### E-mail ou Senha Inválidos (Código 401)

Caso o e-mail ou a senha fornecidos sejam inválidos, a resposta será um JSON contendo:

```json
{
  "message": "authentication failed: Invalid email or password",
  "statuscode": 401
}
```
### Erro Interno no Servidor (Código 500)

Caso ocorra um erro interno no servidor durante o processo de autenticação, a resposta será um JSON contendo:

```json
{
  "message": "Internal server error",
  "statuscode": 500
}
```
Ah, entendi! Vou preparar a documentação para o endpoint `add()` da sua API de pacientes. Aqui está:

# Adicionar Paciente

Este endpoint permite adicionar um novo paciente ao sistema.

## Requisição

- **Método:** `POST`
- **URL:** `/api/v1/patient/add/`

### Parâmetros da Requisição

O corpo da requisição deve ser enviado no formato JSON e conter os seguintes campos:

- `dr_id` (*integer*): ID do médico responsável pelo paciente.
- `name` (*string*): Nome completo do paciente.
- `social_name` (*string*): Nome social do paciente.
- `cpf` (*string*): CPF do paciente.
- `age` (*integer*): Idade do paciente.
- `escort` (*boolean*): Indica se o paciente precisa de acompanhante.
- `email` (*string*): Endereço de e-mail do paciente.
- `date` (*string*): Data do agendamento.

Exemplo de corpo da requisição:

```json
{
  "dr_id": 123,
  "name": "Nome do Paciente",
  "social_name": "Nome Social do Paciente",
  "cpf": "123.456.789-00",
  "age": 30,
  "escort": true,
  "email": "paciente@example.com",
  "date": "2024-03-15"
}
```

### Respostas

#### Sucesso (Código 200)

Caso o paciente seja registrado com sucesso, a resposta será um JSON contendo:

- `message` (*string*): Mensagem indicando o sucesso.
- `user_id` (*integer*): ID do paciente registrado.
- `patient_id` (*integer*): ID do paciente.
- `schedule_id` (*integer*): ID do agendamento.
- `pwd` (*string*): Senha gerada para o paciente.
- `statuscode` (*integer*): Código de status HTTP 200.

Exemplo de resposta de sucesso:

```json
{
  "message": "patient registered successfully",
  "user_id": 1,
  "patient_id": 1,
  "schedule_id": 123,
  "pwd": "SenhaGerada1!",
  "statuscode": 200
}
```

#### Erros

- `missing required fields` (Código 400): Campos obrigatórios estão faltando no corpo da requisição.
- `invalid dr_id` (Código 400): ID do médico fornecido é inválido.
- `invalid email` (Código 400): O endereço de e-mail fornecido é inválido.
- `patient already exists` (Código 400): O paciente já está registrado no sistema.
- `busy schedule` (Código 400): O médico possui uma agenda ocupada na data especificada.
- `internal server error` (Código 500): Ocorreu um erro interno no servidor durante o processo de registro.

As mensagens de erro serão acompanhadas pelo código de status HTTP correspondente.
