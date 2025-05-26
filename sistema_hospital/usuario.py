# sistema_hospital/usuario.py

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_admin(usuario):
    """
    Painel Admin: daqui você pode implementar:
      - Gerenciamento de usuários
      - Relatórios
      - Configurações do sistema
    """
    while True:
        limpar_tela()
        print('=== Painel Admin ===')
        print('1) Listar usuários')
        print('2) Criar usuário')
        print('3) Excluir usuário')
        print('0) Voltar')
        opc = input("Selecione: ").strip()

        if opc == '1':
            # TODO: substituir por listagem real via serviço/BD
            print("Listando usuários... (a implementar)")
        elif opc == '2':
            print("Criar usuário... (a implementar)")
        elif opc == '3':
            print("Excluir usuário... (a implementar)")
        elif opc == '0':
            break
        else:
            print("Opção inválida.")
        input("Pressione Enter para continuar…")

def menu_usuario(usuario):
    """
    Painel de usuário autenticado.
    Recebe apenas o objeto `usuario`, que deve ter os atributos:
      - username
      - is_recepcionista (bool)
      - is_medico (bool)
      - is_admin (bool)
    """
    from .recepcionista import menu_recepcionista

    while True:
        limpar_tela()
        print(' _________________________________________')
        print('[                                         ]')
        print('#--------# Painel Administrativo #--------#')
        print('|                                         |')
        print(f'| Usuario: {usuario.username:<14}|')
        print('|                                         |')
        print('|               # Opções #                |')
        print('| ======================================= |')
        print('| 1 - Painel Recepcionista/Médico         |')
        print('| 2 - Painel Médico                       |')
        print('| 3 - Painel Admin                        |')
        print('| 0 - Finalizar Sistema / Sair            |')
        print('l_________________________________________l')

        opcao = input("Digite sua opção: ").strip()
        limpar_tela()

        if opcao == '1':
            if usuario.is_recepcionista or usuario.is_medico:
                menu_recepcionista(usuario)
            else:
                print('Sem permissão para Recepcionista.')
                input("Pressione Enter…")

        elif opcao == '2':
            if usuario.is_medico:
                print('Painel Médico ainda não implementado.')
            else:
                print('Sem permissão para Médico.')
            input("Pressione Enter…")

        elif opcao == '3':
            if usuario.is_admin:
                menu_admin(usuario)
            else:
                print('Sem permissão para Admin.')
            input("Pressione Enter…")

        elif opcao == '0':
            break

        else:
            print("Opção inválida.")
            input("Pressione Enter…")