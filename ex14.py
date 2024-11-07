kg=float(input('Peso dos peixes, em KG:'))
if kg>50:
    excesso=kg-50
    multa=excesso*4
    print(f'João, você teve {excesso}KG excedentes, sua multa será de R${multa:.2f}')
else:
    print('Você não teve quilos excedentes.')