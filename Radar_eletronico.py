vel = float(input("Digite a velocidade do veículo: "))
print("Sua velocidade foi de {} km/h".format(vel))
if vel <= 80:
    print("Você está dirigindo dentro do limite permitido.")
else:
    multa = (vel-80) * 7
    print("Você excedeu o limite de velocidade e será multado. O Valor da sua multa será de {}".format(multa))