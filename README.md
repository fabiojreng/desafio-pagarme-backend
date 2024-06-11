# Desafio Software Engineer, Back-end - Pagar.me

Sou Fábio da Silva Eloi Júnior e nesse desafio irei construir uma versão super simplificada de um Payment Service Provider (PSP) como o Pagar.me e talvez aprender um pouco mais sobre como funcionam pagamentos no Brasil.

[Link do repositório](https://github.com/pagarme/vagas/blob/master/desafios/software-engineer-backend)

## Contexto

Em sua essência um PSP tem duas funções muito importantes:

1. Permitir que nossos clientes processem transações ("cash-in")
2. Efetuar os pagamentos dos recebíveis para os nossos clientes ("cash-out")

No Pagar.me, nós temos duas entidades que representam essas informações:

- `transactions`: que representam as informações da compra, dados do cartão, valor, etc
- `payables`: que representam os recebíveis que pagaremos ao cliente

## Execução

1. **Pré-requisitos**:

   - Python3 & Pip.
   - MySQL.

2. **Passos**:
   - Instalar os pacotes necessários:
     ```bash
         pip install -r requirements.txt
     ```
   - Fazer a criação do DataBase e suas tabelas, no arquivo schema.sql.
   - Configurar o arquivo .env com as credenciais do DataBase.
   - Rodar o arquivo main.py
