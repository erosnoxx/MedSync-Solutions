# APIS - Registro de Usuário

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
  "password": "SenhaSegura1#",
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

# API - Login de Usuário

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
  "user": {
    "id": 123,
    "name": "Nome do Usuário",
    "email": "usuario@example.com"
    // Outros campos do usuário
  },
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

