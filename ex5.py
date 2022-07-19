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

listaA = [11, 22, 3, 4, 6, 7, 98, 45, 33, 8, 10]
listaB = []
for pares in listaA:
        if pares % 2 == 0:
            listaB.append(pares)
        print (listaB)
