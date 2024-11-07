n = int(input('Digite um número: '))
print(f'Números primos até {n}:')

for num in range(2, n+1):
    divisores = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisores += 1
    if divisores == 2:
        print(num, 'é primo.')
