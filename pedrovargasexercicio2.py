login = []
senha = []
funcionarios = ['Pedro', 'Ana', 'Carlos', 'Maria Clara', 'João Antonio']
salarios = [3470.00,  2200.00,  3970.34,  7450.23,  5677.33]
opção = 0
while opção != 5:
    print('''MENU
        [1] Cadastrar Login e Senha
        [2] Aumento de 10%
        [3] Relatório
        [4] Cadastrar Funcionário
        [5] Fechar Programa
    ''')
    opção = int(input('Escolha: '))
    if opção == 1:
        login_user = str(input('Cadastre seu login: '))
        login.append(login_user)
        senha_user = int(input('Cadastre sua senha: '))
        senha.append(senha_user)
    elif opção == 2:
        medsal = sum(salarios) / len(salarios)
        print('Média Salarial: R$ {}'.format((medsal)))
        login1 = str(input('Digite seu login: '))
        senha1 = int(input('Digita sua senha: '))
        if (login1 == login_user and senha1 == senha_user):
            print('seja bem vindo')

        else:
            print('Login ou senha inválidos')
