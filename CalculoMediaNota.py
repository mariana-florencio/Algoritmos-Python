p1=int(input('NOTA DA PROVA 1 [0 À 10]:'))
if p1<6:
    print('Você não atingiu a nota mínima 6. Faça a prova de recuperação.')
else:
    print('Você foi aprovado nessa prova! Parabéns.')
print('-=' *30)

p2=int(input('NOTA DA PROVA 2 [0 À 10]:'))
if p2<6:
    print('Você não atingiu a nota mínima 6. Faça a prova de recuperação.')
else:
    print('Você foi aprovado nessa prova! Parabéns.')
print('-=' *30)

t1=int(input('NOTA TRABALHO 1 [0 À 10]:'))
if t1<6:
    print('Você não atingiu a nota mínima 6. Faça a prova de recuperação.')
else:
    print('Você foi aprovado nesse trabalho! Parabéns.')
print('-=' *30)

t2=int(input('NOTA TRABALHO 2 [0 À 10]:'))
if t2<6:
    print('Você não atingiu a nota mínima 6. Faça a prova de recuperação.')
else:
    print('Você foi aprovado nesse trabalho ! Parabéns.')
mediaprova=(p1+p2)/2
mediatrab=(t1+t2)/2
mediafinal=(p1+p2+t1+t2)/4

print('-=' *30)
print(f'MÉDIA DAS PROVAS: {mediaprova}\nMÉDIA DOS TRABALHOS: {mediatrab}\nMÉDIA FINAL: {mediafinal}')

if mediafinal > 6:
    print('PARABÉNS!! VOCÊ FOI APROVADO NA DISCIPLINA.')
else:
    print('Você foi reprovado na disciplina.')
