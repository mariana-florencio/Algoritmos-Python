tamanho=float(input('digite o tamanho do arquivo em MB:'))
velocidade=float(input('Digite a velocidade de um link de Internet em Mbps:'))
tempo= (tamanho*8)/(velocidade*60)
print(f'O tempo aproximado de download em minutos é de: {tempo:.2f}')