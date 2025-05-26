import pytest
from db import SessionLocal, engine
from models import Base, Paciente, HistoricoPaciente
from servicos.cadastro_pacientes import atualizar_paciente_com_historico

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

def test_update_patient_history(session):
    # 1. Criar paciente inicial
    p = Paciente(
        nome_completo="Teste",
        data_nascimento="2000-01-01",
        cpf="12345678901",
        sexo="M",
        telefone="99999-0000"
    )
    session.add(p)
    session.commit()

    # 2. Atualizar telefone
    novos = {"telefone": "88888-1111", "versao": p.versao}
    atualizado = atualizar_paciente_com_historico(session, p.cpf, novos, usuario="tester")

    # 3. Verificar versão incrementada
    assert atualizado.versao == p.versao + 1

    # 4. Verificar histórico criado
    hist = session.query(HistoricoPaciente).filter_by(paciente_id=p.id).all()
    assert len(hist) == 1
    assert '"telefone": "99999-0000"' in hist[0].dados_anteriores
    assert '"telefone": "88888-1111"' in hist[0].dados_novos
