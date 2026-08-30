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

## Documentação Swagger

Com o servidor em execução, abra `http://127.0.0.1:8000/api/docs/` para visualizar e testar os endpoints pela interface Swagger. O schema OpenAPI também está disponível em `http://127.0.0.1:8000/api/schema/`.

## Exemplos de uso

Com o servidor em execução, a API estará disponível em `http://127.0.0.1:8000/api/`.

### Criar um autor

```powershell
curl.exe -X POST http://127.0.0.1:8000/api/autores/ `
  -H "Content-Type: application/json" `
  -d "{\"nome\":\"Machado de Assis\",\"biografia\":\"Escritor brasileiro.\"}"
```

### Criar um livro

Substitua `1` pelo identificador de um autor já cadastrado.

```powershell
curl.exe -X POST http://127.0.0.1:8000/api/livros/ `
  -H "Content-Type: application/json" `
  -d "{\"titulo\":\"Dom Casmurro\",\"sinopse\":\"Romance brasileiro.\",\"isbn\":\"9788508150167\",\"ano_publicacao\":1899,\"autor\":1}"
```

### Listar e atualizar livros

```powershell
curl.exe http://127.0.0.1:8000/api/livros/

curl.exe -X PUT http://127.0.0.1:8000/api/livros/1/ `
  -H "Content-Type: application/json" `
  -d "{\"titulo\":\"Dom Casmurro\",\"sinopse\":\"Romance brasileiro.\",\"isbn\":\"9788508150167\",\"ano_publicacao\":1899,\"autor\":1}"
```

### Excluir um livro

```powershell
curl.exe -X DELETE http://127.0.0.1:8000/api/livros/1/
```

### Consultar a API externa

```powershell
curl.exe "http://127.0.0.1:8000/api/pesquisa-open-library/?q=machado+de+assis"
```

A consulta à Open Library não exige chave de API. Em caso de termo ausente, demora ou indisponibilidade da API externa, a aplicação retorna respostas JSON com os códigos HTTP `400`, `504` ou `502`, respectivamente.
