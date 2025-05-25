from .login import menu_login
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    limpar_tela()

    condicao = True

    while condicao:
        print(' _________________________________________  \n'
              '[                                         ] \n'
              '#-----#Bem-Vindo ao Menu Interativo #-----# \n'
              '|                                         | \n'
              '| - Selecione a opção:        Pág: 0      | \n'
              '|                                         | \n'
              '|                                         | \n'
              '|               # Opções #                | \n'
              '| ======================================= | \n'
              '|                                         | \n'
              '| 1 - Entrar como Usuário                 | \n'
              '| 0 - Finalizar Sistema / Sair            | \n'
              '|                                         | \n'
              '|                                         | \n'
              '|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+| \n'
              '|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|\n'
              'l_________________________________________l')

        opcao = input("Digite sua opção: ")
        limpar_tela()
        
        if opcao == "1":
            print("Você escolheu entrar como Usuário")
            return menu_login()
            # aqui você pode chamar a função que trata o login, por exemplo
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            condicao = False
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
