lista_salarios = []
lista_15 = []
lista_10 = []
while True:
    salario = float(input("Digite o salário do funcionário ou 0 para sair: "))
    if salario > 0:
        lista_salarios.append(salario)
    if salario <= 1250.00:
        sal15 = salario + (salario * 15 / 100)
        lista_15.append(sal15)
        print(f'Seu novo salário será de {sal15}, com aumento de 15%.')
    if salario > 1250.00:
        sal10 = salario + (salario * 10 / 100)
        lista_10.append(sal10)
        print(f"seu novo salário de de {sal10}, com aumento de 10%")
    if salario == 0:
        print(f'Salários com aumento de 15%: {lista_15}')
        print(f'Salários com aumento de 10%: {lista_10}')
        print("Fim do Programa")
