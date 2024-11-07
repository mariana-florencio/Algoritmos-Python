n=int(input('Digite um número inteiro: '))
if n>1:
    primo=True
    for c in range(2, n):
        if n%c==0:
            primo=False
            break
    if primo:
        print(f'{n} é um número primo.')
    else:
        print(f'{n} não é um número primo.')
else:
    print(f'{n} não é um número primo, porque é menor ou igual a 1.')