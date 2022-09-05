distancia = float(input("Qual a distância que você irá percorrer na sua viagem: "))
if distancia <= 200:
    valor1 = distancia * 0.50
    print("O valor da passagem será de R$ {:.2f} ".format(valor1))
else:
    valor2 = distancia * 0.45
    print("O valor da passagem será de R$ {:.2f} ".format(valor2))
