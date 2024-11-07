frase=(input('Digite uma palavra ou frase:')).replace(' ', '').upper()

frase_invertida=frase[::-1].upper()

print(f'O inverso de {frase} é {frase_invertida}')
if frase == frase_invertida:
    print('É UM PALÍNDROMO.')
else:
    print('NÃO É UM PALÍNDROMO.')