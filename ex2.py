cont=0
str=(input('Digite seu texto:'))

sempontuacao=""
pontuacao='''.,:;!?'''
for c in str:
    if c not in pontuacao:
        sempontuacao+=c

lista_palavras=sempontuacao.split()
numero_palavras=len(lista_palavras)
print(f'No texto: "{str}". \nHá um total de {numero_palavras} palavras.')

