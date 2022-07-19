real = float(input("Quanto dinheiro você tem na carteira? "))
dol = float(input("Qual a cotação do US$? "))
peso = float(input("Qual a cotação do peso argentino? "))
eur = float(input("Qual a cotação do euro? "))
usd = real / dol
arg = real * peso
epsilon = real / eur
print ("Como valor de R$ {:.2f}, você pode comprar {:.2f}US$, ou comprar {:.2f} ARS (pesos aregentinos), ou {:.2f} euros" .format(real, usd, arg, epsilon))
