import random
numuser = int(input("Digite um número entre de 1 a 5: "))
if 1 > numuser > 5:
    print('Digite um número de 1 a 5')
print("O número digitado pelo usuário foi {}.".format(numuser))
numsorteio = random.randint(1, 5)
print("o número sorteado foi {}".format(numsorteio))
if numuser == numsorteio:
    print("Você escolheu um número igual ao sorteado.")
else:
    print("o númer escolhido não foi o mesmo do que o sorteado.")
