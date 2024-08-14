# Tech Challenge FIAP - 8SOAT

## Descrição

Este é um projeto de desenvolvimento de um sistema backend para autoatendimento e gerenciamento de pedidos para um fastfood utilizando DDD e Arquitetura Hexagonal.

## DDD

Segue o link do Miro com os diagramas e documentação do sistema: [Link](https://miro.com/app/board/uXjVKr2Jyo4=/?share_link_id=255249241481)

## Tecnologias Usadas

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework para construção de APIs.
- **Poetry**: Ferramenta para gerenciamento de dependências.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional.
- **SQLAlchemy**: ORM para interação com o banco de dados.
- **Alembic**: Ferramenta para migrações de banco de dados.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte maneira:

## Instalação e uso (local)

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/gabrielslotti/food-autoservice.git
    cd food-autoservice
    ```

2. **Instale o Poetry:**

    Siga as instruções da [documentação oficial do Poetry para instalação da ferramenta](https://python-poetry.org/docs/#installing-with-the-official-installer). Mas para exemplo utilizando o `pip` podemos executar o seguinte comando:
    ```bash
    pip install poetry
    ```

2. **Crie e ative um ambiente virtual**:
    ```bash
    poetry shell
    ```
    Ou
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Ou utilize o comando `poetry shell`
    ```

3. **Instale as dependências**:

    ```bash
    poetry install
    ```

4. **Configure o arquivo para migração no banco de dados**:

    Altere no arquivo `alembic.ini` que está na raiz do projeto o campo `sqlalchemy.url` com as configs do seu banco:

    ```ini
    sqlalchemy.url=postgresql://usuario:senha@localhost:5432/meu_banco
    ```

5. **Aplique as migrações**:

    ```bash
    poetry alembic upgrade head
    ```

6. **Configurar variáveis de ambiente:**
    Crie um arquivo `.env` na raíz do projeto e adicione as seguintes variáveis:

    ```env
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=postgres
    DB_PASS=postgres
    DB_BASE=food
    ```


7. **Inicie o servidor FastAPI**:

    ```bash
    poetry run python src/main.py
    ```

    O servidor estará rodando em `http://localhost:8000`.

8. **Acesse a documentação da API**:

    Acesse a documentação (Swagger) da API em `http://localhost:8000/docs`.


## Instalação e uso (docker)

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/gabrielslotti/food-autoservice.git
    cd food-autoservice
    ```

1. **Execute o docker compose**:

    ```bash
    docker compose up
    ```

    Este comando irá subir dois containers docker, um rodando nosso app (API) e outro rodando o banco de dados Postgres.
