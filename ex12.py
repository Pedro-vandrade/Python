preço = float(input("Digite o preço do produto: R$"))
novo = preço - (preço * 5 / 100)
print("o valor do produto que custava R$ {:.2f} com deconto sera de R$ {:.2f}" .format(preço, novo))
