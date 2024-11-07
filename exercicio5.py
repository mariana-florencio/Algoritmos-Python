n=int(input('Digite um número inteiro positivo: '))
d=2
while n!=1:
    fator=False
    while n%d==0:
        n=n/d
        fator=True
    if fator:
        print(d)
    d+=1
