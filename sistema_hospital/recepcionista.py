<<<<<<< HEAD
from servicos.cadastro_pacientes import consultar_cpf, cadastrar_paciente
=======
from servicos.cadastro_pacientes import consultar_cpf, cadastrar_paciente, atualizar_paciente_cli
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
from .consultarUsuario import consultar_paciente
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

posicao_dados = [
<<<<<<< HEAD
             'CPF',
             'Nome completo',
             'Data de nascimento',
             'Sexo',
             'Telefone',
             'Endereço',
             'Email',
             'Tipo sanguíneo',
             'Alergias conhecidas'
]

def menu_recepcionista(usuario):

=======
    'CPF', 'Nome completo', 'Data de nascimento',
    'Sexo', 'Telefone', 'Endereço',
    'Email', 'Tipo sanguíneo', 'Alergias conhecidas'
]

def menu_recepcionista(usuario):
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
    usuario_exibicao = usuario
    usuario_permissao = 'Recepcionista'

    while True:
<<<<<<< HEAD
        print(' _________________________________________  \n'
              '[                                         ] \n'
              '#--------# Painel Administrativo #--------# \n'
              '|                                         | \n'
              '| - Selecione a opção:                    | \n'
              '|                                         | \n'
             f'| Usuário: {usuario.username:<30}         | \n'
             f'| Nome: {usuario.nome_completo:<30}       | \n'
              '|               # Opções #                | \n'
              '| ======================================= | \n'
              '|                                         | \n'
              '| 1 - Cadastrar Paciente                  | \n'
              '| 2 - Consultar dados do paciente         | \n'
              '| 0 - Finalizar Sistema / Sair            | \n'
              '|                                         | \n'
              '|                                         | \n'
              '|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+| \n'
              '|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|\n'
              'l_________________________________________l')
        
=======
        print(' _________________________________________  ')
        print('[                                         ] ')
        print('#--------# Painel Administrativo #--------# ')
        print('|                                         | ')
        print('| - Selecione a opção:                    | ')
        print('|                                         | ')
        print(f'| Usuário: {usuario.username:<30}         | ')
        print(f'| Nome: {usuario.nome_completo:<30}       | ')
        print('|               # Opções #                | ')
        print('| ======================================= | ')
        print('|                                         | ')
        print('| 1 - Cadastrar Paciente                  | ')
        print('| 2 - Consultar dados do paciente         | ')
        print('| 3 - Editar cadastro de paciente         | ')
        print('| 0 - Finalizar Sistema / Sair            | ')
        print('|                                         | ')
        print('|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+| ')
        print('|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-| ')
        print('l_________________________________________l')

>>>>>>> 5d35a02 (Implementação do caso de uso 3)
        opcao = input("Digite sua opção: ")
        limpar_tela()
        if opcao == '1':
            print("Você escolheu Cadastrar Paciente.\n")
            dados_cadastro = pagina_cadastro()
            if dados_cadastro:
<<<<<<< HEAD
                #if consultar_cpf(dados_cadastro['CPF']):
=======
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
                cadastrar_paciente(
                    dados_cadastro['Nome completo'],
                    dados_cadastro['Data de nascimento'],
                    dados_cadastro['CPF'],
                    dados_cadastro['Sexo'],
                    dados_cadastro['Telefone'],
                    dados_cadastro['Email'],
                    dados_cadastro['Tipo sanguíneo'],
<<<<<<< HEAD
                    dados_cadastro['Alergias conhecidas'])
        elif opcao == "2":
            print("Você escolheu consultar os dados.\n")
            consultar_paciente()            
=======
                    dados_cadastro['Alergias conhecidas']
                )
        elif opcao == '2':
            print("Você escolheu consultar os dados.\n")
            consultar_paciente()
        elif opcao == '3':
            print("Você escolheu Editar cadastro de paciente.\n")
            atualizar_paciente_cli(usuario)
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

#------------------- LOGICA DE PAGINAS ----------------------#

def pagina_cadastro(pagina_atual=1, dados=None):
    if dados is None:
<<<<<<< HEAD
        dados = {
            'CPF': '',
            'Nome completo': '',
            'Data de nascimento': '',
            'Sexo': '',
            'Telefone': '',
            'Endereço': '',
            'Email': '',
            'Tipo sanguíneo': '',
            'Alergias conhecidas': ''
        }
=======
        dados = {campo: '' for campo in posicao_dados}
>>>>>>> 5d35a02 (Implementação do caso de uso 3)

    while True:
        limpar_tela()
        category_name = posicao_dados[pagina_atual - 1]
        parameter = dados[category_name]

<<<<<<< HEAD
        print(f' __________________________________________{len(parameter + category_name) * "_"}\n'
              f'|{" " * len(parameter + category_name)}                                          |\n'
              f'|Cadastro de Usuário{" " * len(parameter + category_name)}                       |\n'
              f'|Painel Administrativo ->{" " * len(parameter + category_name)}                  |\n'
              f'|{" " * len(parameter + category_name)}                                          |\n'
              f'| - Pág: {pagina_atual}/9{" " * len(parameter + category_name)}                  |\n'
              f'| - Selecione a opção:{" " * len(parameter + category_name)}                     |\n'
              f'|{" " * len(parameter + category_name)}                                          |\n'
              f'| - {category_name}: {parameter}                                                 |\n'
              f'|{" " * len(parameter + category_name)}                                          |\n'
              f'|# Opções #{" " * len(parameter + category_name)}                                |\n'
              f'={"=" * len(parameter + category_name)}==========================================\n'
              f'| 1 - Informar/Editar {category_name}{" " * len(parameter)}                      |\n'
              f'| 2 - Avançar Página{" " * len(parameter + category_name)}                       |\n'
              f'| 3 - Voltar Página{" " * len(parameter + category_name)}                        |\n'
              f'| 4 - Cadastrar Paciente{" " * len(parameter + category_name)}                   |\n'
              f'| 5 - Cancelar Cadastro{" " * len(parameter + category_name)}                    |\n'
              f'| 6 - Preencher todos os dados de uma vez{" " * len(parameter + category_name)}  |\n'
              f'| 0 - Finalizar Sistema / Sair{" " * len(parameter + category_name)}             |\n'
              f'|__________________________________________{len(parameter + category_name) * "_"}|\n')
=======
        print(f' __________________________________________{"_" * (len(parameter + category_name))}')
        print(f'| Cadastro de Usuário{' ' * (len(parameter + category_name))}|')
        print(f'| Painel Administrativo ->{' ' * (len(parameter + category_name))}|')
        print(f'| - Pág: {pagina_atual}/9{' ' * (len(parameter + category_name))}|')
        print(f'| - {category_name}: {parameter}{' ' * (len(parameter + category_name))}|')
        print(f'| Opções: 1-Editar 2-Avançar 3-Voltar 4-Cadastrar 5-Cancelar 6-Preencher 0-Sair{' ' * (len(parameter + category_name))}|')
        print(f'|__________________________________________{"_" * (len(parameter + category_name))}|')
>>>>>>> 5d35a02 (Implementação do caso de uso 3)

        opcao = input("Digite sua opção: ").strip()

        if opcao == '1':
<<<<<<< HEAD
            print(f"Você escolheu Informar/Editar {category_name}.\n")
            novo_valor = input(f"Informe {category_name}: ").strip()
            dados[category_name] = novo_valor

        elif opcao == '2':
            if pagina_atual < len(posicao_dados):
                pagina_atual += 1
            else:
                print("Já está na última página.")
                input("Pressione Enter para continuar...")

        elif opcao == '3':
            if pagina_atual > 1:
                pagina_atual -= 1
            else:
                print("Já está na primeira página.")
                input("Pressione Enter para continuar...")

        elif opcao == '4':
            # Verificar campos obrigatórios
            campos_obrigatorios = ['CPF', 'Nome completo', 'Data de nascimento', 'Sexo', 'Telefone']
            faltando = [campo for campo in campos_obrigatorios if not dados[campo].strip()]
            if faltando:
                print(f"\n⚠️  Cadastro incompleto! Preencha os campos obrigatórios: {', '.join(faltando)}")
                input("Pressione Enter para continuar...")
            else:
                return dados

        elif opcao == '5':
            print("Cadastro cancelado.")
            return None

        elif opcao == '6':
            print("\n--- Preenchendo todos os campos ---\n")
            for campo in posicao_dados:
                atual = dados[campo]
                entrada = input(f"{campo} [{atual}]: ").strip()
                if entrada:
                    dados[campo] = entrada
            print("\n✔️ Dados atualizados.")
            input("Pressione Enter para continuar...")

        elif opcao == '0':
            print("Saindo do cadastro.")
            return None

        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")
=======
            novo_valor = input(f"Informe {category_name}: ").strip()
            dados[category_name] = novo_valor
        elif opcao == '2':
            pagina_atual = min(pagina_atual + 1, len(posicao_dados))
        elif opcao == '3':
            pagina_atual = max(pagina_atual - 1, 1)
        elif opcao == '4':
            campos_obrigatorios = posicao_dados[:5]
            faltando = [campo for campo in campos_obrigatorios if not dados[campo].strip()]
            if faltando:
                print(f"⚠️ Campos faltando: {', '.join(faltando)}")
                input("Enter para continuar...")
            else:
                return dados
        elif opcao == '5':
            print("Cadastro cancelado.")
            return None
        elif opcao == '6':
            for campo in posicao_dados:
                valor = input(f"{campo} [{dados[campo]}]: ").strip()
                if valor:
                    dados[campo] = valor
            print("✔️ Dados atualizados.")
            input("Enter para continuar...")
        elif opcao == '0':
            return None
        else:
            print("Opção inválida.")
            input("Enter para continuar...")
>>>>>>> 5d35a02 (Implementação do caso de uso 3)
