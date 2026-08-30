# wsBackendFabricaDeSoftware26.2

API REST de biblioteca desenvolvida em Django para o Workshop de Backend — Fábrica de Software 26.2.

## Requisitos atendidos

- CRUD JSON completo de `Autor` e `Livro`, relacionados por chave estrangeira.
- Consulta à API pública Open Library para pesquisar obras por título, autor ou assunto.
- Tratamento de erros de entrada, timeout, indisponibilidade e resposta inválida da API externa.
- Arquivos obrigatórios: `.gitignore`, `requirements.txt` e este `README.md`.

## Execução

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

O projeto foi criado diretamente na raiz com `django-admin startproject config .`.

Endpoints da API:

```text
GET    /api/autores/
POST   /api/autores/
GET    /api/livros/
POST   /api/livros/
GET    /api/livros/{id}/
PUT    /api/livros/{id}/
DELETE /api/livros/{id}/
GET    /api/pesquisa-open-library/?q=machado+de+assis
```
