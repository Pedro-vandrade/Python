lista_produtos = ['1001', '1324', '6548', '2987', '7623']
lista_preços =   [ 5.32 ,  6.45 ,  2.37 ,  5.32 ,  6.45 ]

for ind in range(len(lista_produtos)):
    print(lista_produtos[ind].ljust(8),lista_preços[ind])
while True:
    cod = (input('Digite o código do produto escolhido: '))
    if cod in lista_produtos:
        qtd = input('Agora digite a quantidade : ')
        valor = qtd * lista_produtos.index(cod)
    else:
        print ('Produto não disponível!')
