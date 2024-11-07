cont=0
soma=0
string=str(input('Digite uma sequencia de numeros inteiros:'))
n=string.split()

print("Sequencia digitada: ")
for c in n:
    numeroint=int(c)
    cont+=1
    soma+=numeroint
    print(numeroint, end=' ')

media=soma/cont
print(f'\nMÉDIA: {media}')




