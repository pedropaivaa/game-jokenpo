from random import randint
from time import sleep

itens = ("Pedra", "Papel","Tesoura")
computadorOpcao = randint(0,2)
print ("{:=^50}".format(" PEDRA PAPEL TESOURA "))

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')

usuario = int(input("Qual a sua jogada? "))

#Palavra JOKENPO irá aparecer devagar
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

print("-=" * 14)
print("O jogador jogou {}".format(itens[usuario]))
print("O computador jogou {}".format(itens[computadorOpcao]))
print("-=" * 14)

if computadorOpcao == 0:
    if usuario == 0:
        print("\033[4;33mEMPATE\033[0m")
    elif usuario == 1:
        print("\033[1;32m{} VENCE\033[0m".format('JOGADOR'))
    elif usuario == 2:
        print("\033[1;32m{} VENCE\033[0m".format('COMPUTADOR'))
    else:
        print("\033[1;31mENTRADA INVÁLIDA\033[0m")
elif computadorOpcao == 1:
    if usuario == 0:
        print("\033[1;32m{} VENCE\033[0m".format('COMPUTADOR'))
    elif usuario == 1:
        print("\033[4;33mEMPATE\033[0m")
    elif usuario == 2:
        print("\033[1;32m{} VENCE\033[0m".format('JOGADOR'))
    else:
        print("\033[1;31mENTRADA INVÁLIDA\033[0m")
elif computadorOpcao == 2:
    if usuario == 0:
        print("\033[1;32m{} VENCE\033[0m".format('JOGADOR'))
    elif usuario == 1:
        print("\033[1;32m{} VENCE\033[0m".format('COMPUTADOR'))
    elif usuario == 2:
        print("\033[4;33mEMPATE\033[0m")
    else:
        print("\033[1;31mENTRADA INVÁLIDA\033[0m")


# Testando se o computador está jogando corretamente as opções
# print("O computador jogou {}".format(itens[computadorOpcao]))
