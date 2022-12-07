class Jogador:
    __participou_partida: True

    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao  # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATACANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False  # ou True

    def get_nome(self):
        return self.__nome_jogador

    def get_numero(self):
        return self.__numero

    def get_posicao(self):
        return self.__posicao

    def get_participu_partida(self):
        return self.__participou_partida

    def get_expulsao(self):
        return self.__situacao


def exibir_menu():
    print('''MENU ======
    1 - Ler arquivo de    jogadores
    2 - Escalar time
    3 - Realizar Substiuição
    4 - Expulsão
    5 - Imprimir escalação
    
    Escolha: ''')


def ler_arquivo():
    with open('convocados.txt', 'r') as file:
        for valor in file:
            print(valor)
        file.close()


arquivo = open('convocados.txt', 'r')
leitura = arquivo.readline()
lst_reserva = []

for linha in leitura:
    lst_reserva.append(linha)
    arquivo.close()

lst_reserva = []
lst_escalados = []


def escalar_time():
    while True:
        titular = (input("Escale o time titular: "))
        if titular in lst_reserva:
            lst_escalados.append(titular)
        if len(lst_escalados) <= 11:
            break
        for jogador in lst_escalados:
            if titular == jogador.get_nome:
                jogador.__participou_partida = True
    print(lst_escalados)


lst_sub = []


def fazer_sub():
    print(lst_escalados)
    print(lst_reserva)
    for sub in lst_escalados:
        subst = str(input("Digite o jogador que você quer substituir: "))
        lst_sub.append(subst)
        if sub in lst_escalados:
            lst_escalados.remove(subst)
        reserva = str(input("Digite o jogador que entrará no jogo: "))
        if reserva in lst_reserva:
            lst_escalados.append(reserva)
            print(lst_escalados)
            for jogador2 in lst_escalados:
                if reserva == jogador2.get_nome:
                    reserva.__participou_partida = True


def expulsao_jogador():
    player = input('Digite o nome do jogador expulso: ')
    if player in lst_escalados:
        lst_escalados.remove(player)
        lst_reserva.append(player)
        print(f'o {player} foi expulso da partida.')


def imprimir_escalacao():
    with open('todosjogadores.txt', 'w') as subs:
        for item in lst_sub and lst_escalados:
            subs.write('\n' % item)
        open('todosjogadores.txt', 'r')
        subs.close()


while True:
    exibir_menu()
    opcao = int(input('Opção? '))
    if opcao == "1":
        ler_arquivo()
    if opcao == "2":
        escalar_time()
    if opcao == "3":
        fazer_sub()
    if opcao == "4":
        expulsao_jogador()
    if opcao == "5":
        imprimir_escalacao()
    break

exibir_menu()
ler_arquivo()
escalar_time()
fazer_sub()
expulsao_jogador()
imprimir_escalacao()
