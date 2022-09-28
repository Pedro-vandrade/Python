lista_salarios = []
while True:
    salario = float(input("Digite o salário do funcionário ou 0 para sair: "))
    lista_salarios.append(salario)
    if salario <= 1250.00:
        sal15 = salario + (salario * 15 / 100)
        print(f'Seu novo salário será de {sal15}, com aumento de 15%.')
    if salario > 1250.00:
        sal10 = salario + (salario * 10 / 100)
        print(f"seu novo salário de de {sal10}, com aumento de 10%")
    if salario == 0:
        print(lista_salarios)
        print("Fim do Programa")
