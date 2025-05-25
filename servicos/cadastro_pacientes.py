from db import SessionLocal
from models import Paciente

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
    return None


def validar_sexo(sexo):
    if sexo is None:
        print("Sexo não pode ser vazio.")
        return False
    sexo = sexo.upper()
    if sexo not in ('M', 'F', 'O'):
        print("Valor inválido para sexo. Use 'M', 'F' ou 'O'.")
        return False
    return sexo

def cadastrar_paciente(nome_completo, data_nascimento, cpf, sexo, telefone, email=None, tipo_sanguineo=None, alergias_conhecidas=None):
    obrigatorios = {
        'Nome completo': nome_completo,
        'Data de nascimento': data_nascimento,
        'CPF': cpf,
        'Sexo': sexo,
        'Telefone': telefone
    }


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

    return
    