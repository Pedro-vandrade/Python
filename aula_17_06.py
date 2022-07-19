lista_idade = []
lista_altura = []

for qt_pessoas in range(5):
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    lista_idade.append(idade)
    lista_altura.append(altura)

for indice in range (4,-1, -1):
    print(f"idade: {lista_idade[qt]}) - Altura {lista_altura}")
