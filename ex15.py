ganha_hora=float(input('Quanto voê ganha por hora: R$'))
num_horas=int(input('Quantas horas você trabalha no mês:'))

tot=ganha_hora*num_horas
ir=tot*0.11
inss=tot*0.08
sind=tot*0.05
liq=(tot-ir)-(inss-sind)

print(f'Salario bruto: R${tot:.2f}')
print(f'Imposto de renda (11%): R${ir:.2f}')
print(f'INSS (8%): R${inss:.2f}')
print(f'Sindicato (5%): R${sind:.2f}')
print(f'Salario líquido: R${liq:.2f}')