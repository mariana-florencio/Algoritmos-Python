n1=int(input('Digite o 1º número:'))
n2=int(input('Digite o 2º número:'))
n3=int(input('Digite o 3º número:'))
if n1<=n2<=n3:
    print(f'Os números em ordem crescente são:{n1}, {n2} e {n3}')
elif n1<=n3<=n2:
    print(f'Os números em ordem crescente são:{n1}, {n3} e {n2}')
elif n2<=n1<=n3:
    print(f'Os números em ordem crescente são:{n2}, {n1} e {n3}')
elif n2<=n3<=n1:
    print(f'Os números em ordem crescente são:{n2}, {n3} e {n1}')
elif n3<=n1<=n2:
    print(f'Os números em ordem crescente são:{n3}, {n1} e {n2}')
else:
    print(f'Os números em ordem crescente são:{n3}, {n2} e {n1}')