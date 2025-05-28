
import pytest
from db import SessionLocal, engine
from models import Base, Paciente, Consulta, HistoricoPaciente, Usuario
from datetime import datetime
from servicos.cadastro_pacientes import inativar_paciente

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def session():
    s = SessionLocal()
    yield s
    s.rollback()
    s.close()

class FakeUsuario:
    def __init__(self, nome, nivel_acesso):
        self.nome = nome
        self.nivel_acesso = nivel_acesso

def test_inativar_paciente_sem_consulta(session, monkeypatch):
    # Criar paciente ativo
    p = Paciente(
        nome_completo="Paciente Teste",
        data_nascimento="1990-01-01",
        cpf="00000000000",
        sexo="F",
        telefone="12345-6789",
        status="Ativo"
    )
    session.add(p)
    session.commit()

    # Criar usuário admin simulado
    admin = FakeUsuario(nome="Admin Teste", nivel_acesso="Admin")

    # Simular input do motivo
    monkeypatch.setattr("builtins.input", lambda _: "Encerramento voluntário")

    # Executar função
    inativar_paciente(p.cpf, admin)

    # Recarregar paciente do banco
    paciente_inativo = session.query(Paciente).filter_by(cpf="00000000000").first()
    assert paciente_inativo.status == "Inativo"

    # Verificar histórico
    historico = session.query(HistoricoPaciente).filter_by(cpf_paciente=p.cpf).first()
    assert historico is not None
    assert historico.motivo == "Encerramento voluntário"
    assert historico.usuario_responsavel == "Admin Teste"
