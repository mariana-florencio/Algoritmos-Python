from datetime import datetime
dia1=str(input('Digite o 1º dia:'))
mes1=str(input('Digite o 1º mes:'))
ano1=str(input('Digite o 1º ano:'))
dia2=str(input('Digite o 2º dia:'))
mes2=str(input('Digite o 2º mes:'))
ano2=str(input('Digite o 2º ano:'))
data1str=f'{dia1}-{mes1}-{ano1}'
data1=datetime.strptime(data1str, '%d-%m-%Y')
data1formatada=data1.strftime('%d-%m-%Y')
print(data1formatada)

data2str=f'{dia2}-{mes2}-{ano2}'
data2=datetime.strptime(data2str, '%d-%m-%Y')
data2formatada=data2.strftime('%d-%m-%Y')
print(data2formatada)

if data1formatada<data2formatada:
    print(f'A data: {data1formatada} ocorreu primeiro.')
elif data2formatada<data1formatada:
    print(f'A data: {data2formatada} ocorreu primeiro.')
else:
    print('As datas são as mesmas.')