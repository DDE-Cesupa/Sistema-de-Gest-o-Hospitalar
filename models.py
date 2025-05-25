from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    senha_hash = Column(String(512), nullable=False)  # Armazena senha hasheada
    nome_completo = Column(String(150), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_recepcionista = Column(Boolean, default=False)
    is_medico = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(150), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)  # armazenar só números (11 dígitos)
    sexo = Column(String(1), nullable=False)  # 'M' para 'Masculino', 'F' para 'Feminino', 'O' para 'Outro'
    telefone = Column(String(20), nullable=False)

    email = Column(String(100), nullable=True)
    tipo_sanguineo = Column(String(3), nullable=True)  # Ex: 'A+', 'O-', etc
    alergias_conhecidas = Column(String(255), nullable=True)  # texto simples, lista separada por vírgulas
