from datetime import date
ano = int(input("Que ano você quer analisar? Se quiser analisar o ano atual, digite 0: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 00 and ano % 100 != 0 or ano % 400 ==0:
    print("o ano {} é BISSEXTO".format(ano))
else:
    print("O ano {} não é BISSEXTO.".format(ano))