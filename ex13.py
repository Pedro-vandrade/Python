sal = float(input("Digite o valor do salário: R$"))
novo = sal + (sal / 100 * 15)
print("o valor do salário que era de R$ {:.2f}, com acrescimo de 15%, sera de R$ {:.2f}" .format(sal, novo))
