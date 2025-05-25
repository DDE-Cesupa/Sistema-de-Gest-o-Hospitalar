from werkzeug.security import check_password_hash, generate_password_hash
from db import SessionLocal
from models import Usuario

def autenticar_usuario(email, senha):
    session = SessionLocal()
    try:
        usuario = session.query(Usuario).filter_by(email=email).first()
        if usuario and check_password_hash(usuario.senha_hash, senha):
            return usuario
        return None
    finally:
        session.close()

def cadastrar_usuario(usuario_logado, nome, email, senha, username, is_recepcionista=False, is_admin=False):
    if not usuario_logado or not usuario_logado.is_admin:
        print("Acesso negado: apenas administradores podem cadastrar novos usuários.")
        return

    session = SessionLocal()
    try:
        if session.query(Usuario).filter_by(email=email).first():
            print("Erro: email já cadastrado.")
            return
        if session.query(Usuario).filter_by(username=username).first():
            print("Erro: username já existe.")
            return

        senha_hash = generate_password_hash(senha)
        novo_usuario = Usuario(
            nome_completo=nome,
            email=email,
            senha_hash=senha_hash,
            username=username,
            is_admin=is_admin,
            is_recepcionista=is_recepcionista
        )
        session.add(novo_usuario)
        session.commit()
        print(f"Usuário '{username}' cadastrado com sucesso.")
    finally:
        session.close()


