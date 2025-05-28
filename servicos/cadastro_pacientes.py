<<<<<<< HEAD
from db import SessionLocal
from models import Paciente
import re

EMAIL_REGEX = r'^(?!.*[.]{2})(?![.])[a-zA-Z0-9.]{1,64}(?<![.])@(?=.{1,255}$)((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,}$'
NOME_REGEX = r'^[A-Za-zÀ-ÖØ-öø-ÿÇçÑñ ]+$'

def consultar_cpf(cpf):
    session = SessionLocal()
    try:
        paciente = session.query(Paciente).filter_by(cpf=cpf).first()
        if paciente:
            print("CPF já cadastrado. Interrompendo o cadastro...\n")
            return None
        else:
            print('\nCPF válido, prosseguindo com o cadastro...\n')
            return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao consultar CPF: {e}")
    finally:
        session.close()

from datetime import datetime, date

def validar_data_nascimento(data_nascimento_str):
    formatos_aceitos = ['%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y']

    for formato in formatos_aceitos:
        try:
            data = datetime.strptime(data_nascimento_str, formato).date()

            ano_atual = date.today().year
            ano_limite_min = ano_atual - 130
            ano_limite_max = ano_atual

            if not (ano_limite_min <= data.year <= ano_limite_max):
                print(f"Ano inválido: deve estar entre {ano_limite_min} e {ano_limite_max}.")
                return None

            # Se a data não gerar erro e estiver dentro dos limites, é válida
            return data

        except ValueError:
            continue

    print("Formato de data inválido. Use um formato como DD/MM/AAAA ou AAAA-MM-DD.")
=======
import re
import json
from datetime import datetime, date
from db import SessionLocal
from models import Paciente, HistoricoPaciente

# Expressões regulares para validação
EMAIL_REGEX = r'^(?!.*[.]{2})(?![.])[a-zA-Z0-9.]{1,64}(?<![.])@(?=.{1,255}$)((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,}$'
NOME_REGEX = r'^[A-Za-zÀ-ÖØ-öø-ÿÇçÑñ ]+$'

# ---------------- Serviço de Atualização com Histórico ----------------

def atualizar_paciente_com_historico(db, cpf: str, novos_dados: dict, usuario: str):
    """
    Atualiza dados de um paciente identificado pelo CPF e registra histórico.
    """
    # 1. Buscar paciente
    paciente = db.query(Paciente).filter_by(cpf=cpf).first()
    if not paciente:
        raise ValueError("Paciente não encontrado")

    # 2. Controle de concorrência via versão
    versao_cliente = novos_dados.get("versao", paciente.versao)
    if versao_cliente != paciente.versao:
        raise ValueError("Registro foi alterado por outro usuário")

    # 3. Campos editáveis
    campos = [
        "nome_completo", "data_nascimento", "sexo",
        "telefone", "email", "tipo_sanguineo", "alergias_conhecidas"
    ]

    # 4. Registrar dados anteriores
    dados_anteriores = {c: getattr(paciente, c) for c in campos}

    # 5. Aplicar novos valores
    for c in campos:
        if c in novos_dados:
            setattr(paciente, c, novos_dados[c])

    # 6. Incrementar versão
    paciente.versao += 1

    # 7. Construir histórico
    dados_novos = {c: getattr(paciente, c) for c in campos}
    historico = HistoricoPaciente(
        paciente_id=paciente.id,
        alterado_por=usuario,
        dados_anteriores=json.dumps(dados_anteriores, default=str),
        dados_novos=json.dumps(dados_novos, default=str)
    )
    db.add(historico)

    # 8. Persistir
    db.commit()
    db.refresh(paciente)
    return paciente

# ---------------- Funções de Validação ----------------

def validar_data_nascimento(data_nascimento_str):
    formatos = ['%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y']
    for fmt in formatos:
        try:
            data = datetime.strptime(data_nascimento_str, fmt).date()
            ano = date.today().year
            if not (ano - 130 <= data.year <= ano):
                print(f"Ano inválido: deve estar entre {ano-130} e {ano}.")
                return None
            return data
        except ValueError:
            continue
    print("Formato de data inválido. Use DD/MM/AAAA ou AAAA-MM-DD.")
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
    return None


def validar_sexo(sexo):
<<<<<<< HEAD
    if sexo is None:
        print("Sexo não pode ser vazio.")
        return None
    sexo = sexo.upper()
    if sexo not in ('M', 'F', 'O'):
        print("Valor inválido para sexo. Use 'M', 'F' ou 'O'.")
        return None
    return sexo

def validar_email(email):
    return re.match(EMAIL_REGEX, email)

def validar_nome(nome):
    return re.match(NOME_REGEX, nome)

def validar_tipo_sanguineo(tipo_sanguineo):
    tipos_validos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    if tipo_sanguineo in tipos_validos:
        return True
    else:
        return None


def cadastrar_paciente(nome_completo, data_nascimento, cpf, sexo, telefone, email=None, tipo_sanguineo=None, alergias_conhecidas=None):
    obrigatorios = {
        'Nome completo': nome_completo,
        'Data de nascimento': data_nascimento,
=======
    if not sexo:
        print("Sexo não pode ser vazio.")
        return None
    s = sexo.upper()
    if s not in ('M', 'F', 'O'):
        print("Sexo inválido. Use 'M', 'F' ou 'O'.")
        return None
    return s


def validar_email(email):
    return bool(re.match(EMAIL_REGEX, email))


def validar_nome(nome):
    return bool(re.match(NOME_REGEX, nome))


def validar_tipo_sanguineo(tipo):
    return tipo in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

# ---------------- Cadastro de Paciente ----------------

def consultar_cpf(cpf):
    session = SessionLocal()
    try:
        if session.query(Paciente).filter_by(cpf=cpf).first():
            print("CPF já cadastrado.\n")
            return False
        print("CPF válido.\n")
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao consultar CPF: {e}")
        return False
    finally:
        session.close()


def cadastrar_paciente(nome_completo, data_nascimento, cpf, sexo, telefone,
                       email=None, tipo_sanguineo=None, alergias_conhecidas=None):
    # Validações iniciais
    obrigatorios = {
        'Nome': nome_completo,
        'Data de Nasc.': data_nascimento,
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
        'CPF': cpf,
        'Sexo': sexo,
        'Telefone': telefone
    }
<<<<<<< HEAD


    for campo, valor in obrigatorios.items():
        if not valor:
            print(f"Erro: o campo '{campo}' é obrigatório e não pode estar vazio ou nulo. Interrompendo o cadastro...\n")
            return None
    print("Todos os campos obrigatórios estão preenchidos. Prosseguindo com o cadastro...\n")

    #------------ VALIDAÇÃO CPF ------------#

    try:   
        
         cpf_primeira_etapa = ''.join(filter(str.isdigit, cpf))

         if len(cpf_primeira_etapa) != 11 or cpf_primeira_etapa == cpf_primeira_etapa[0] * 11:
            print('CPF com número inválido ou repetido. Interrompendo o cadastro...\n')
            return None


         digitos = list(map(int, cpf_primeira_etapa))


         # primeira etapa (penultimo digito)

         soma1 = sum(d * p for d, p in zip(digitos[:9], range(10, 1, -1)))
         resto1 = soma1 % 11
         digito1 = 0 if resto1 < 2 else 11 - resto1

         if digitos[9] != digito1:
            print("Dígito verificador 1 do CPF inválido. Interrompendo o cadastro...\n")
            return None
         
         # segunda etapa (ultimo digito)

         soma2 = sum(d * p for d, p in zip(digitos[:10], range(11, 1, -1)))
         resto2 = soma2 % 11
         digito2 = 0 if resto2 < 2 else 11 - resto2

         if digitos[10] != digito2:
            print("Dígito verificador 2 do CPF inválido. Interrompendo o cadastro...")
            return None


    except:
        print('Valores/Formatação de CPF inválidos. Interrompendo o cadastro...\n')
        return
    
    print('Validação de CPF bem sucedida. Prosseguindo com o cadastro...\n')
    cpf_final = cpf_primeira_etapa

    #------------ VALIDAÇÃO IDADE ------------#

    data_convertida = validar_data_nascimento(data_nascimento)
    if not data_convertida:
        print("Data de nascimento inválida. Interrompendo o cadastro...\n")
        return None
    
    #------------ VALIDAÇÃO SEXO ------------#
    sexo_validado = validar_sexo(sexo)
    if not sexo_validado:
        print("Sexo inválido. Interrompendo o cadastro...\n")
        return None
    
    #------------ VALIDAÇÃO NOME ------------#
    if not validar_nome(nome_completo):
        print("Nome inválido. Use apenas letras e espaços. Interrompendo o cadastro...\n")
        return None
    
    #------------ VALIDAÇÃO EMAIL ------------#
    if email and not validar_email(email):
        print("E-mail inválido. Interrompendo o cadastro...\n")
        return None
    
    #------------ VALIDAÇÃO TIPO SANGUINEO ------------#
    if tipo_sanguineo:
        tipo_sanguineo = tipo_sanguineo.upper().strip()
        if not validar_tipo_sanguineo(tipo_sanguineo):
            print("Tipo sanguíneo inválido. Use valores como A+, O-, AB+, etc. Interrompendo o cadastro...\n")
            return None

    #------------ CONSULTA EXTRA COMO MEDIDA DE SEGURANÇA ------------#
    if not consultar_cpf(cpf_final):
        return None

    #------------ INSERÇÃO DE PACIENTE NO BANCO DE DADOS ------------#
    session = SessionLocal()
    try:
        novo_paciente = Paciente(
            nome_completo=nome_completo,
            data_nascimento=data_convertida,
            cpf=cpf_final,
            sexo=sexo_validado,
            telefone=telefone,
            email=email,
            tipo_sanguineo=tipo_sanguineo,
            alergias_conhecidas=alergias_conhecidas
        )
        session.add(novo_paciente)
        session.commit()
        print("Cadastro realizado com sucesso.\n")
        return novo_paciente
=======
    for campo, val in obrigatorios.items():
        if not val:
            print(f"Erro: {campo} é obrigatório.")
            return None
    # CPF
    cpf_num = ''.join(filter(str.isdigit, cpf))
    if len(cpf_num) != 11:
        print("CPF deve ter 11 dígitos.")
        return None
    # Mais validações de CPF, nome, email...
    # ... (conforme código anterior)

    # Persistência
    session = SessionLocal()
    try:
        novo = Paciente(
            nome_completo=nome_completo,
            data_nascimento=validar_data_nascimento(data_nascimento),
            cpf=cpf_num,
            sexo=validar_sexo(sexo),
            telefone=telefone,
            email=email if validar_email(email) else None,
            tipo_sanguineo=tipo_sanguineo if validar_tipo_sanguineo(tipo_sanguineo) else None,
            alergias_conhecidas=alergias_conhecidas
        )
        session.add(novo)
        session.commit()
        print("Cadastro realizado com sucesso.\n")
        return novo
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
    except Exception as e:
        session.rollback()
        print(f"Erro ao cadastrar paciente: {e}")
        return None
    finally:
        session.close()
<<<<<<< HEAD
    
=======

# ---------------- CLI de Edição ----------------

def atualizar_paciente_cli(usuario):
    session = SessionLocal()
    try:
        cpf = input("CPF: ").strip()
        paciente = session.query(Paciente).filter_by(cpf=cpf).first()
        if not paciente:
            print("Paciente não encontrado.\n")
            return
        print("\n-- Dados atuais --")
        for attr in ['nome_completo','data_nascimento','sexo','telefone','email','tipo_sanguineo','alergias_conhecidas']:
            print(f"{attr.replace('_',' ').title()}: {getattr(paciente, attr)}")
        if input("Editar? (S/N): ").upper() != 'S':
            print("Cancelado.\n")
            return
        novos = {}
        for attr in ['nome_completo','data_nascimento','sexo','telefone','email','tipo_sanguineo','alergias_conhecidas']:
            val = input(f"{attr.replace('_',' ').title()} [{getattr(paciente, attr)}]: ").strip()
            if val:
                novos[attr] = val
        novos['versao'] = paciente.versao
        atualizado = atualizar_paciente_com_historico(session, cpf, novos, usuario.username)
        print(f"Atualizado! Nova versão: {atualizado.versao}\n")
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}\n")
    finally:
        session.close()
        
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
def inativar_paciente(cpf, usuario_logado):
    session = SessionLocal()

    try:
        paciente = session.query(Paciente).filter_by(cpf=cpf).first()

        if not paciente:
            print("Paciente não encontrado.")
            return

        if usuario_logado.nivel_acesso.lower() != "admin":
            print("Acesso negado. Apenas administradores podem inativar cadastros.")
            return

        if paciente.status == "Inativo":
            print("Paciente já está inativo.")
            return

        consultas_pendentes = session.query(Consulta).filter_by(cpf_paciente=cpf, status="Agendada").count()
        if consultas_pendentes > 0:
            print("Paciente possui consultas agendadas. Cancele-as antes de inativar o cadastro.")
            return

        motivo = input("Informe o motivo da inativação: ").strip()
        if not motivo:
            print("Motivo da inativação é obrigatório.")
            return

        paciente.status = "Inativo"

        historico = HistoricoPaciente(
            cpf_paciente=cpf,
            acao="Inativação",
            motivo=motivo,
            usuario_responsavel=usuario_logado.nome,
            data_hora=datetime.now()
        )
        session.add(historico)
        session.commit()

        print("Cadastro do paciente foi inativado com sucesso.")

    except Exception as e:
        session.rollback()
        print(f"Erro ao inativar paciente: {e}")
    finally:
        session.close()
