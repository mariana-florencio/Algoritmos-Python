n=int(input('Digite um número inteiro para saber o nº de divisores: '))
if n>1:
    print(f'Divisores de {n}:')
    for c in range(1,n+1):
        if n%c==0:
            print(c, end='->')
    print('FIM')
else:
    print('VOCÊ DIGITOU UM NÚMERO NEGATIVO... TENTE NOVAMENTE!')




