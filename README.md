# wsBackendFabricaDeSoftware26.2

Projeto de uma API REST de biblioteca, criado para o Workshop de Backend — Fábrica de Software 26.2.

O sistema permite cadastrar autores e livros, além de pesquisar livros em uma API externa chamada Open Library.

## O que este projeto possui

- CRUD completo de autores e livros. CRUD significa criar, consultar, atualizar e excluir dados.
- Relação entre as entidades: cada livro pertence a um autor.
- Consulta à API externa gratuita Open Library.
- Tratamento de erros quando a consulta externa não recebe um termo, demora ou fica indisponível.
- Swagger para visualizar e testar a API pelo navegador.
- Arquivos obrigatórios: `.gitignore`, `requirements.txt` e este `README.md`.

## Antes de começar

Você precisa ter o Python instalado. Para conferir, abra o PowerShell e execute:

```powershell
python --version
```

Também abra o terminal dentro da pasta do projeto:

```powershell
cd "C:\Users\caioa\OneDrive\Documentos\GitHub\wsBackendFabricaDeSoftware26.2"
```

## Passo a passo para executar

### 1. Ativar o ambiente virtual

O ambiente virtual (`venv`) mantém as bibliotecas deste projeto separadas das demais bibliotecas do computador.

No PowerShell, execute:

```powershell
.\venv\Scripts\Activate.ps1
```

Se funcionar, o terminal mostrará `(venv)` no começo da linha.

> Se o PowerShell bloquear o script, execute uma vez: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` e tente o comando novamente.

### 2. Instalar as dependências

As dependências são bibliotecas necessárias para o projeto funcionar. O arquivo `requirements.txt` lista todas elas.

```powershell
pip install -r requirements.txt
```

### 3. Preparar o banco de dados

Este comando cria e atualiza as tabelas usadas pelo projeto no banco SQLite local.

```powershell
python manage.py migrate
```

### 4. Iniciar o servidor

```powershell
python manage.py runserver
```

O terminal deverá mostrar um endereço semelhante a `http://127.0.0.1:8000/`. Enquanto esse terminal estiver aberto, a API estará funcionando.

Se a porta 8000 estiver ocupada, use outra porta, por exemplo:

```powershell
python manage.py runserver 8001
```

Nesse caso, troque `8000` por `8001` em todos os endereços mostrados abaixo.

Para parar o servidor, pressione `Ctrl + C` no terminal.

## Como testar pelo navegador: Swagger

Com o servidor ligado, abra:

```text
http://127.0.0.1:8000/api/docs/
```

Essa página é o Swagger: uma documentação visual que permite consultar e testar os endpoints sem usar comandos no terminal. Clique em uma rota, depois em **Try it out**, preencha os dados e use **Execute**.

O endereço abaixo é o schema OpenAPI. Ele é o arquivo técnico que descreve as rotas e é usado pelo Swagger para construir a documentação:

```text
http://127.0.0.1:8000/api/schema/
```

## Endpoints disponíveis

| Endereço | O que faz |
| --- | --- |
| `GET /api/autores/` | Lista todos os autores. |
| `POST /api/autores/` | Cria um autor. |
| `GET /api/autores/{id}/` | Consulta um autor pelo identificador. |
| `PUT /api/autores/{id}/` | Atualiza um autor. |
| `DELETE /api/autores/{id}/` | Exclui um autor. |
| `GET /api/livros/` | Lista todos os livros. |
| `POST /api/livros/` | Cria um livro. |
| `GET /api/livros/{id}/` | Consulta um livro pelo identificador. |
| `PUT /api/livros/{id}/` | Atualiza um livro. |
| `DELETE /api/livros/{id}/` | Exclui um livro. |
| `GET /api/pesquisa-open-library/?q=termo` | Pesquisa livros na Open Library. |

`{id}` significa o número identificador de um registro. Por exemplo, para acessar o livro de identificador 1: `http://127.0.0.1:8000/api/livros/1/`.

## Exemplo completo usando o Swagger

1. Abra `http://127.0.0.1:8000/api/docs/`.
2. Abra a rota `POST /api/autores/`.
3. Clique em **Try it out** e use este JSON:

```json
{
  "nome": "Machado de Assis",
  "biografia": "Escritor brasileiro."
}
```

4. Clique em **Execute**. A resposta trará o `id` do autor criado, por exemplo `1`.
5. Abra a rota `POST /api/livros/`, clique em **Try it out** e use o `id` do autor no campo `autor`:

```json
{
  "titulo": "Dom Casmurro",
  "sinopse": "Romance brasileiro.",
  "isbn": "9788508150167",
  "ano_publicacao": 1899,
  "autor": 1
}
```

6. Para pesquisar obras fora do seu banco de dados, abra no navegador:

```text
http://127.0.0.1:8000/api/pesquisa-open-library/?q=machado+de+assis
```

## API externa: Open Library

A Open Library é uma API pública de livros. Ela não exige cadastro nem chave de acesso. O projeto envia o termo informado em `q` para a Open Library e retorna título, autores, ano de publicação e ISBN dos resultados encontrados.

Caso não seja informado o parâmetro `q`, a API retorna o código `400`. Se a Open Library demorar demais, retorna `504`; se estiver indisponível ou responder de forma inválida, retorna `502`.

## Estrutura do projeto

- `config/`: configurações principais do Django e URLs gerais.
- `catalogo/`: aplicação de biblioteca, com modelos, rotas, serializers, views e testes.
- `catalogo/models.py`: define as tabelas `Autor` e `Livro`.
- `catalogo/serializers.py`: transforma os dados em JSON.
- `catalogo/views.py`: contém a lógica dos endpoints e a integração externa.
- `catalogo/urls.py`: define as URLs da API.
- `requirements.txt`: lista as bibliotecas necessárias.
- `.gitignore`: evita enviar arquivos locais, como `venv` e `__pycache__`, ao GitHub.

## Como validar o projeto

Com o ambiente virtual ativado, execute:

```powershell
python manage.py check
python manage.py test
```

O primeiro comando verifica erros de configuração. O segundo executa os testes automatizados do projeto.
