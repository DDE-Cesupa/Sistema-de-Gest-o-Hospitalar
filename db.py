import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
<<<<<<< HEAD
from models import Base, Usuario
=======
from models import Base, Usuario, Paciente, HistoricoPaciente
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

<<<<<<< HEAD
DATABASE_URL = "mysql+pymysql://root:endocKbOsIQU@localhost:3306/hospital"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

=======
# URL de conexão (MySQL no Docker)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:endocKbOsIQU@localhost:3306/hospital"
)
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

# Cria todas as tabelas (incluindo novas)
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
Base.metadata.create_all(bind=engine)

def criar_admin_inicial():
    session = SessionLocal()
    try:
        admin_existente = session.query(Usuario).filter_by(is_admin=True).first()
        if not admin_existente:
            admin = Usuario(
                username=os.getenv("ADMIN_USERNAME"),
                senha_hash=generate_password_hash(os.getenv("ADMIN_PASSWORD")),
                nome_completo="Administrador Padrão",
                email=os.getenv("ADMIN_EMAIL"),
                is_admin=True,
                is_recepcionista=False,
<<<<<<< HEAD
                is_medico = True 
=======
                is_medico=True
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
            )
            session.add(admin)
            session.commit()
            print("✅ Usuário admin criado com sucesso.")
        else:
            print("ℹ️ Usuário admin já existe.")
    except Exception as e:
        session.rollback()
        print(f"Erro ao criar admin: {e}")
    finally:
        session.close()

<<<<<<< HEAD
=======

>>>>>>> 5d35a02 (Implementação do caso de uso 3)
def criar_recepcionista_inicial():
    session = SessionLocal()
    try:
        recepcionista_existente = session.query(Usuario).filter_by(is_recepcionista=True).first()
        if not recepcionista_existente:
            recepcionista = Usuario(
<<<<<<< HEAD
                username="recepcionista",
                senha_hash=generate_password_hash('12345'),
                nome_completo="RECEPCIONISTA PADRÃO",
                email="joão@hospital.com",
                is_admin=False,
                is_medico=True,
=======
                username=os.getenv("RECEP_USERNAME", "recepcionista"),
                senha_hash=generate_password_hash(os.getenv("RECEP_PASSWORD", "12345")),
                nome_completo="Recepcionista Padrão",
                email=os.getenv("RECEP_EMAIL", "recepcionista@hospital.com"),
                is_admin=False,
                is_medico=False,
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
                is_recepcionista=True
            )
            session.add(recepcionista)
            session.commit()
            print("✅ Usuário recepcionista criado com sucesso.")
        else:
            print("ℹ️ Usuário recepcionista já existe.")
    except Exception as e:
        session.rollback()
        print(f"Erro ao criar recepcionista: {e}")
    finally:
        session.close()

<<<<<<< HEAD
=======

>>>>>>> 5d35a02 (Implementação do caso de uso 3)
if __name__ == "__main__":
    criar_admin_inicial()
    criar_recepcionista_inicial()
