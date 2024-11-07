peso=float(input('Digite seu peso[Kg]:'))
altura=float(input('Digite sua altura[M]:'))

imc=peso/(altura*altura)
print(f'Seu IMC é: {imc:.1f}')
if imc <18.5:
    print('Você está abaixo do ideal. SUGIRO UMA DIETA PARA GANHO DE PESO: \n'
          ' Coma 5 a 6 pequenas refeições durante o dia, em vez de duas ou três grandes refeições.'
          ' \nEscolha alimentos ricos em nutrientes, pães integrais, massas e cereais; frutas e vegetais; \nlacticínios; fontes de proteína;'
          ' e nozes e sementes.')
elif 18.5 <= imc <= 24.9:
    print('Seu peso é ideal. Mantenha assim!')
elif 25 <= imc <= 29.9:
    print('Você esta em sobrepeso. SUGIRO UMA DIETA PARA ELIMINAR GORDURA:\n'
          'Coma alimentos ricos em fibras, como frutas, legumes, verduras e cereais integrais . \nA fibra dos alimentos auxilia na saciedade. '
          'Legumes e verduras devem estar presentes no almoço e no jantar. \nFrutas devem estar presentes nos lanches.')
else:
    print('Você está em OBESIDADE! SUGIRO UMA DIETA E CARDIO DIARIAMENTE NO MÍNIMO 20 MINUTOS.\n'
          'RECOMENDAÇÕES GERAIS: mastigar bem os alimentos, preferir os alimentos ricos em fibras\n( verduras e legumes crus, frutas com casca e bagaço)'
          '. Nas refeições, comer primeiro os vegetais. Usar alimentos assados,\n cozidos ou grelhados. Evitar frituras e retirar peles e couros.')