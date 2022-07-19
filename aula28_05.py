while True:
    escolha = input ()

'''    Menu
        1- Inserir números inteiros na listaA
        2- Imprimir listaA individualmente
        3- Retirar elemento listaA
        4- Ler um número e mostrar quantas vezes este se repete na listaA
5- Copiar todos elementos pares da listaA para a listaB
6- Copiar todos indices ímpares da listaA para a listaC
 7- ler um valor de indice e mostrar o elemento que ocupa esta posição na listaB
 8- Ler um número e mostrar qual seu índice na listaC.

        Escolha >>:'''


listaA = []
listaB = []
listaC = []


if escolha == "1":
    Numero = int(input("insira números:"))
    ListaA.append(numero)
    print(listaA)

if escolha == "3":
    listaA = [11,22,33,44,55,66]
    # retirando elemento pelo indice
    print(listaA)
    ind = int(input("Escolha u índice pra retirar o elemento:"))
    listaA.pop(ind)
    print(listaA)

    # retirando pelo elemento

    primt(listaA)
    elemento = int(input("Escoha um elemento:"))
    listaA.remove( elemento )


if escolha == "4"
        listaA = [2 ,2 ,2, 44, 33, 56, 77, 77, 9]
        repeticoes = listaA.count(2)
        print = repeticoes

if escolha == "5"
    listaA = [11, 22, 3, 4, 6, 7, 98, 45, 33, 8, 10]
        for pares in listaA:
            if valor % 2 == 0
            listaB.append(pares)
        print (listaB)
