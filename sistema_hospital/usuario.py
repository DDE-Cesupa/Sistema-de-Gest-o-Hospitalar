from servicos.cadastro_pacientes import consultar_cpf, cadastrar_paciente
from . recepcionista import menu_recepcionista
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_usuario(usuario, is_recepcionista, is_medico, is_admin):
    usuario_exibicao = usuario

    while True:
        print(' _________________________________________  \n'
              '[                                         ] \n'
              '#--------# Painel Administrativo #--------# \n'
              '|                                         | \n'
              '| - Selecione a opção:                    | \n'
              '|                                         | \n'
             f'| Usuario:{usuario_exibicao}{(14 - len(usuario_exibicao))*' '}| \n'
              '|                                         | \n'
              '|               # Opções #                | \n'
              '| ======================================= | \n'
              '|                                         | \n'
              '| 1 - Acessar painel Recepcionista        | \n'
              '| 2 - Acessar painel Médico               | \n'
              '| 3 - Acessar painel Admin                | \n'
              '| 0 - Finalizar Sistema / Sair            | \n'
              '|                                         | \n'
              '|                                         | \n'
              '|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+| \n'
              '|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|\n'
              'l_________________________________________l')
        
        opcao = input("Digite sua opção: ")
        limpar_tela()
        if opcao == '1':
            if is_recepcionista:
                return menu_recepcionista(usuario)
            else:
                print('Usuario não tem permissão para acessar painel Recepcionista.\n')

        elif opcao == '2':
            if is_medico:
                #adicionar menu_medico no futuro
                return
            else:
                print('Usuario não tem permissão para acessar painel Médico.\n')
        elif opcao == '3':
            if is_admin:
                #adicionar menu_admin no futuro
                return
            else:
                print('Usuario não tem permissão para acessar painel Admin.\n')
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

