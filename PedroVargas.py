qtd = int(input("Quantidade de alunos: "))
i = 0
somaIDD = 0
while i < qtd:
    idd = int(input("Informe a idade: "))
    somaIDD = somaIDD + idd
    i += 1
mediaIDD = somaIDD / qtd
print ("A média das idades da turma é de: ", mediaIDD)
if mediaIDD > 0 & =< 25:
    print ("A turma é jovem")
if mediaIDD ==> 26 & ==< 60:
    print ("A turma é adulta")
if mediaIDD ==> 60
    print ("A Turma é idosa")

