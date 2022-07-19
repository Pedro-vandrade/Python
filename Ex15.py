km = float(input("digite quantos km você rodou com o veículo: "))
dia = int(input("digite durante quantos dias foi alugado: "))
preço = (km * 0.15) + (dia * 60)
print ("O valor a ser pago pelo aluguel do veículo, com o calculo de KM {:.2f} rodados e {} dias de aluguel, será de R$ {:.2f}" .format(km, dia, preço))
