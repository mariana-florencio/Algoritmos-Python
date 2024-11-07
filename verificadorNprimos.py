n = int(input('Digite um número: '))

print(f'Numeros primos até {n}:')
for i in range(1,n+1):
    b = 0
    for c in range(1, i+1):
        if i % c == 0:
            b += 1
    #print(f'para {i} b é igual {b}')

    if b == 2:
        print(i, end=' ')

