# Criar o arquivo README.txt com as instruções para o setup do projeto
conteudo_readme = """
Sistema Hospitalar - Setup e Guia Inicial

Este projeto é um sistema básico para gestão hospitalar utilizando Python, SQLAlchemy e MySQL via Docker.

---

Requisitos
- Docker instalado  
- Python 3.7+ instalado  
- Ambiente virtual Python recomendado (venv)

---

Passo a Passo para Setup

1. Subir container MySQL com Docker
docker run --name mysql_hospital -e MYSQL_ROOT_PASSWORD=senha_segura -e MYSQL_DATABASE=hospital -p 3306:3306 -d mysql:latest

2. Verificar se o container está rodando
docker ps
Você deve ver o container mysql_hospital ativo e a porta 3306 exposta.

3. Conectar ao MySQL dentro do container para testes
docker exec -it mysql_hospital mysql -uroot -p
Digite a senha que escolheu, nossa senha é: 'endocKbOsIQU'.
No prompt MySQL, verifique o banco e tabelas:
USE hospital;
SHOW TABLES;

4. Criar ambiente virtual Python (opcional, mas recomendado)
No Linux/Mac:
python3 -m venv .venv
source .venv/bin/activate

No Windows PowerShell:
python -m venv .venv
.\\.venv\\Scripts\\activate

5. Instalar as dependências Python
pip install sqlalchemy pymysql cryptography
sqlalchemy — ORM para Python
pymysql — driver para conectar no MySQL
cryptography — suporte para autenticação segura com MySQL

6. Criar o arquivo models.py com os models
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    senha_hash = Column(String(128), nullable=False)
    nome_completo = Column(String(150), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_recepcionista = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(150), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    sexo = Column(String(1), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=True)
    tipo_sanguineo = Column(String(3), nullable=True)
    alergias_conhecidas = Column(String(255), nullable=True)

7. Criar o arquivo db.py para criar as tabelas no banco
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "mysql+pymysql://root:senha_segura@localhost:3306/hospital"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)
Substitua senha_segura pela senha configurada no MySQL.

8. Executar o script para criar as tabelas
python db.py
Se tudo estiver correto, você verá no terminal logs do SQL que indicam a criação das tabelas usuarios e pacientes.

9. Verificar as tabelas criadas no banco (opcional)
docker exec -it mysql_hospital mysql -uroot -p
Depois, no prompt MySQL:
USE hospital;
SHOW TABLES;
Deve listar as tabelas criadas.

Próximos passos recomendados
Criar funções para inserir, consultar, atualizar e deletar dados (CRUD).
Desenvolver interface de interação (linha de comando, web, etc).
Implementar autenticação de usuários e controle de permissões.
Adicionar validações e tratamentos de erro.
Documentar funcionalidades e possíveis melhorias.

Se precisar de ajuda para qualquer uma dessas etapas, estou à disposição para ajudar!

Contato
Criado por Elias Bariani Cardoso.
Email: elias23070038@aluno.cesupa.br
Discord: ebariani (Envie pedido de amizade se precisar de algo)
Data: 2025-05-24
"""

# Salvar o arquivo
caminho_arquivo = "/mnt/data/README.txt"
with open(caminho_arquivo, "w", encoding="utf-8") as f:
    f.write(conteudo_readme)

caminho_arquivo

# Recomeçar Docker, caso necessário (remover o volume persistente e recriar tudo)
docker-compose down -v (derrubar containers e remover volumes)
docker-compose up --build (subir o docker novamente)

# Aplica migrations com Alembic
alembic revision --autogenerate -m "(descricao)"
alembic upgrade head

# Acessar o banco MySQL (Atalho)
Liste os containers: docker ps
Acesse o terminal do container: docker exec -it nome_ou_id_do_container mysql -u seu_usuario -p
No nosso caso, isso é: docker exec -it mysql_hospital mysql -uroot -p
E nossa senha é: 'endocKbOsIQU'
Selecione o banco: USE hospital;



