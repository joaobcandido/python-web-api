# python-web-api

Este repositório agora inclui uma API Django pronta para deploy e testes locais via Docker.

## Como executar localmente

1. Construa a imagem:
   `docker compose build`

2. Inicie o serviço:
   `docker compose up`

3. Verifique endpoints:
   - `http://localhost:8000/api/` (health)
   - `http://localhost:8000/api/ping/`
   - `http://localhost:8000/api/hello/?name=SeuNome`

## Testes Django

`docker compose run --rm web python manage.py test`

## Observações

- O projeto Django está em `api/`.
- O banco de dados local será `api/db.sqlite3`.
