from servicos.auth import autenticar_usuario
from .usuario import menu_usuario
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_login():

    email = '                                  '
    senha = '                                  '
    email_exibicao, senha_exibicao = email, senha

    while True:
        print(' _________________________________________  \n'
              '[                                         ] \n'
              '#----------#       Login       #----------# \n'
              '|                                         | \n'
              '| - Selecione a opção:        Pág: 1      | \n'
              '|                                         | \n'
             f'| email:{email_exibicao}| \n'
             f'| senha:{senha_exibicao}| \n'
              '|               # Opções #                | \n'
              '| ======================================= | \n'
              '|                                         | \n'
              '| 1 - Inserir email                       | \n'
              '| 2 - Inserir senha                       | \n'
              '| 3 - Entrar                              | \n'
              '| 0 - Finalizar Sistema / Sair            | \n'
              '|                                         | \n'
              '|                                         | \n'
              '|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+| \n'
              '|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|\n'
              'l_________________________________________l')

        opcao = input("Digite sua opção: ")
        limpar_tela()
        if opcao == '1':
            print("Você escolheu Inserir email.\n")
            email = input("Insira seu email: ")
            email_exibicao = email + ' ' * (34 - len(email))

            # aqui você pode chamar a função que trata o login, por exemplo
        elif opcao == '2':
            print("Você escolheu Inserir senha.\n")
            senha = input("Insira sua senha: ")
            senha_exibicao = ('*' * len(senha)) + ' ' * (34 - len(senha))

        elif opcao == '3':
            print("Você escolheu Entrar.\n")
            usuario = autenticar_usuario(email, senha)
            if usuario is None:
                print("Email e/ou senha incorretos. Por favor, tente novamente.")
            else:
                print(f"Bem-vindo, {usuario.nome_completo}!")
                return menu_usuario(usuario.username, usuario.is_recepcionista, usuario.is_medico, usuario.is_medico)
            
        elif opcao == '0':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_login()