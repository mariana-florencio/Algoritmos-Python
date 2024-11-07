print('Celsius-->Fahrenheit [1]'
      '\nFahrenheit-->Celsius [2]')
opcao=int(input('Digite a sua opção:'))

if opcao == 1:
    celsius=float(input('TEMPERATURA EM ºC:'))
    temperatura_fah=celsius*(9/5)+32
    print(f'{celsius}ºC é igual a: {temperatura_fah}ºF')
else:
    fahrenheit=float(input('TEMPERATURA EM ºF:'))
    temperatura_cel=(fahrenheit-32)*(5/9)
    print(f'{fahrenheit}ºF é igual a: {temperatura_cel}ºC')