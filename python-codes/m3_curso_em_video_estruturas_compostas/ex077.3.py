lista = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON',
         'CURSO','GRÁTIS','ESTUDAR','PRATICAR',
         'TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for c in lista:
    print(f'\nNa palavra {c} temos ',end='')
    for letra in c:
        if letra in 'AEIOUÁÉÓÂÊÔÕÍÃ':
            print(letra,end=' ')
