'''Fazer um Jo-Ken-Pô com a máquina'''

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

print('-='*14)

print('Computador jogou {}'.format(itens[computador]))

print('Jogador jogou  {}'.format(itens[jogador]))

print('=-'*14)

if computador == 0: #pedra

    if jogador == 0: 

        print('EMPATOU!!!')

    elif jogador == 1: 

        print('VOCÊ GANHOU!!!')

    else: print('VOCÊ PERDEU!!!')

elif computador == 1: #papel

    if jogador == 0: 

        print('VOCÊ PERDEU!!!')

    elif jogador == 1: 

        print('EMPATOU!!!')

    else: print('VOCÊ GANHOU!!!')

elif computador == 2: #tesoura

    if jogador == 0: 

        print('VOCÊ GANHOU!!!')

    elif jogador == 1: 

        print('VOCÊ PERDEU!!!')

    else: print('EMPATOU!!!')
