from servicos.auth import cadastrar_usuario


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
              '| 4 - Voltar ao menu inicial              | \n'
              '| 0 - Finalizar Sistema / Sair            | \n'
              '|                                         | \n'
              '|                                         | \n'
              '|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+| \n'
              '|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|\n'
              'l_________________________________________l')