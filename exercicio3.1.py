n=int(input('Digite um número inteiro: '))
d=0
if n>1:
    for c in range(2,n):
        if n%c==0:
            d=d+1

    if d==0:
        print(f'{n} É UM NÚMERO PRIMO')
    else:
        print(f'{n} NÃO É UM NÚMERO PRIMO')

else:
    print(f'O NÚMERO DIGITADO NÃO É INTEIRO MAIOR QUE 1')