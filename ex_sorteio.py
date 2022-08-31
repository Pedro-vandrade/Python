import random
num = int(input("Digite um número de 1 a 5: "))
while num <= 1 and num <= 5:
    print("O número digitado pelo usuário foi {}.".format(num))
numsort = random.randint(1, 5)
print("o número sorteado foi {}".format(numsort))
if num == numsort:
    print("Você acertou o número!")
elif num != numsort:
    print("Você não adivinhou o número corretamente")
else:
    print("O número digitado não é válido.")