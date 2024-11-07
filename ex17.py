from math import ceil
area=float(input('Tamanho em M² da área a ser pintada:'))
preço_lata=80
preço_galão=25
cobertura=6
litros_necessarios= area/cobertura
latas=ceil(litros_necessarios/18)
galoes=ceil(litros_necessarios/3.6)

preçototal_lata=latas*preço_lata
print('APENAS LATAS DE 18 LITROS:')
print(f'Nº de latas:{latas}')
print(f'Preço: R${preçototal_lata}')

preçototal_galao= preço_galão*galoes
print('APENAS GALÕES DE 3,6 LITROS:')
print(f'Nº de galões:{galoes}')
print(f'Preço: R${preçototal_galao}')



