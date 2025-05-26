# sistema_hospital/consultarUsuario.py

import os
from db import SessionLocal
from models import Paciente

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def buscar_por_nome(termo: str):
    session = SessionLocal()
    try:
        return session.query(Paciente).\
            filter(Paciente.nome_completo.ilike(f"%{termo}%")).all()
    finally:
        session.close()

def buscar_por_cpf(termo: str):
    session = SessionLocal()
    try:
        return session.query(Paciente).\
            filter(Paciente.cpf == termo).all()
    finally:
        session.close()

def buscar_por_id(pid: int):
    session = SessionLocal()
    try:
        p = session.query(Paciente).get(pid)
        return [p] if p else []
    finally:
        session.close()

def exibir_detalhes(paciente: Paciente):
    limpar_tela()
    print("=== Detalhes do Paciente ===")
    print(f"ID: {paciente.id}")
    print(f"Nome completo: {paciente.nome_completo}")
    print(f"CPF: {paciente.cpf}")
    print(f"Nascimento: {paciente.data_nascimento}")
    print(f"Sexo: {paciente.sexo or 'N/A'}")
    print(f"Telefone: {paciente.telefone or 'N/A'}")
    print(f"Endereço: {paciente.endereco or 'N/A'}")
    print(f"E-mail: {paciente.email or 'N/A'}")
    print(f"Tipo sanguíneo: {paciente.tipo_sanguineo or 'N/A'}")
    print(f"Alergias: {paciente.alergias_conhecidas or 'N/A'}")
    input("\nPressione Enter para voltar…")

def consultar_paciente():
    limpar_tela()
    print("=== Consulta de Paciente ===")
    print("1) Por Nome")
    print("2) Por CPF")
    print("3) Por ID")
    print("0) Voltar")
    opc = input("Selecione: ").strip()
    if opc == '0':
        return

    termo = input("Informe termo de busca: ").strip()
    if opc == '1':
        resultados = buscar_por_nome(termo)
    elif opc == '2':
        resultados = buscar_por_cpf(termo)
    elif opc == '3':
        try:
            resultados = buscar_por_id(int(termo))
        except ValueError:
            resultados = []
    else:
        print("Opção inválida.")
        input("Enter para continuar…")
        return

    limpar_tela()
    if not resultados:
        print("Nenhum paciente encontrado.")
        input("\nPressione Enter para voltar…")
        return

    print("Resultados encontrados:")
    for p in resultados:
        print(f"[{p.id}] {p.nome_completo} — CPF: {p.cpf}")

    sel = input("\nID para detalhes (0 para voltar): ").strip()
    if sel == '0':
        return

    try:
        pid = int(sel)
    except ValueError:
        print("ID inválido.")
        input("Enter para voltar…")
        return

    paciente = next((p for p in resultados if p.id == pid), None)
    if not paciente:
        paciente = buscar_por_id(pid)
        paciente = paciente[0] if paciente else None

    if not paciente:
        print("Paciente não encontrado.")
        input("Enter para voltar…")
        return

    exibir_detalhes(paciente)

def cadastrar_paciente_flow():
    """
    Se quiser manter o cadastro aqui, importe e use
    sua própria função cadastrar_paciente() do servicos.
    """
    from .recepcionista import pagina_cadastro
    from servicos.cadastro_pacientes import cadastrar_paciente

    limpar_tela()
    print("=== Cadastro de Paciente ===")
    dados = pagina_cadastro()
    if dados:
        cadastrar_paciente(
            dados['Nome completo'],
            dados['Data de nascimento'],
            dados['CPF'],
            dados['Sexo'],
            dados['Telefone'],
            dados['Endereço'],
            dados['Email'],
            dados['Tipo sanguíneo'],
            dados['Alergias conhecidas']
        )
        print("Paciente cadastrado com sucesso!")
        input("Pressione Enter para continuar…")