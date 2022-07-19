y = float(input("Qual a altura da parede? "))
x = float(input("Qual a largura da parede? "))
tot = x * y
l = (x * y) / 2
print ("Sua parede tem {}m de altura e {}m de largura que equivale a {}m²".format(y, x, tot))
print ("Você precisa de {:.2f} litros de tinta para a pintura." .format(l))
