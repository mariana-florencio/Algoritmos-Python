c=0
texto=str(input('Coloque seu texto aqui:')).lower()
palavra=str(input('Que palavra você deseja encontrar no texto?:')).lower()
posicao=texto.find(palavra)

while posicao != -1:
    c+=1
    print(f'A palavra {palavra} está na posição {posicao}')
    posicao = texto.find(palavra, posicao + 1)
if c==0:
    print(f'A palavra {palavra} não foi encontrada no texto')
