# opencredz-back-python

Este repositório contém o backend da aplicação OpenCredz, desenvolvido em Python utilizando o framework FastAPI. Ele é responsável por gerenciar as credenciais e a lógica de negócios da plataforma.

## Sumário

1.  [Visão Geral do Projeto](#visão-geral-do-projeto)
2.  [Pré-requisitos](#pré-requisitos)
3.  [Configuração do Ambiente de Desenvolvimento](#configuração-do-ambiente-de-desenvolvimento)
    *   [Instalação do Python](#instalação-do-python)
        *   [Windows](#windows)
        *   [macOS](#macos)
    *   [Instalação do PostgreSQL](#instalação-do-postgresql)
        *   [Windows](#windows-1)
        *   [macOS](#macos-1)
4.  [Configuração do Projeto](#configuração-do-projeto)
    *   [Clonando o Repositório](#clonando-o-repositório)
    *   [Configurando o Ambiente Virtual](#configurando-o-ambiente-virtual)
    *   [Variáveis de Ambiente](#variáveis-de-ambiente)
    *   [Executando as Migrações do Banco de Dados](#executando-as-migrações-do-banco-de-dados)
5.  [Executando a Aplicação](#executando-a-aplicação)
6.  [Testes](#testes)
7.  [Estrutura do Projeto](#estrutura-do-projeto)
8.  [Contribuição](#contribuição)
9.  [Licença](#licença)

## 1. Visão Geral do Projeto

O `opencredz-back-python` é o serviço de backend que sustenta a plataforma OpenCredz. Ele é construído com FastAPI, uma estrutura web moderna e de alto desempenho para a construção de APIs com Python 3.7+. A aplicação utiliza PostgreSQL como banco de dados para persistência de dados e `SQLAlchemy` como ORM para interagir com o banco de dados. A autenticação é gerenciada através de tokens JWT.

## 2. Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes softwares instalados em sua máquina:

*   **Python 3.x**: Versão 3.8 ou superior é recomendada.
*   **PostgreSQL**: Um sistema de gerenciamento de banco de dados relacional.
*   **Git**: Para clonar o repositório.

As seções a seguir detalham a instalação do Python e do PostgreSQL para sistemas operacionais Windows e macOS.



### Instalação do Python

#### Windows

Para instalar o Python no Windows, siga os passos abaixo:

1.  **Baixe o Instalador**: Acesse o site oficial do Python em [python.org](https://www.python.org/downloads/windows/) e baixe a versão mais recente do instalador para Windows (geralmente o instalador executável de 64 bits).
2.  **Execute o Instalador**: Execute o arquivo `.exe` baixado.
3.  **Adicionar Python ao PATH**: **Muito importante**: Na primeira tela do instalador, certifique-se de marcar a caixa "Add Python X.Y to PATH" (onde X.Y é a versão do Python). Isso permitirá que você execute o Python a partir de qualquer diretório no Prompt de Comando ou PowerShell.
4.  **Instalação Personalizada (Opcional)**: Você pode escolher "Install Now" para uma instalação padrão ou "Customize installation" para selecionar componentes específicos e o diretório de instalação.
5.  **Concluir a Instalação**: Siga as instruções na tela para concluir a instalação.
6.  **Verificar a Instalação**: Abra o Prompt de Comando (CMD) ou PowerShell e digite `python --version` e `pip --version`. Você deverá ver as versões instaladas do Python e do pip, respectivamente.

```bash
python --version
pip --version
```

#### macOS

O macOS geralmente vem com uma versão pré-instalada do Python, mas é recomendável instalar uma versão mais recente e gerenciá-la com ferramentas como `pyenv` ou diretamente via Homebrew para evitar conflitos com o sistema. Aqui estão as opções:

##### Opção 1: Usando Homebrew (Recomendado)

1.  **Instalar Homebrew**: Se você ainda não tem o Homebrew, abra o Terminal e execute o seguinte comando:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

    Siga as instruções na tela para concluir a instalação do Homebrew.
2.  **Instalar Python**: Com o Homebrew instalado, você pode instalar a versão mais recente do Python com:

    ```bash
    brew install python
    ```

3.  **Verificar a Instalação**: Após a instalação, verifique a versão do Python e do pip:

    ```bash
    python3 --version
    pip3 --version
    ```

    O Homebrew geralmente cria links simbólicos para `python3` e `pip3`.

##### Opção 2: Baixando o Instalador Oficial

1.  **Baixe o Instalador**: Acesse o site oficial do Python em [python.org](https://www.python.org/downloads/macos/) e baixe o instalador `.pkg` para macOS.
2.  **Execute o Instalador**: Execute o arquivo `.pkg` e siga as instruções na tela.
3.  **Verificar a Instalação**: Abra o Terminal e digite `python3 --version` e `pip3 --version` para verificar se a instalação foi bem-sucedida.

É crucial que a versão do Python utilizada seja consistente em todo o ambiente de desenvolvimento. Recomenda-se o uso de ambientes virtuais para isolar as dependências do projeto.



### Instalação do PostgreSQL

#### Windows

Para instalar o PostgreSQL no Windows, o método mais comum é usar o instalador interativo fornecido pela EnterpriseDB:

1.  **Baixe o Instalador**: Acesse a página de downloads do PostgreSQL da EnterpriseDB em [PostgreSQL Downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) e selecione a versão mais recente para Windows.
2.  **Execute o Instalador**: Execute o arquivo `.exe` baixado. O assistente de instalação o guiará através do processo.
3.  **Selecione Componentes**: Durante a instalação, você pode escolher quais componentes instalar. Certifique-se de incluir:
    *   **PostgreSQL Server**: O servidor de banco de dados principal.
    *   **pgAdmin 4**: Uma ferramenta gráfica para gerenciar seus bancos de dados PostgreSQL.
    *   **Stack Builder**: Uma ferramenta para baixar e instalar ferramentas e drivers adicionais (opcional, mas útil).
4.  **Defina a Senha do Superusuário**: Você será solicitado a definir uma senha para o usuário `postgres` (o superusuário do banco de dados). **Anote esta senha**, pois ela será necessária para acessar o banco de dados.
5.  **Defina a Porta**: A porta padrão para o PostgreSQL é `5432`. Você pode alterá-la se houver conflitos, mas é recomendado manter a padrão.
6.  **Local de Dados**: Escolha um diretório para armazenar os dados do banco de dados.
7.  **Concluir a Instalação**: Siga as instruções restantes para finalizar a instalação.
8.  **Verificar a Instalação**: Após a instalação, você pode abrir o `pgAdmin 4` e tentar se conectar ao servidor local (`localhost:5432`) usando o usuário `postgres` e a senha que você definiu.

#### macOS

No macOS, você tem algumas opções para instalar o PostgreSQL. A mais recomendada é via Homebrew, mas também há instaladores gráficos.

##### Opção 1: Usando Homebrew (Recomendado)

1.  **Instalar PostgreSQL**: Se você já tem o Homebrew instalado (conforme as instruções de Python), abra o Terminal e execute:

    ```bash
    brew install postgresql
    ```

2.  **Iniciar o Serviço PostgreSQL**: Para iniciar o servidor PostgreSQL, você pode usar:

    ```bash
    brew services start postgresql
    ```

    Para que o PostgreSQL inicie automaticamente no login, use:

    ```bash
    brew services enable postgresql
    ```

3.  **Criar um Usuário e Banco de Dados (Opcional)**: Por padrão, o Homebrew cria um usuário `postgres` que corresponde ao seu usuário macOS. Você pode criar um banco de dados para o seu projeto:

    ```bash
    createdb opencredz
    ```

    Se você precisar de um usuário diferente, pode criá-lo com:

    ```bash
    createuser --interactive
    ```

4.  **Verificar a Instalação**: Você pode se conectar ao banco de dados usando o cliente `psql`:

    ```bash
    psql postgres
    ```

    Para sair, digite `\q` e pressione Enter.

##### Opção 2: Usando o Instalador Gráfico (Postgres.app)

O [Postgres.app](https://postgresapp.com/) é uma maneira fácil de instalar e executar o PostgreSQL no macOS:

1.  **Baixe o Postgres.app**: Acesse o site oficial e baixe a versão mais recente.
2.  **Arraste para Aplicativos**: Arraste o arquivo `Postgres.app` para a pasta `Applications`.
3.  **Inicie o Postgres.app**: Abra o aplicativo. Ele aparecerá na barra de menus. Clique em "Start" para iniciar o servidor PostgreSQL.
4.  **Configure o PATH (Opcional)**: Para usar os comandos `psql`, `createdb`, etc., no Terminal, você pode adicionar o diretório binário do Postgres.app ao seu PATH. As instruções estão disponíveis no site do Postgres.app.

Com o PostgreSQL instalado, você estará pronto para configurar o banco de dados para o projeto OpenCredz.



## 4. Configuração do Projeto

### Clonando o Repositório

Para começar, clone o repositório para sua máquina local usando Git:

```bash
git clone https://github.com/vinimw/opencredz-back-python.git
cd opencredz-back-python
```

### Configurando o Ambiente Virtual

É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto e evitar conflitos com outras instalações Python em seu sistema. Siga os passos:

1.  **Crie o Ambiente Virtual**: No diretório raiz do projeto, execute:

    ```bash
    python -m venv venv
    ```

    Isso criará uma pasta `venv` contendo o ambiente virtual.

2.  **Ative o Ambiente Virtual**:

    *   **Windows (Prompt de Comando/PowerShell)**:

        ```bash
        .\venv\Scripts\activate
        ```

    *   **macOS/Linux (Bash/Zsh)**:

        ```bash
        source venv/bin/activate
        ```

    Você saberá que o ambiente virtual está ativo quando `(venv)` aparecer no início da linha de comando.

3.  **Instale as Dependências**: Com o ambiente virtual ativo, instale todas as dependências do projeto listadas no `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

    As dependências são:

    *   `fastapi`: O framework web para construção da API.
    *   `uvicorn`: Um servidor ASGI para rodar a aplicação FastAPI.
    *   `psycopg2-binary`: Adaptador PostgreSQL para Python.
    *   `python-multipart`: Necessário para lidar com formulários (e.g., upload de arquivos).
    *   `pydantic[email]`: Para validação de dados, incluindo validação de e-mail.
    *   `sqlalchemy`: ORM (Object Relational Mapper) para interagir com o banco de dados.
    *   `python-jose[cryptography]`: Para manipulação de JWT (JSON Web Tokens).
    *   `passlib[bcrypt]`: Para hashing de senhas.
    *   `pydantic-settings`: Para gerenciar configurações e variáveis de ambiente.

### Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para configurações sensíveis e específicas do ambiente (como credenciais de banco de dados e chaves secretas). Você precisará criar um arquivo `.env` na raiz do projeto. Este arquivo **não deve ser versionado** (ele já está no `.gitignore`).

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```dotenv
ENV=development
DATABASE_URL=postgresql://viniciusweber:q1w2e3@localhost/opencredz
SECRET_KEY=local-AYIHJKG!@F
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=300
```

**Explicação das Variáveis:**

*   `ENV`: Define o ambiente da aplicação (e.g., `development`, `production`).
*   `DATABASE_URL`: A URL de conexão com o banco de dados PostgreSQL. Certifique-se de substituir `viniciusweber:q1w2e3` pelo seu usuário e senha do PostgreSQL, e `opencredz` pelo nome do banco de dados que você criou ou deseja usar.
*   `SECRET_KEY`: Uma chave secreta forte usada para assinar tokens JWT. **Em produção, esta chave deve ser gerada de forma segura e mantida em segredo.**
*   `ALGORITHM`: O algoritmo de criptografia usado para os tokens JWT (e.g., `HS256`).
*   `ACCESS_TOKEN_EXPIRE_MINUTES`: Tempo de expiração dos tokens de acesso em minutos.

### Executando as Migrações do Banco de Dados

Após configurar o banco de dados PostgreSQL e as variáveis de ambiente, você precisará executar as migrações para criar as tabelas necessárias no banco de dados. O projeto provavelmente utiliza `Alembic` ou uma ferramenta similar para migrações. Assumindo que as migrações estão configuradas, execute:

```bash
# Certifique-se de que o ambiente virtual está ativo
# e que o PostgreSQL está rodando

# Exemplo de comando para rodar migrações (pode variar dependendo da ferramenta)
# alembic upgrade head

# Se o projeto usa um script customizado para migrações, ele deve ser executado aqui.
# Verifique a documentação interna do projeto para o comando exato de migração.
```

**Nota**: O comando exato para executar as migrações pode variar. Consulte a documentação específica do projeto (se houver) ou o código-fonte para identificar o script ou comando correto. Geralmente, frameworks como FastAPI com SQLAlchemy usam Alembic para gerenciar migrações de banco de dados.



## 5. Executando a Aplicação

Com todas as dependências instaladas e o banco de dados configurado, você pode iniciar a aplicação FastAPI. Certifique-se de que seu ambiente virtual esteja ativo.

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Explicação do Comando:**

*   `uvicorn`: O servidor ASGI que executa a aplicação.
*   `app.main:app`: Indica que a aplicação FastAPI (`app`) está localizada no módulo `main.py` dentro do pacote `app`.
*   `--reload`: Habilita o recarregamento automático do servidor quando há alterações no código-fonte (ótimo para desenvolvimento).
*   `--host 0.0.0.0`: Faz com que o servidor escute em todas as interfaces de rede disponíveis, tornando-o acessível de outras máquinas na mesma rede (se o firewall permitir). Para acesso apenas local, você pode usar `--host 127.0.0.1` ou `--host localhost`.
*   `--port 8000`: Define a porta na qual a aplicação será executada. Você pode acessar a API em `http://localhost:8000`.

Após iniciar o servidor, você pode acessar a documentação interativa da API (Swagger UI) em `http://localhost:8000/docs` e a documentação alternativa (ReDoc) em `http://localhost:8000/redoc`.



## 6. Testes

Para executar os testes automatizados do projeto, certifique-se de que todas as dependências de desenvolvimento (incluindo `pytest` ou outras bibliotecas de teste) estejam instaladas. Geralmente, os testes podem ser executados com um comando como:

```bash
pytest
```

Consulte o diretório `tests/` (se existir) para entender a estrutura dos testes e quaisquer configurações adicionais necessárias.

## 7. Estrutura do Projeto

A estrutura do projeto `opencredz-back-python` segue uma organização modular para facilitar o desenvolvimento e a manutenção. Embora a estrutura exata possa variar, uma organização típica para aplicações FastAPI com SQLAlchemy pode incluir:

```
opencredz-back-python/
├── app/
│   ├── __init__.py
│   ├── main.py             # Ponto de entrada da aplicação FastAPI
│   ├── api/                # Módulos para endpoints da API (e.g., users, auth, credentials)
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── endpoints/  # Arquivos para cada recurso/endpoint (e.g., users.py, auth.py)
│   │       └── deps.py     # Dependências comuns (e.g., autenticação, conexão DB)
│   ├── core/               # Configurações, constantes, segurança
│   │   ├── config.py
│   │   └── security.py
│   ├── crud/               # Operações CRUD (Create, Read, Update, Delete) para o DB
│   │   └── __init__.py
│   ├── db/                 # Configuração do banco de dados e modelos SQLAlchemy
│   │   ├── __init__.py
│   │   ├── base.py         # Base declarativa para modelos
│   │   ├── session.py      # Configuração da sessão do DB
│   │   └── models/         # Definição dos modelos de dados (e.g., user.py, credential.py)
│   ├── schemas/            # Modelos Pydantic para validação de entrada/saída da API
│   │   └── __init__.py
│   └── services/           # Lógica de negócios complexa, serviços auxiliares
├── alembic/                # Diretório para migrações do banco de dados (se usado Alembic)
│   ├── versions/
│   └── env.py
├── .env.example            # Exemplo de arquivo de variáveis de ambiente (não versionado)
├── .gitignore              # Arquivo para ignorar arquivos e diretórios no Git
├── requirements.txt        # Dependências do projeto Python
├── README.md               # Este arquivo
└── Dockerfile              # (Opcional) Para conteinerização com Docker
```

## 8. Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para o projeto, por favor, siga estas diretrizes:

1.  Faça um fork do repositório.
2.  Crie uma nova branch para sua feature (`git checkout -b feature/sua-feature`).
3.  Faça suas alterações e teste-as.
4.  Certifique-se de que seu código segue os padrões de estilo do projeto.
5.  Faça commit de suas alterações (`git commit -m 'feat: Adiciona nova feature'`).
6.  Envie para a branch original (`git push origin feature/sua-feature`).
7.  Abra um Pull Request descrevendo suas alterações.

## 9. Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` na raiz do repositório para mais detalhes.

---

**Desenvolvido por Manus AI**

