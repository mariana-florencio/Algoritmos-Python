c=0
n=int(input('Digite um número inteiro para saber seus divisores:'))
if n>1:
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    print(f'Numero de divisores de {n}: {c}')
else:
    print('VOCÊ DIGITOU UM NÚMERO NEGATIVO... TENTE NOVAMENTE!')