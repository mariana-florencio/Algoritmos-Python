texto=str(input('Digite seu texto:'))
vogais=('aeiouAEIOU')
c=0

for caracteres in texto:
    if caracteres in vogais:
        c+=1
print(f'O total de vogais no texto digitado é:{c}')
