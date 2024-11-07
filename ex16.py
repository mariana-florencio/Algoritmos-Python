from math import ceil
area=float(input('Tamanho em M² da área a ser pintada:'))
l_porlata=18
preço=80
cobertura=3
totallitros=area/cobertura
latastotais=ceil(totallitros/l_porlata)
totalpreço=latastotais*preço

print(f"qantidade de latas necessárias: {latastotais}")
print(f"preço total: R${totalpreço:.2f}")
