a=float(input('Digite o número A:'))
b=float(input('Digite o número B:'))
c=float(input('Digite o número C:'))
if a!=0:
    delta= ((b)**2)-4*a*c
    if delta>=0:
        raizmais=(-b+(delta**0.5))/2*a
        raizmenos=(-b-(delta**0.5))/2*a
        print(f'As raizes são: {raizmais} e {raizmenos}.')
    else:
        print('Não possi raizes reais pois o DELTA é menor que 0.')
else:
    #se a=0
    print('a=0, entao a operação é uma euação do 1º grau de solução:',-c/b)
