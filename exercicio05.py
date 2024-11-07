print('=====PERA, PAPEL E TESOURA=====')
print('\n 1)PEDRA \n 2)PAPEL \n 3)TESOURA')
jogadora=str(input('Jogador A, digite sua jogada:'))
jogadorb=str(input('Jogador B, digite sua jogada:'))
if jogadora=='1' and jogadorb=='2':
    print('Jogador B ganha')
elif jogadora=='2' and jogadorb=='1':
    print('Jogador A ganha')

elif jogadora=='1' and jogadorb=='3':
    print('Jogador A ganha')
elif jogadora=='3' and jogadorb=='1':
    print('Jogador B ganha')

elif jogadora=='2' and jogadorb=='3':
    print('Jogador B ganha')
elif jogadora=='3' and jogadorb=='2':
    print('Jogador A ganha')

elif jogadora=='1' and jogadorb=='1':
    print('EMPATE')
elif jogadora=='2' and jogadorb=='2':
    print('EMPATE')
elif jogadora=='3' and jogadorb=='3':
    print('EMPATE')
