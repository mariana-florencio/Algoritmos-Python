from random import randint
numero_aleatorio=randint(1,100)
#print(numero_aleatorio)
usuario=0
while usuario != numero_aleatorio:
    usuario = int(input('Adivinhe o número:'))
    if usuario > numero_aleatorio:
        print('DICA: O número digitado é MAIOR que o número aleatório. Tente novamente.')
        print('-_'*25)
    elif usuario < numero_aleatorio:
        print('DICA: O número digitado é MENOR que o número aleatório. Tente novamente.')
        print('-_' * 25)
    else:
        print('Parabéns! Você venceu o jogo!')