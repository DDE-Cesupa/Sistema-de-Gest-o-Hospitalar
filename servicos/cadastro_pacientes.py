from db import SessionLocal
from models import Paciente

def consultar_cpf(cpf):
    session = SessionLocal()
    try:
        paciente = session.query(Paciente).filter_by(cpf=cpf).first()
        if paciente:
            print("CPF já cadastrado. Interrompendo o cadastro...")
            return paciente
        else:
            print('\nCPF válido, prosseguindo com o cadastro...\n')
            return None
    except Exception as e:
        session.rollback()
        print(f"Erro ao consultar CPF: {e}")
    finally:
        session.close()

        

#def cadastrar_paciente(nome_completo, data_nascimento, cpf, sexo, telefone, email=None, tipo_sanguineo=None, alergias_conhecidas=None):
    
    