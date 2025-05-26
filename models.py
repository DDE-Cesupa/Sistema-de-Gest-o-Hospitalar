<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base
=======
from sqlalchemy import Column, Integer, String, Date, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
>>>>>>> 5d35a02 (Implementação do caso de uso 3)

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
<<<<<<< HEAD
    senha_hash = Column(String(512), nullable=False)  # Armazena senha hasheada
=======
    senha_hash = Column(String(512), nullable=False)
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
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
<<<<<<< HEAD
    cpf = Column(String(11), unique=True, nullable=False)  # armazenar só números (11 dígitos)
    sexo = Column(String(1), nullable=False)  # 'M' para 'Masculino', 'F' para 'Feminino', 'O' para 'Outro'
    telefone = Column(String(20), nullable=False)

    email = Column(String(100), nullable=True)
    tipo_sanguineo = Column(String(3), nullable=True)  # Ex: 'A+', 'O-', etc
    alergias_conhecidas = Column(String(255), nullable=True)  # texto simples, lista separada por vírgulas
=======
    cpf = Column(String(11), unique=True, nullable=False)
    sexo = Column(String(1), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=True)
    tipo_sanguineo = Column(String(3), nullable=True)
    alergias_conhecidas = Column(String(255), nullable=True)

    versao = Column(Integer, nullable=False, default=0)
    historicos = relationship("HistoricoPaciente", back_populates="paciente")

class HistoricoPaciente(Base):
    __tablename__ = 'historico_paciente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'), nullable=False)
    alterado_por = Column(String(150), nullable=False)
    data_alteracao = Column(DateTime, default=func.now())
    dados_anteriores = Column(Text, nullable=False)
    dados_novos = Column(Text, nullable=False)

    paciente = relationship("Paciente", back_populates="historicos")
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
